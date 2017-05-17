ANSI colors for Python
======================

Add ANSI colors and decorations to your strings.

Example Usage
-------------

::

    from __future__ import print_function  # accomodate Python 2
    from colors import *

    print(color('my string', fg='blue'))

    print(color('bold', fg='red', bg='yellow', style='underline'))


You can choose the foreground (text) color with the ``fg`` parameter,
the background color with ``bg``, and the style with ``style``.

You can choose one of the 8 basic ANSI colors: ``black``, ``red``, ``green``,
``yellow``, ``blue``, ``magenta``, ``cyan``, and ``white``, plus a special
``default`` which is display-specific, but usually a rational "no special
color" setting.

But you can also choose other color specifications. The
`ANSI code sequences <https://en.wikipedia.org/wiki/ANSI_escape_code>`_
define an idiosyncratic 256-color scheme associated with the
`xterm terminal emulator <https://en.wikipedia.org/wiki/Xterm>`_.
The above basic colors comprise
just the first 8. The remaining ones can be specified via ``int`` value.

To see them all::

    from __future__ import print_function
    from colors import color

    for i in range(256):
        print(color('Color #%d' % i, fg=i))


The included``show_colors.py`` program is a much-expanded
version of this that can be used
to explore available color and style combinations
on your terminal or output device.

Modern terminals go even further, often supporting a full 24-bit RGB color scheme.
You can provide a full RGB value several ways:

* with a 3-elment ``tuple`` or ``list`` of ``int`` each valued 0 to 255 (e.g. ``(255, 218, 185)``),
* a string containing a CSS-compatible color name (e.g. ``'peachpuff'``),
* a string containing a CSS-style hex value (e.g. ``'#aaa'`` or ``'#8a2be2'``)
* a string containing a CSS-style RGB notation (e.g. ``rgb(102,51,153)``)

These forms can be mixed and matched at will::

    print(color('orange on gray', 'orange', 'gray'))
    print(color('nice color', 'brightwhite', '#8a2be2'))

Caveats
-------

Unfortunately there is no guarantee that every terminal or
console will support all the colors and styles that ANSI
ostensibly defines. In fact, most output systems implement
a small subset such as colors and *maybe* one or two styles,
such as ``bold`` or ``underline``.

Whatever colors and styles are supported, there is no guarantee they will be
accurately rendered. Even at this late date, over fifty years after the codes
began to be standardized, support from terminals and out devices is limited,
fragemented, and piecemeal.

ANSI codes evolved in an entirely different historical context from today's.
Both the Web and the idea of broad standardization were decades in the future.
Display technology was low-resolution, colors were limited even when present,
and color/style fidelity was not a major consideration. Vendors thought little
or nothing of creating their own proprietary codes, and/or co-opting codes
previously in use for something else. Practical ANSI reference materials tend to
include many phrases such as 'hardly ever supported' and 'non-standard.'

We still use ANSI codes
because they're the best and most standard approach pre-Web display
systems even remotely agreed upon, not because they're great. And
even in this post-Web era, output of text to consoles and terminal windows
endures as an important means of computer-human interaction.
The good news, such is it is: The color specifications are the most-used
and best-adhered-to portion of the whole ANSI show.

More Examples
-------------

::

    from colors import red, green, blue
    print red('This is red')
    print green('This is green')
    print blue('This is blue')

Optionally you can specify a background color.

::

    print red('red on blue', bg='blue')
    print green('green on black', bg='black')

You can additionally specify one of the supported styles: ``none``, ``bold``,
``faint``, ``italic``,
``underline``, ``blink``, ``blink2``, ``negative``, ``concealed``, ``crossed``.
Not all styles are
supported by all terminals. (In fact, most styles are *not* supported.)

If you like, you can use multiple styles at once. Separate them with
a ``+``::

    print red('This is very important', style='bold+underline')

If you want a general-purpose styling function, that's available too.

::

    from colors import color

    print color('This', style='underline'), 'is', color('very red', fg='brightred')

xterm-256 colors are supported as well, to use them give an integer instead of
a color name.

::

    from colors import color
    for i in range(256):
        print color('Color #%d' % i, fg=i)

The included test program, ``test_colors.py``, can be run to see what colors
and styles work well on a given terminal.

License
-------

colors is licensed under the ISC license.
