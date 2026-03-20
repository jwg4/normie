from hypothesis import given
import pytest

from normie_alternatives.abram_steg.erf import erf_approx_7_1_25, erf_approx_7_1_26, erf_approx_7_1_27, erf_approx_7_1_28
from normie_alternatives.wichura.erf import PPND7, PPND7_inv_erf
from tests.constants import ERF_IS_64_BIT_MINUS_ONE, ERF_IS_64_BIT_ONE
from tests.custom_strategies import pos_erf_floats, inv_erf_floats, inv_cdf_floats


ERF_FUNCTIONS = [
    erf_approx_7_1_25,
    erf_approx_7_1_26,
    erf_approx_7_1_27,
    erf_approx_7_1_28
]

@given(x=pos_erf_floats)
@pytest.mark.parametrize(
    "erf_function",
    ERF_FUNCTIONS
)
def test_valid_erf(erf_function, x):
    result = erf_function(x)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


INV_ERF_FUNCTIONS = [
    PPND7_inv_erf
]

@given(x=inv_erf_floats)
@pytest.mark.parametrize("inv_erf_function", INV_ERF_FUNCTIONS)
def test_valid_inv_erf(inv_erf_function, x):
    result = inv_erf_function(x)
    assert isinstance(result, float)
    assert ERF_IS_64_BIT_MINUS_ONE <= result <= ERF_IS_64_BIT_ONE


INV_CDF_FUNCTIONS = [
    PPND7
]

@given(x=inv_cdf_floats)
@pytest.mark.parametrize("inv_cdf_function", INV_CDF_FUNCTIONS)
def test_valid_inv_cdf(inv_cdf_function, x):
    result = inv_cdf_function(x)
    assert isinstance(result, float)
    assert ERF_IS_64_BIT_MINUS_ONE <= result <= ERF_IS_64_BIT_ONE
