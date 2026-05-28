"""Tests for basic string utility behaviour."""


def test_empty_string():
    """An empty string has length zero."""
    assert len("") == 0


def test_unicode_string():
    """Unicode round-trips through native string operations."""
    s = "héllo"
    assert s[0] == "h"
    assert s == "héllo"


def test_long_string():
    """Very long strings should preserve length."""
    s = "a" * 10000
    assert len(s) == 10000
    assert s[-1] == "a"
