from tests.constants import TEST_ERF_MAX, TEST_ERF_MIN

from hypothesis.strategies import floats


erf_floats = floats(min_value=TEST_ERF_MIN, max_value=TEST_ERF_MAX, allow_infinity=False, allow_nan=False)
pos_erf_floats = floats(min_value=0.0, max_value=TEST_ERF_MAX, allow_infinity=False, allow_nan=False)
finite_floats = floats(allow_infinity=False, allow_nan=False)