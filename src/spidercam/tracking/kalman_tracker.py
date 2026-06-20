"""
Filtro de Kalman para estimación de trayectoria del balón (OE-04, RF-04).

Responsabilidad:
    Suavizar las detecciones ruidosas del balón y predecir su posición en
    frames donde la detección falla (oclusión, balón fuera de cuadro, etc).

Usa FilterPy como base en lugar de implementar Kalman desde cero.
"""


class KalmanTracker:
    def __init__(self, process_noise: float, measurement_noise: float):
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        # TODO: inicializar filterpy.kalman.KalmanFilter (estado: posición + velocidad)

    def predict(self):
        """Paso de predicción (sin nueva medición)."""
        raise NotImplementedError

    def update(self, measurement):
        """Paso de corrección con una nueva detección (u, v)."""
        raise NotImplementedError
