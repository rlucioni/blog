---
title: Mocking UUID.hex
description: Mocking a property on an instance of a Python class when writing tests.
date: 2015-03-20T21:51:05-04:00
lastmod: 2019-03-02T20:10:21-04:00
---

Mocking is an indispensable tool when writing unit tests, allowing you to temporarily replace parts of your system under test with controlled, predictable mock objects. I recently struggled to mock [`UUID.hex`](https://docs.python.org/2/library/uuid.html#uuid.UUID.hex), a read-only attribute on instances of the UUID class. Ned Batchelder has written about [mocking `datetime.today()`](https://nedbatchelder.com/blog/201209/mocking_datetimetoday.html). This is a good resource if you're trying to mock out a method belonging to a class from a module imported by your code under test.

However, my goal was to mock out an object property, specifically a property (`hex`) on an instance of a class (`UUID`) belonging to a module (`uuid`) imported by my code under test. I ended up using the following code in my test class, where `target_module` represents the module being tested:

```python
def setUp(self):
    uuid_patcher = mock.patch.object(
        target_module.uuid.UUID,
        'hex',
        new_callable=mock.PropertyMock(return_value=self.UUID_HEX)
    )
    mocked_uuid = uuid_patcher.start()
    self.addCleanup(uuid_patcher.stop)
```

What's going on here? In a nutshell, [`patch.object()`](https://docs.python.org/3/library/unittest.mock.html#patch-object) is used to replace the `hex` property on instances of `target_module.uuid.UUID` with a [`PropertyMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock) which returns some fixed value, `self.UUID_HEX`. The rest of the `uuid` module's functionality remains intact.

I hit a couple of stumbling blocks while figuring out how to do this. The first was identifying the right target to patch. The module I was trying to test -- `target_module` -- imported `uuid`, requiring me to patch the `hex` attribute on instances of `target_module.uuid.UUID`. Patching the `hex` attribute on `uuid.UUID` only replaces `hex` with a mock object within the scope of the test module itself, not the module under test.

The second challenge for me was replacing `hex` with the right kind of `Mock` object, that being a `PropertyMock`. As you might have guessed, this subclass of `Mock` creates a mock object intended to be used as a property. Getting a `PropertyMock` instance from an object calls the mock with no arguments and returns whatever return value you've specified. The key to replacing `hex` with a `PropertyMock` is specifying `PropertyMock` as a new callable when invoking `patch.object()`. By default, `patch.object()` replaces its target attribute with an instance of [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock). Specifying `PropertyMock` as a new callable instructs `patch.object()` to use this alternative subclass of `Mock` when patching attributes.
