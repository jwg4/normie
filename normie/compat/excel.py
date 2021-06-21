from normie import invcdf


def NORMINV(p, m, sd):
    return invcdf(p) * sd + m
