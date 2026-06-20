"""
Cinemática inversa del rig de cables de la SpiderCam (OE-02).

Responsabilidad:
    Dado un conjunto de puntos de anclaje fijos (4 esquinas del estadio) y
    la posición (X, Y, Z) del carro/cámara, calcular la longitud de cada
    cable. Se usa SOLO para visualización (dibujar los cables), no forma
    parte del lazo de control (que opera en espacio cartesiano).

No incluye: cinemática directa, tensión de cables, catenaria/pandeo.
"""
import numpy as np


def cable_lengths(anchor_points, platform_position) -> list[float]:
    """Distancia euclidiana de cada anclaje a la posición del carro."""
    p = np.array(platform_position)
    return [float(np.linalg.norm(np.array(a) - p)) for a in anchor_points]
