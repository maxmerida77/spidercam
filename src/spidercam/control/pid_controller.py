"""
Controlador PID para el seguimiento de referencias (OE-06, RF-06).

Responsabilidad:
    Dada la posición actual de la SpiderCam y la referencia generada,
    calcular la señal de control (velocidad o posición corregida) para
    que la SpiderCam siga la referencia de forma estable.

Usa python-control como base en lugar de un PID artesanal.
"""


class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        # TODO: estado interno (integral acumulada, error anterior)

    def step(self, setpoint, current_value, dt: float):
        """Calcula la señal de control para un paso de tiempo dt."""
        raise NotImplementedError
