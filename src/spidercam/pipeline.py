"""
Orquestador end-to-end del sistema (OE-07).

Conecta todos los módulos siguiendo la arquitectura definida en
docs/architecture.md: video -> detección -> tracking -> Kalman ->
referencias -> PID -> SpiderCam -> visualización -> métricas.

Se desarrolla en la Fase 8 (Integración completa), una vez que cada
módulo individual esté probado por separado.
"""


class Pipeline:
    def __init__(self, config: dict):
        self.config = config
        # TODO: instanciar BallDetector, KalmanTracker, FieldHomography,
        # ReferenceGenerator, PIDController, SpiderCamModel, Viewer3D,
        # PerformanceTracker a partir de self.config

    def run(self, video_path: str):
        raise NotImplementedError
