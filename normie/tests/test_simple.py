from normie import cdf, invcdf, pdf


def test_single_cdf_value():
    # From NCST
    assert 0.97495 < cdf(1.96) < 0.97505


def test_another_single_cdf_value():
    # From NCST
    assert 0.75485 < cdf(0.69) < 0.75495


def test_a_basic_cdf_value():
    assert cdf(0.0) == 0.5


def test_single_pdf_value():
    # From manual calculation
    assert 0.39885 < pdf(0) < 0.39895
    assert 0.39885 < pdf(0.0) < 0.39895


def test_exact_pdf_value():
    assert pdf(0.0) == 0.3989422917366028


def test_another_single_pdf_value():
    # From Wolfram Alpha
    # TODO: find accurate value for pdf(1)
    assert 0.2419705 < pdf(1) < 0.2419715
    assert 0.2419705 < pdf(1.0) < 0.2419715


def test_single_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert 1.64485 < invcdf(0.95) < 1.64495


def test_high_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert 2.05365 < invcdf(0.98) < 2.05375


def test_low_invcdf_value():
    """ Bounds from New Cambridge Statistical Tables, 2nd Ed.
        (4dp of precision given in Table 5)
    """
    assert -2.05375 < invcdf(0.02) < -2.05365


def test_a_basic_invcdf_value():
    assert invcdf(0.5) == 0.0


def test_a_medium_invcdf_value():
    # From Wichura 1988
    assert invcdf(0.25) == -0.674_489_750_196_081_7
    

def test_a_small_invcdf_value():
    # From Wichura 1988
    assert invcdf(0.001) == -3.090_232_306_167_814
    

def test_a_very_small_invcdf_value():
    # From Wichura 1988
    assert invcdf(1E-20) == -9.263_340_089_798_408

