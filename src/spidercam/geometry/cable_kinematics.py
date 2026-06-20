"""
Cinemática inversa del rig de cables de la SpiderCam (OE-02).

Responsabilidad:
    Dado un conjunto de puntos de anclaje fijos (4 esquinas del estadio),
    calcular la longitud de cada cable hacia una posición (X, Y, Z) del
    carro/cámara. Se usa SOLO para visualización (dibujar los cables), no
    forma parte del lazo de control (que opera en espacio cartesiano).

No incluye: cinemática directa, tensión de cables, catenaria/pandeo.
"""
import numpy as np

class CableKinematics:
    def __init__(self, anchors):
        """anchors: lista/array de 4x3 con las coordenadas (X, Y, Z) de los postes."""
        self.anchors = np.array(anchors)

    def calculate_lengths(self, camera_pos):
        """L_i = distancia euclidiana entre cada anclaje y la posición de la cámara."""
        camera_pos = np.array(camera_pos)
        diff = self.anchors - camera_pos
        return np.linalg.norm(diff, axis=1)