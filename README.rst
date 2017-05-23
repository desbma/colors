
| |travisci| |version| |versions| |impls| |wheel| |coverage|

.. |travisci| image:: https://api.travis-ci.org/jonathaneunice/colors.svg
    :target: http://travis-ci.org/jonathaneunice/colors

.. |version| image:: http://img.shields.io/pypi/v/ansicolors.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ansicolors

.. |versions| image:: https://img.shields.io/pypi/pyversions/ansicolors.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ansicolors

.. |impls| image:: https://img.shields.io/pypi/implementation/ansicolors.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ansicolors

.. |wheel| image:: https://img.shields.io/pypi/wheel/ansicolors.svg
    :alt: Wheel packaging support
    :target: https://pypi.python.org/pypi/ansicolors

.. |coverage| image:: https://img.shields.io/badge/test_coverage-100%25-6600CC.svg
    :alt: Test line coverage
    :target: https://pypi.python.org/pypi/ansicolors


ANSI colors for Python
======================

Add ANSI colors and decorations to your strings.

Example Usage
-------------

::

    from __future__ import print_function  # accomodate Python 2
    from colors import *

    print(color('my string', fg='blue'))
    print(color('some text', fg='red', bg='yellow', style='underline'))

The strings returned by ``color`` will have embedded
`ANSI code sequences <https://en.wikipedia.org/wiki/ANSI_escape_code>`_
stipulating text colors and styles. For example, the above
code will print the strings::

    '\x1b[34mmy string\x1b[0m'
    '\x1b[31;43;4msome text\x1b[0m'

You can choose the foreground (text) color with the ``fg`` parameter,
the background color with ``bg``, and the style with ``style``.

You can choose one of the 8 basic ANSI colors: ``black``, ``red``, ``green``,
``yellow``, ``blue``, ``magenta``, ``cyan``, and ``white``, plus a special
``default`` which is display-specific, but usually a rational "no special
color" setting.

There are other ways to specify colors. Many devies supprt
an idiosyncratic 256-color scheme developed as an ANSI extension
in conjunction with the
`xterm terminal emulator <https://en.wikipedia.org/wiki/Xterm>`_.
Colors (or grays) from this larger palette can be specified via ``int``
value.

To see them all::

    from __future__ import print_function
    from colors import color

    for i in range(256):
        print(color('Color #%d' % i, fg=i))


The included ``show_colors.py`` program is a much-expanded version of this idea
that can be used to explore available color and style combinations on your
terminal or output device.

Modern terminals go even further than the ``xterm`` 256, often supporting a
full 24-bit RGB color scheme. You can provide a full RGB value several ways:

* with a 3-element ``tuple`` or ``list`` of ``int``, each valued 0 to 255 (e.g. ``(255, 218, 185)``),
* a string containing a CSS-compatible color name (e.g. ``'peachpuff'``),
* a string containing a CSS-style hex value (e.g. ``'#aaa'`` or ``'#8a2be2'``)
* a string containing a CSS-style RGB notation (e.g. ``rgb(102,51,153)``)

These forms can be mixed and matched at will::

    print(color('orange on gray', 'orange', 'gray'))
    print(color('nice color', 'white', '#8a2be2'))

Note that any color name defined in the basic ANSI color set takes
primacy over the CSS color names. Combined with the fact that
terminals do not always agree which precise tone of blue should
qualify as ANSI ``blue``, there can be some ambiguity regarding
the named colors. If you need full precision, specify the RGB
color exactly. The ``parse_rgb`` function can be used to identify
the correct definition according to the CSS standards.

Caveats
-------

Unfortunately there is no guarantee that every terminal or console will support
all the colors and styles that ANSI ostensibly defines. In fact, most do not.
Most output systems implement a subset. Colors are often better supported than
styles, for which you *might* get one or two of the most popular styles such as
``bold`` or ``underline``.

Whatever colors and styles are supported, there is no guarantee they will be
accurately rendered. Even at this late date, over **fifty years** after the codes
began to be standardized, support from terminals and output devices is limited,
fragemented, and piecemeal.

ANSI codes evolved in an entirely different historical context from today's.
Both the Web and the idea of broad standardization were decades in the future.
Display technology was low-resolution, colors were limited even when present,
and color/style fidelity was not a major consideration. Vendors thought little
or nothing of creating their own proprietary codes, implementing functions
differently from other vendors, and/or co-opting codes previously in use for
something else. Practical ANSI reference materials tend to include many phrases
such as 'hardly ever supported' and 'non-standard.'

We still use ANSI codes not because they're especially good, but because they're
the best, most standard approach pre-Web display systems even remotely agreed
upon. And even in this post-Web era, output of text to consoles and terminal
windows endures as an important means of computer-human interaction. The good
news, such is it is: The color and style specifications ("SGR" or "Select
Graphic Rendition" in ANSI terminology) are the most-used and best-adhered-to
portion of the whole ANSI show.

More Examples
-------------

::

    # use some partial functions

    from __future__ import print_function # so works on Python 2 and 3 alike
    from colors import red, green, blue

    print(red('This is red'))
    print(green('This is green'))
    print(blue('This is blue'))

Optionally you can add a background color and/or styles.::

    print(red('red on blue', bg='blue'))
    print(green('green on black', bg='black', style='underline'))

You can additionally specify one of the supported styles: ``none``, ``bold``,
``faint``, ``italic``,
``underline``, ``blink``, ``blink2``, ``negative``, ``concealed``, ``crossed``.
While most devices support only a few styles, unsupported styles
are generally ignored, so the only harm done is your text is less
pretty and/or less formatted than you might like.

You can use multiple styles at once. Separate them with
a ``+``.::

    print(red('very important', style='bold+underline'))

If you use this style often, you may want to create your own
named style::

    from functools import partial
    from colors import color

    important = partial(colors, fg='red', style='bold+underline'))

    print(important('very important'))

Utility Functions
-----------------

In deailing with ANSI-styled text, it can be necessary or convenient to
determine the "equivalent" text minus the styling. The function
``strip_color(s)`` does that, removing ANSI codes from ``s``, returning its
"plain text equivalent."

You may also wish to determine the effective length of a string. If it contains
ANSI color and styling codes, the builtin ``len()`` function will return the
length of those codes as well, which is probably not what you want. So
``ansilen`` returns the "effective" length of the string, including only the
non-ANSI characters. ``ansilen(s)`` is equivalent to ``len(strip_color(s))``,

License
-------

``colors`` is licensed under the `ISC license <https://en.wikipedia.org/wiki/ISC_license>`_.
