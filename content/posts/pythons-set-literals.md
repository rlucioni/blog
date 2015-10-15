Title: Python's Set Literals
Description: Elucidating the benefits of Python's set literals.
Slug: pythons-set-literals
Date: 2015-10-14 23:47
Modified: 2015-10-14 23:47
Author: Renzo Lucioni
Tags: python, set, performance

You have two options when it comes to creating a set in Python. It's common to pass an iterable to `set()`. You can also use Python's syntax for set literals, `{}`. Although both approaches will return your set, a set literal executes twice as quickly as `set()`. For reference, I'm running CPython 3.5.0.

    :::python
    >>> import timeit
    >>> import dis
    >>>
    >>> def f():
    ...     return set([1, 2, 3])
    ... 
    >>> def g():
    ...     return {1, 2, 3}
    ... 
    >>> min(timeit.repeat(f))
    0.4566022079670802
    >>> min(timeit.repeat(g))
    0.21465317299589515

To understand this disparity, take a look at the disassembled bytecode for the two functions defined above, `f()` and `g()`.

    :::
    >>> dis.dis(f)
      2           0 LOAD_GLOBAL              0 (set)
                  3 LOAD_CONST               1 (1)
                  6 LOAD_CONST               2 (2)
                  9 LOAD_CONST               3 (3)
                 12 BUILD_LIST               3
                 15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                 18 RETURN_VALUE
    >>> dis.dis(g)
      2           0 LOAD_CONST               1 (1)
                  3 LOAD_CONST               2 (2)
                  6 LOAD_CONST               3 (3)
                  9 BUILD_SET                3
                 12 RETURN_VALUE

To create your set, `f()` needs to load the global named `set`, push three constants onto the stack, build a list consuming the three constants from the stack, then call the loaded `set()` function. On the other hand, `g()` only needs to push the three constants onto the stack before consuming them to build your set.

Not only are set literals pretty, they don't waste time building a list and calling a function. The next time you need to create a set, try using the literal syntax.
