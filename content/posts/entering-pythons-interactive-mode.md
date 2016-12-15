Title: Entering Python's Interactive Mode
Description: How to enter Python's interactive mode immediately after running a script.
Slug: entering-pythons-interactive-mode
Date: 2016-12-14 20:57
Modified: 2016-12-14 20:57
Author: Renzo Lucioni
Tags: python

Did you know you can drop into Python's interactive mode immediately after executing a script? Say you have the following script, `foo.py`.

    :::python
    message = 'Hello, World!'

To execute `foo.py` then immediately enter interactive mode, use the Python interpreter's [`-i` option](https://docs.python.org/3/using/cmdline.html#cmdoption-i).

    :::
    $ python -i foo.py
    >>> message
    'Hello, World!'

This is a nice way to avoid repeatedly typing the same commands when developing a script or experimenting with something new. You can achieve a similar effect by setting a [breakpoint](https://docs.python.org/3/library/pdb.html#pdb.set_trace) in your script, though I prefer the `-i` option when I don't want to end up in the debugger.
