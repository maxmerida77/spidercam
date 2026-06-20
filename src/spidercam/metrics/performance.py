"""
Métricas básicas de desempeño (RNF-05, criterios de éxito).

Responsabilidad:
    Calcular métricas como: % de frames con balón dentro del encuadre,
    error medio de seguimiento, reducción de ruido del Kalman vs.
    medición cruda. Exportar a CSV (ver config.yaml -> metrics.export_path).
"""


class PerformanceTracker:
    def __init__(self):
        self.records = []

    def log_frame(self, frame_idx, ball_position, spidercam_position, in_frame: bool):
        raise NotImplementedError

    def summary(self) -> dict:
        """Devuelve un resumen agregado de las métricas."""
        raise NotImplementedError

    def export_csv(self, path: str):
        raise NotImplementedError
