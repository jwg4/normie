from normie import cdf, invcdf


def test_single_cdf_value():
    assert 0.97495 < cdf(1.96) < 0.97505


def test_another_single_cdf_value():
    assert 0.75485 < cdf(0.69) < 0.75495


def test_single_invcdf_value():
    assert 1.64485 < invcdf(0.95) < 1.64495


def test_high_invcdf_value():
    assert 2.0 < invcdf(0.98) < 3.0
