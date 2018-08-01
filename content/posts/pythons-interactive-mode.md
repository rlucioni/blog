---
title: "Python's Interactive Mode"
date: 2016-12-14T21:48:45-04:00
---

You can drop into Python's interactive mode immediately after executing a script. Say you have the following script, `foo.py`.

```py
message = 'Hello, World!'

def greet():
    print(message)

greet()
```

To execute `foo.py` then immediately enter interactive mode, use the Python interpreter's [`-i` option](https://docs.python.org/3/using/cmdline.html#cmdoption-i).

```py
$ python -i foo.py
Hello, World!
>>> greet()
Hello, World!
```

This is a nice way to avoid repeatedly typing the same commands when developing a script or experimenting with something new. You can achieve a similar effect by setting a [breakpoint](https://docs.python.org/3/library/pdb.html#pdb.set_trace) in your script, though I prefer the `-i` option when I don't want to end up in the debugger.