from normie.compat.excel import NORM_INV


def test_basic_value():
    assert 80.775 < NORM_INV(.1, 100, 15) < 80.785


def test_another_value():
    assert 134.895 < NORM_INV(.99, 100, 15) < 134.905


def test_basic_dist():
    assert 0.8405 < NORM_DIST(5, 3, 2, True) < 0.8415
