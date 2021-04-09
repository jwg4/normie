from normie import cdf


def test_single_cdf_value():
    assert 0.97495 < cdf(0.96) < 0.97505
