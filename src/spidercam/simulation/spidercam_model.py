"""
Modelo de la SpiderCam virtual (OE-01, OE-02).

Responsabilidad:
    Mantener el estado (posición actual X, Y, Z) del carro/cámara y
    actualizarlo en cada paso de simulación a partir de una señal de
    velocidad. Internamente usa geometry.cable_kinematics solo para
    exponer las longitudes de cable a la capa de visualización.

Modelo de movimiento (decisión de diseño):
    update() recibe una VELOCIDAD (m/s), no una posición objetivo. Es un
    integrador de primer orden simple (sin aceleración/inercia), con la
    velocidad limitada a max_speed_m_s y la posición resultante saturada
    al volumen de trabajo físico del rig (Stadium.workspace_bounds).
    Esto prepara el terreno para la Fase 7 (PID): el controlador
    calculará naturalmente una velocidad de corrección a partir del
    error de posición.
"""
import numpy as np

from spidercam.geometry.cable_kinematics import CableKinematics
import numpy as np

class SpiderCamModel:
    def __init__(self, stadium, initial_position, max_speed_m_s: float = 5.0):
        self.stadium = stadium
        self.position = np.array(initial_position, dtype=float)
        self.max_speed_m_s = max_speed_m_s
        self._cable_kinematics = CableKinematics(stadium.anchor_points)

    def update(self, velocity_command, dt: float):
        """Integra la posición un paso dt a partir de una velocidad deseada.

        1. Limita la magnitud de la velocidad a max_speed_m_s (conserva dirección).
        2. Integra: posición += velocidad * dt.
        3. Satura la posición resultante al volumen de trabajo físico.
        """
        v = np.array(velocity_command, dtype=float)
        speed = np.linalg.norm(v)
        if speed > self.max_speed_m_s and speed > 0:
            v = v * (self.max_speed_m_s / speed)

        candidate_position = self.position + v * dt
        self.position = self._clip_to_workspace(candidate_position)
        return self.position

    def get_cable_lengths(self):
        """Longitudes actuales de los 4 cables (para visualización)."""
        return self._cable_kinematics.calculate_lengths(self.position)

    def _clip_to_workspace(self, position):
        """Satura la posición al volumen de trabajo físico del rig."""
        x_min, x_max, y_min, y_max, z_min, z_max = self.stadium.workspace_bounds
        x, y, z = position
        return np.array([
            np.clip(x, x_min, x_max),
            np.clip(y, y_min, y_max),
            np.clip(z, z_min, z_max),
        ])
