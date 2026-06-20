"""Pruebas del modelo cinemático de la SpiderCam (update, clipping, cables)."""
import numpy as np

from spidercam.simulation.stadium import Stadium
from spidercam.simulation.spidercam_model import SpiderCamModel


def _make_stadium():
    return Stadium(
        field_length_m=105,
        field_width_m=68,
        anchor_points=[(0, 0, 25), (105, 0, 25), (105, 68, 25), (0, 68, 25)],
    )


def test_update_integrates_position():
    model = SpiderCamModel(_make_stadium(), initial_position=[50, 30, 10], max_speed_m_s=5.0)
    model.update(velocity_command=[1.0, 0.0, 0.0], dt=1.0)
    assert np.allclose(model.position, [51, 30, 10])


def test_update_caps_velocity_at_max_speed():
    model = SpiderCamModel(_make_stadium(), initial_position=[50, 30, 10], max_speed_m_s=2.0)
    model.update(velocity_command=[10.0, 0.0, 0.0], dt=1.0)
    desplazamiento = np.linalg.norm(model.position - np.array([50, 30, 10]))
    assert np.isclose(desplazamiento, 2.0)


def test_update_clips_position_to_workspace():
    model = SpiderCamModel(_make_stadium(), initial_position=[50, 30, 10], max_speed_m_s=1000.0)
    model.update(velocity_command=[1000.0, 0.0, 0.0], dt=1.0)
    x_min, x_max, _, _, _, _ = model.stadium.workspace_bounds
    assert model.position[0] <= x_max


def test_get_cable_lengths_returns_four_positive_values():
    model = SpiderCamModel(_make_stadium(), initial_position=[50, 30, 10])
    lengths = model.get_cable_lengths()
    assert len(lengths) == 4
    assert all(l > 0 for l in lengths)
