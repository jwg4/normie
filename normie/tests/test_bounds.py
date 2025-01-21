from normie import cdf, invcdf, pdf


def test_cdf_at_positive_infinity():
    assert cdf(float("inf")) == 1.0


def test_cdf_at_negative_infinity():
    assert cdf(float("-inf")) == 0.0


def test_invcdf_at_positive_infinity():
    assert invcdf(1.0) == float("inf")


def test_invcdf_at_negative_infinity():
    assert invcdf(0.0) == float("-inf")


def test_pdf_at_positive_infinity():
    assert pdf(float("inf")) == 0.0


def test_pdf_at_negative_infinity():
    assert pdf(float("-inf")) == 0.0

