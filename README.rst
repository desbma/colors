ANSI colors for Python
======================

le module to add ANSI colors and decorations to your strings.

Example Usage
-------------

You can choose one of the 8 basic ANSI colors: ``black``, ``red``, ``green``,
``yellow``, ``blue``,
``magenta``, ``cyan``, and ``white``.

Each color also has a 'bright' partner: ``brightblack``, ``brightred``,
ghtgreen``, ``brightyellow``, ``brightblue``, ``brightmagenta``,
``brightcyan``, and ``brightwhite``. (Instead of 'bright', these additional 8
colors are sometimes referred to as 'light', 'high', or 'intense' 
variants.) On many terminals, such 'bright' variants are needed to get the
color you expect, especially for naturally bright colors.
``brightyellow`` is often a much better yellow than ``yellow``, and
``brightwhite`` is much whiter than ``white``.

::

    from colors import red, green, blue, brightgreen
    print red('This is red')
    print green('This is green')
    print brightgreeen('This is brightgreen')
    print blue('This is blue')

Optionally you can specify a background color.

::

    print red('red on blue', bg='blue')
    print green('green on black', bg='black')

You can additionally specify one of the supported styles: none, bold, faint, italic,
underline, blink, blink2, negative, concealed, crossed. Not all styles are
supported by all terminals.

::

    from colors import bold, underline
    print bold('This is bold')
    print underline('underline red on blue', fg='red', bg='blue')
    print green('bold green on black', bg='black', style='bold')

You can also use more than one styles at once.

::

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
