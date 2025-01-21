from normie import cdf

from pytest import mark

# These values come from a supplementary table to Table 4 in NCST,
# which shows the critical values where the last digit of the cdf changes
bounds = [
    (None, 3.075, 0.999),
    (0.999, 3.105, 0.9991),
    (0.9991, 3.138, 0.9992),
    (0.9992, 3.174, 0.9993),
    (0.9993, 3.215, 0.9994),
    (0.9994, 3.263, 0.9995),
    (0.9995, 3.32, 0.9996),
    (0.9996, 3.389, 0.9997),
    (0.9997, 3.48, 0.9998),
    (0.9998, 3.615, 0.9999),
    (0.9999, 3.731, 0.99991),
    (0.99991, 3.759, 0.99992),
    (0.99992, 3.791, 0.99993),
    (0.99993, 3.826, 0.99994),
    (0.99994, 3.867, 0.99995),
    (0.99995, 3.916, 0.99996),
    (0.99996, 3.976, 0.99997),
    (0.99997, 4.055, 0.99998),
    (0.99998, 4.173, 0.99999),
    (0.99999, 4.417, 1.0),
]


@mark.parametrize("lower, x, upper", bounds)
def test_tail_bounds(lower, x, upper):
        f_value = cdf(x) 
        if lower is not None:
            assert lower <= f_value, f"Assertion failed for input value {x}: f({x}) = {f_value}, not more than {lower}" 
        if upper is not None:
            assert f_value <= upper, f"Assertion failed for input value {x}: f({x}) = {f_value}, not less than {upper}" 
