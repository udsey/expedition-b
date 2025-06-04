"""Tests for main.py using pytest."""

from code.main import add

def test_even():
    """Test for even numbers."""
    assert add(2, 6) == 8

def test_odd():
    """Test for odd numbers."""
    assert add(1, 3) == 4
