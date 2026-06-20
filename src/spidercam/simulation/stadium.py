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

    @classmethod
    def from_config(cls, config: dict) -> "Stadium":
        """Construye el estadio a partir del dict cargado de config.yaml."""
        stadium_cfg = config["stadium"]
        return cls(
            field_length_m=stadium_cfg["field_length_m"],
            field_width_m=stadium_cfg["field_width_m"],
            anchor_points=[tuple(p) for p in stadium_cfg["anchor_points"]],
        )

    @property
    def workspace_bounds(self):
        """Caja (x_min, x_max, y_min, y_max, z_min, z_max) físicamente
        alcanzable por el carro, derivada de los 4 anclajes. El carro no
        puede subir más alto que los anclajes ni bajar del piso (z=0).

        No incluye el margen de seguridad adicional (config:
        spidercam.workspace_margin_m); ese se aplica en
        control/reference_generator.py sobre las referencias, antes de
        que lleguen aquí.
        """
        xs = [p[0] for p in self.anchor_points]
        ys = [p[1] for p in self.anchor_points]
        zs = [p[2] for p in self.anchor_points]
        return (min(xs), max(xs), min(ys), max(ys), 0.0, min(zs))
