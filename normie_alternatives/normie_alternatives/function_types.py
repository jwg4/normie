class FunctionTypes:
    # sends min value to -1, 0 to 0, and max value to 1
    ERF_FUNCTION = "erf_function"
    # sends min value to 0, 0 to 1/2 and max value to 1
    CDF_FUNCTION = "cdf_function"

    # sends -1 to min value, 0 to 0, and 1 to max value
    INV_ERF_FUNCTION = "inv_erf_function"
    # sends 0 to min value, 1/2 to 0 and 1 to max value
    INV_CDF_FUNCTION = "inv_cdf_function"


def erf_function(fn):
    fn.function_type = FunctionTypes.ERF_FUNCTION
    return fn


def cdf_function(fn):
    fn.function_type = FunctionTypes.CDF_FUNCTION
    return fn


def inv_erf_function(fn):
    fn.function_type = FunctionTypes.INV_ERF_FUNCTION
    return fn


def inv_cdf_function(fn):
    fn.function_type = FunctionTypes.INV_CDF_FUNCTION
    return fn
