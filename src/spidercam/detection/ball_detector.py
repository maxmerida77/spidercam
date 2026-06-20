"""
Detección del balón mediante YOLOv8 (modelo preentrenado).

Responsabilidad (OE-03, RF-02, RF-03):
    Dado un frame de video, devolver la posición en píxeles (u, v) del
    balón detectado (y opcionalmente su bounding box / confianza).

No incluye: entrenamiento de modelo, detección de jugadores.
"""
from dataclasses import dataclass


@dataclass
class Detection:
    u: float
    v: float
    confidence: float


class BallDetector:
    def __init__(self, model_path: str, confidence_threshold: float = 0.25):
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        # TODO: cargar modelo YOLOv8 (ultralytics.YOLO)

    def detect(self, frame) -> "Detection | None":
        """Devuelve la detección del balón en el frame, o None si no se detecta."""
        raise NotImplementedError
