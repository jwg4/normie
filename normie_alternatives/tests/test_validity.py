from hypothesis import given
import pytest

from normie_alternatives.abram_steg.erf import erf_approx_7_1_25, erf_approx_7_1_26, erf_approx_7_1_27, erf_approx_7_1_28
from tests.custom_strategies import pos_erf_floats


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
    assert -1.0 <= result <= 1.0
