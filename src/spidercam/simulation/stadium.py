"""
Modelo del estadio simplificado (OE-01).

Responsabilidad:
    Representar la geometría básica del estadio (dimensiones de la cancha,
    posición de los 4 anclajes del rig) a partir de config.yaml.
"""
from dataclasses import dataclass


@dataclass
class Stadium:
    field_length_m: float
    field_width_m: float
    anchor_points: list  # 4 puntos (x, y, z)
