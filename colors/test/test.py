# -*- encoding: utf-8 -*-

"""
Tests for colors module
"""

from __future__ import absolute_import
from colors import color, strip_color
from pytest import raises


def test_nocolors():
    """We should have the original text with no parameters"""
    assert color("RED") == "RED"


def test_redcolor():
    """Test if we get a correct red"""
    assert color("RED", fg="red") == '\x1b[31mRED\x1b[0m'


def test_error_on_bad_color_string():
    """Test if we have an exception with a bad string color"""
    with raises(ValueError):
        color("RED", "bozo")


def test_integer_color():
    """Test if we can use a integer as a color"""
    assert color("RED", 1) == '\x1b[38;5;1mRED\x1b[0m'


def test_error_on_bad_color_int():
    """Test if we have an exception with a bad color number"""
    with raises(ValueError):
        color("RED", 911)


def test_background_color():
    """Test the background color with string"""
    assert color("RED", bg="red") == '\x1b[41mRED\x1b[0m'


def test_style_color():
    """Test the style with a string"""
    assert color('BOLD', style='bold') == '\x1b[1mBOLD\x1b[0m'


def test_error_setting_style_color():
    """Test if we have an exception setting the style"""
    with raises(ValueError):
        color("BOLD", style="MAY")


def test_error_on_bad_color_notint():
    """Test if we have an exception with a bad color number"""
    with raises(ValueError):
        color("RED", 911.11)


def test_error_on_bad_style():
    """Test if we have an exception with a bad color number"""
    with raises(ValueError):
        color("RED", bg="cursivas")


def test_remove_color():
    """We can get the original message without the colors"""
    assert strip_color(color("RED", "red")) == "RED"
