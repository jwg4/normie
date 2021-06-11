from normie import cdf, invcdf


def test_single_cdf_value():
    assert 0.97495 < cdf(1.96) < 0.97505


def test_another_single_cdf_value():
    assert 0.75485 < cdf(0.69) < 0.75495


def test_single_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert 1.64485 < invcdf(0.95) < 1.64495


def test_high_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert 2.05365 < invcdf(0.98) < 2.05375


def test_low_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert -2.05375 < invcdf(0.02) < -2.05365
