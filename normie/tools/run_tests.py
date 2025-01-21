import doctest

import pytest


def test():
    pytest.main()


def run_doctest():
    doctest.testfile("../README.md", optionflags=doctest.ELLIPSIS, raise_on_error=True)
    doctest.testfile("../../examples.md", optionflags=doctest.ELLIPSIS, raise_on_error=True)
