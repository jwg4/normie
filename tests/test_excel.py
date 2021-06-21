from normie.compat.excel import NORMINV


def test_basic_value():
    assert 80.775 < NORMINV(.1, 100, 15) < 80.785


def test_another_value():
    assert 134.895 < NORMINV(.99, 100, 15) < 134.905
