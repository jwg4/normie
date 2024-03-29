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

