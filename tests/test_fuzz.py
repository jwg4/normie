from normie import cdf, invcdf, pdf

from hypothesis import given
from hypothesis.strategies import floats


# SMALLEST NUMBER SUCH THAT CDF IS POSITIVE FLOAT 
CDF_MIN = -8.0

# BIGGEST NUMBER WITH CDF DISTINGUISHABLE FROM 1
CDF_MAX = 8.0


@given(floats(allow_nan=True, allow_infinity=True))
def test_cdf_is_valid(x):
    result = cdf(x)
    assert result is not None


@given(floats(allow_nan=True, allow_infinity=True))
def test_pdf_is_valid(x):
    result = pdf(x)
    assert result is not None


@given(floats(CDF_MIN, CDF_MAX))
def test_cdf_works(x):
    result = cdf(x)
    assert result is not None
    assert result > 0.0
    assert result < 1.0


@given(floats(allow_nan=False, allow_infinity=True))
def test_pdf_works(x):
    result = pdf(x)
    assert result is not None
    assert result >= 0.0


@given(floats(0.0, 1.0))
def test_invcdf_works(x):
    result = invcdf(x)
    assert result is not None



