"""
Modelo de la SpiderCam virtual (OE-01, OE-02).

Responsabilidad:
    Mantener el estado (posición actual X, Y, Z) del carro/cámara y
    actualizarlo en cada paso de simulación a partir de la señal de
    control. Internamente usa geometry.cable_kinematics solo para
    exponer las longitudes de cable a la capa de visualización.
"""


class SpiderCamModel:
    def __init__(self, stadium, initial_position):
        self.stadium = stadium
        self.position = initial_position

    def update(self, control_signal, dt: float):
        """Actualiza la posición del carro según la señal de control."""
        raise NotImplementedError

    def get_cable_lengths(self):
        """Longitudes actuales de los 4 cables (para visualización)."""
        raise NotImplementedError
