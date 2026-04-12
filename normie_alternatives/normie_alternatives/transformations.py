from normie_alternatives.function_types import FunctionTypes, inv_erf_function


def inv_cdf_to_inv_erf(inv_cdf_fn):
    assert hasattr(inv_cdf_fn, "function_type") and inv_cdf_fn.function_type == FunctionTypes.INV_CDF_FUNCTION, "inv_cdf_fn must be a CDF function"

    def inv_erf_fn(x):
        return inv_cdf_fn((x + 1) / 2.0)
    
    return inv_erf_function(inv_erf_fn)
