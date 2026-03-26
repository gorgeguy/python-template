"""Smoke tests — confirm the project is wired up correctly."""

import mypackage


def test_should_have_version():
    assert mypackage.__version__
