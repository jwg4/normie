from normie import cdf, invcdf, pdf

from hypothesis import given
from hypothesis.strategies import floats


@given(floats())
def test_cdf_works(x):
    result = cdf(x)
    assert result is not None
    assert result > 0.0
    assert result < 1.0
