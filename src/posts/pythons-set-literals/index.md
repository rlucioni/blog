---
title: Python's Set Literals
description: Using disassembled bytecode to compare the performance of different ways to create a set in Python.
date: 2015-10-14T21:52:21-04:00
lastmod: 2019-03-02T20:10:21-04:00
---

You have two options when it comes to creating a set in Python. It's common to pass an iterable to `set()`. You can also use Python's syntax for set literals, `{}`. Although both approaches will return your set, a set literal executes twice as quickly as `set()`. For reference, I'm running CPython 3.5.0.

```python
>>> import timeit
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
```

To understand this disparity, take a look at the disassembled bytecode for the two functions defined above, `f()` and `g()`.

```python
>>> import dis
>>>
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
```

To create your set, `f()` needs to load the global named `set`, push three constants onto the stack, build a list consuming the three constants from the stack, then call the loaded `set()` function. On the other hand, `g()` only needs to push the three constants onto the stack before consuming them to build your set.

Set construction from a tuple performs similarly to set construction from a list, although it is a little quicker.

```python
>>> def h():
...     return set((1, 2, 3))
...
>>> min(timeit.repeat(h))
0.40520797698991373
```

Taking a look at the disassembled bytecode for `h()` can also shed some light on its performance.

```python
>>> dis.dis(h)
  2           0 LOAD_GLOBAL              0 (set)
              3 LOAD_CONST               4 ((1, 2, 3))
              6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
              9 RETURN_VALUE
```

To create a set, `h()` also needs to load the global named `set`, but instead of pushing three constants onto the stack and using them to build a list, it only needs to push a single tuple constant onto the stack before calling `set()`.

It's worth noting that some cases which would have ruled out use of the set literal in older versions of Python no longer apply. If you need to construct a set from an iterator and you're using Python 3.5+, you can take advantage of its extended unpacking rules and use a set literal.

```python
>>> i = range(1, 4)
>>> {*i}
{1, 2, 3}
```

In older versions of Python, `set()` continues to be the right tool for the job.

Although the performance differences explored here are often inconsequential, set literals don't waste time building a intermediate data structure or calling a function, and they're pretty, too. If the literal syntax works for you, try using it the next time you need to create a set.
