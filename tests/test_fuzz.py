from normie import cdf, invcdf, pdf

from hypothesis import given
from hypothesis.strategies import floats


# SMALLEST NUMBER SUCH THAT CDF IS POSITIVE FLOAT 
CDF_MIN = -8.0

# BIGGEST NUMBER WITH CDF DISTINGUISHABLE FROM 1
CDF_MAX = 8.0


@given(floats(CDF_MIN, CDF_MAX))
def test_cdf_works(x):
    result = cdf(x)
    assert result is not None
    assert result > 0.0
    assert result < 1.0
