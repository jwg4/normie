from normie import cdf


def test_single_cdf_value():
    assert 0.9745 < cdf(0.96) < 0.9755


def test_single_value_from_excel():
    assert 0.9745 < cdf(0.96) < 0.9755
    assert not "Use correct values for this test."
