from normie import cdf, invcdf


def NORM_INV(p, m, sd):
    return invcdf(p) * sd + m


def NORM_DIST(z, m, sd, _):
    return cdf((z - m) / sd)
