"""
Mapeo de coordenadas de imagen (píxeles) a coordenadas de cancha (metros).

Responsabilidad (ver docs/architecture.md, sección "Mapeo 2D -> 3D"):
    Calcular una homografía una sola vez por video (cv2.findHomography) a
    partir de puntos de calibración, y aplicarla a cada detección del
    balón para obtener su posición real (X, Y) sobre el plano de la
    cancha. Asume cámara fija y balón sobre el plano del piso.
"""


class FieldHomography:
    def __init__(self, image_points, field_points):
        self.image_points = image_points
        self.field_points = field_points
        # TODO: self.H = cv2.findHomography(image_points, field_points)

    def image_to_field(self, u: float, v: float) -> tuple[float, float]:
        """Convierte un punto en píxeles (u, v) a coordenadas de cancha (X, Y) en metros."""
        raise NotImplementedError
