from normie import cdf, invcdf, pdf


def test_cdf_at_infinity():
    assert cdf(float("inf")) == 1.0

