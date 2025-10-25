---
title: Python Proxy Classes
description: Managing access to subclass instances with Python's __getattr__ and __call__ methods.
date: 2017-01-20T21:52:03-04:00
lastmod: 2019-03-02T20:10:21-04:00
---

Let's say you need a class which provides the functionality of two classes at the same time. Those two classes happen to be subclasses of the same base class. You could approach the problem by overriding every property and method provided by the base class, routing calls to the appropriate subclass in each. However, there's a more elegant way to achieve this effect using Python's `__getattr__` and `__call__` methods. The key is to avoid thinking of the problem as one requiring the combination of multiple classes. Instead, the goal is to proxy to these classes.

Consider this simple example. Say you need a class which can dispense both snacks and drinks. `SnackVendingMachine` and `DrinkVendingMachine`, subclasses of `VendingMachine`, have already been implemented. Here's `VendingMachine`:

```python
class VendingMachine:
    def __init__(self):
        # Used to keep track of money collected by the machine.
        self.income = 0

    def dispense(self, product_code, money):
        """
        Dispenses a product identified by a unique product_code.
        """
        raise NotImplementedError('dispense() must be implemented.')
```

Assume you can use the `product_code` to tell which subclass to use. If you were to combine the classes, your solution might be `SnackAndDrinkVendingMachine`:

```python
class SnackAndDrinkVendingMachine(VendingMachine):
    def dispense(self, product_code, money):
        if product_code.startswith('snack'):
            return SnackVendingMachine().dispense(product_code, money)
        elif product_code.startswith('drink'):
            return DrinkVendingMachine().dispense(product_code, money)
```

This is fine if you only have to deal with one method and your class doesn't need to store state on instance attributes like `income`, which `SnackVendingMachine` and `DrinkVendingMachine` increment to keep track of money collected by the machine. But what if you have to handle many methods, or are working with several possibly divergent classes, each of which stores state on a variety of instance attributes, some not present on the base class? With an approach like `ProxiedVendingMachine`, you don't need to override anything; attribute access is proxied to instances of `SnackVendingMachine` and `DrinkVendingMachine`.

```python
class ProxiedCall:
    """
    Utility class used in conjunction with ProxiedVendingMachine to
    route method calls between vending machine classes.
    """
    def __init__(self, proxy, method_name):
        self.proxy = proxy
        self.method_name = method_name

    def __call__(self, *args, **kwargs):
        try:
            # The only methods on vending machine classes which accept
            # product codes as positional arguments expect them as the
            # second positional argument. Hence, we expect the same to
            # be true here.
            product_code = args[0]
        except IndexError:
            product_code = False

        machine = self._get_machine(product_code)

        # Look up the method and call it.
        return getattr(machine, self.method_name)(*args, **kwargs)

    def _get_machine(self, product_code):
        for machine, prefix in self.proxy.machines:
            if product_code and product_code.startswith(prefix):
                return machine

        # If we don't have a product_code to go off of, default to the
        # last machine in the list on the proxy.
        return machine


class ProxiedVendingMachine:
    """
    Vending machine class which proxies to SnackVendingMachine and
    DrinkVendingMachine, defaulting to DrinkVendingMachine.
    """
    def __init__(self):
        snack_machine = SnackVendingMachine()
        drink_machine = DrinkVendingMachine()

        self.machines = [
            (snack_machine, 'snack'),
            (drink_machine, 'drink'),
        ]

    def __getattr__(self, name):
        # For each vending machine, check if the requested attribute
        # is defined. If the attr is defined on both, we take the one
        # defined for DrinkVendingMachine.
        for machine, __ in self.machines:
            try:
                attr = getattr(machine, name)
            except AttributeError:
                pass

        # The value defined for the attribute in the machines may be
        # None, which prevents us from defaulting `attr` to None.
        try:
            attr
        except NameError:
            # The attribute wasn't found on either machine.
            raise AttributeError
        else:
            # The attribute was found. If it's callable, return a
            # ProxiedCall which will route method calls to the
            # correct machine.
            if callable(attr):
                return ProxiedCall(self, name)
            else:
                return attr
```

This technique can be extended to proxy to classes that implement different interfaces. You just need a way to determine which class to route to.

For a less contrived example involving [DRF](https://github.com/tomchristie/django-rest-framework) pagination classes, see [edx/course-discovery](https://github.com/edx/course-discovery/blob/867c39b675b660ac2ee9b5ec4443889d70ffd968/course_discovery/apps/api/pagination.py). In a nutshell: DRF allows you to set a single pagination class on your views. You can use a `ProxiedPagination` class if you want your API to provide both `PageNumberPagination` and `LimitOffsetPagination`.
