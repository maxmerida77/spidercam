"""Pruebas de la cinemática inversa de cables."""


def test_cable_lengths_known_geometry():
    from spidercam.geometry.cable_kinematics import cable_lengths

    anchors = [[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]]
    position = [5, 5, 0]
    lengths = cable_lengths(anchors, position)
    assert len(lengths) == 4
    assert all(l > 0 for l in lengths)
