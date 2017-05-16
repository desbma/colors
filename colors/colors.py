# Copyright (c) 2012 Giorgos Verigakis <verigak@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from __future__ import absolute_import, print_function
import re
import sys
from .csscolors import css_colors

_PY3 = sys.version_info[0] > 2
string_types = str if _PY3 else basestring

from functools import partial

# Stock ANSI color names, extended with "bright" variants which
# are often required for good look on terminals.
COLORS = ('black', 'red', 'green', 'yellow', 'blue',
          'magenta', 'cyan', 'white',
          'brightblack', 'brightred', 'brightgreen', 'brightyellow', 'brightblue',
          'brightmagenta', 'brightcyan', 'brightwhite')

# ANSI style names
STYLES = ('none', 'bold', 'faint', 'italic', 'underline', 'blink',
          'blink2', 'negative', 'concealed', 'crossed')


def is_string(obj):
    """
    Is the given object a string?
    """
    return isinstance(obj, string_types)


def _color_code(spec, base):
    """
    Workhorse of encoding a color. Give preference to named colors from
    ANSI set, then to specific numeric or tuple specs. Finally, look up
    in CSS colors.

    Base is a numeric value, either 30 or 40, signifying the base value
    for color encoding. Low values are added directly to the base. Higher
    values use base + 8 (i.e. 38 or 48) then extended codes.
    """
    if is_string(spec):
        spec = spec.lower()
    if spec in COLORS:
        index = COLORS.index(spec)
        if index < 8:
            return '{}'.format(base + index)
        else:
            return '{};5;{}'.format(base + 8, index)
    elif isinstance(spec, int) and 0 <= spec <= 255:
        return '{};5;{}'.format(base + 8, spec)
    elif isinstance(spec, (tuple, list)):
        rgbpart = ';'.join(x for x in spec)
        return '{};2;{}'.format(base + 8, rgbpart)
    elif spec in css_colors:
        rgb = css_colors[spec]
        rgbpart = ';'.join(x for x in rgb)
        return '{};2;{}'.format(base + 8, rgbpart)
    else:
        raise ValueError('Invalid color "%s"' % spec)


def color(s, fg=None, bg=None, style=None):
    """
    Add ANSI colors and styles to a string.
    :param str s: String to format.
    :param str|int|tuple fg: Foreground color specification.
    :param str|int|tuple bg: Background color specification.
    :param str: Style names, separated by '+'
    :returns: Formatted string.
    :rtype: str (or unicode in Python 2)
    """
    codes = []

    if fg:
        codes.append(_color_code(fg, 30))
    if bg:
        codes.append(_color_code(bg, 40))
    if style:
        for style_part in style.split('+'):
            if style_part in STYLES:
                codes.append(str(STYLES.index(style_part)))
            else:
                raise ValueError('Invalid style "%s"' % style_part)

    if codes:
        prefix = '\x1b[{0}m'.format(';'.join(codes))
        suffix = '\x1b[0m'
        return prefix + s + suffix
    else:
        return s


def strip_color(s):
    """
    Remove ANSI sequences from a string.
    """
    return re.sub('\x1b\[.+?m', '', s)


# Foreground shortcuts
black = partial(color, fg='black')
red = partial(color, fg='red')
green = partial(color, fg='green')
yellow = partial(color, fg='yellow')
blue = partial(color, fg='blue')
magenta = partial(color, fg='magenta')
cyan = partial(color, fg='cyan')
white = partial(color, fg='white')

# Style shortcuts
bold = partial(color, style='bold')
none = partial(color, style='none')
faint = partial(color, style='faint')
italic = partial(color, style='italic')
underline = partial(color, style='underline')
blink = partial(color, style='blink')
blink2 = partial(color, style='blink2')
negative = partial(color, style='negative')
concealed = partial(color, style='concealed')
crossed = partial(color, style='crossed')
