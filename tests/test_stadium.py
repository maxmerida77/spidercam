"""Pruebas del modelo de estadio."""
from spidercam.simulation.stadium import Stadium


def test_from_config_builds_stadium():
    config = {
        "stadium": {
            "field_length_m": 105,
            "field_width_m": 68,
            "anchor_points": [[0, 0, 25], [105, 0, 25], [105, 68, 25], [0, 68, 25]],
        }
    }
    stadium = Stadium.from_config(config)
    assert stadium.field_length_m == 105
    assert stadium.field_width_m == 68
    assert len(stadium.anchor_points) == 4
    assert stadium.anchor_points[0] == (0, 0, 25)


def test_workspace_bounds_derived_from_anchors():
    stadium = Stadium(
        field_length_m=105,
        field_width_m=68,
        anchor_points=[(0, 0, 25), (105, 0, 25), (105, 68, 25), (0, 68, 25)],
    )
    x_min, x_max, y_min, y_max, z_min, z_max = stadium.workspace_bounds
    assert (x_min, x_max) == (0, 105)
    assert (y_min, y_max) == (0, 68)
    assert z_min == 0.0
    assert z_max == 25
