"""
Generador de referencias para la SpiderCam (OE-05, RF-05).

Responsabilidad:
    A partir de la trayectoria estimada del balón (salida del Kalman, ya
    en coordenadas de cancha), generar la posición objetivo (X, Y, Z) que
    debe alcanzar la SpiderCam en cada instante. Aquí se aplica la
    saturación al volumen de trabajo definido por los anclajes.
"""


class ReferenceGenerator:
    def __init__(self, workspace_bounds):
        self.workspace_bounds = workspace_bounds

    def generate(self, ball_position_field) -> tuple[float, float, float]:
        """Devuelve la posición de referencia (X, Y, Z) para la SpiderCam."""
        raise NotImplementedError

    def _clip_to_workspace(self, position):
        """Satura la posición al volumen de trabajo físico del rig."""
        raise NotImplementedError
