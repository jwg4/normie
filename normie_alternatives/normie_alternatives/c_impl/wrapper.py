from normie_alternatives.function_types import inv_cdf_function
from normie_alternatives.transformations import inv_cdf_to_inv_erf

from normie_impl import acklam_invcdf as acklam_invcdf_impl

acklam_invcdf = inv_cdf_function(acklam_invcdf_impl)
acklam_inverf = inv_cdf_to_inv_erf(acklam_invcdf)
