import doctest

import pytest


def test():
    pytest.main()


def run_doctest():
    doctest.testfile("../README.md", raise_on_error=True)
    doctest.testfile("../../examples.md", raise_on_error=True)
