from normie import invcdf


def NORM_INV(p, m, sd):
    return invcdf(p) * sd + m
