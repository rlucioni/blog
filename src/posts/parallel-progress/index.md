---
title: Parallel Progress
description: Visually tracking the progress of Python tasks running in parallel.
date: 2016-03-11T21:52:21-04:00
lastmod: 2019-03-14T16:10:21-04:00
---

Need to keep an eye on the progress of parallelized tasks? If you're using Python's [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) module, one way to do it is with [`tqdm`](https://pypi.org/project/tqdm/), a nice package for generating progress bars. Here's how it looks.

{% asciinema "progress.cast" %}

And here's the code for `progress.py`.

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

from tqdm import tqdm


def nap():
    time.sleep(1)


def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(nap) for i in range(10)]

        kwargs = {
            'total': len(futures),
            'unit': 'nap',
            'unit_scale': True,
            'leave': True
        }

        for f in tqdm(as_completed(futures), **kwargs):
            pass


if __name__ == '__main__':
    main()
```

Since [`as_completed()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed) doesn't provide a `__len__` method yielding the count of [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future) instances to be executed, we need to tell `tqdm` how much work we expect to be done using the `total` parameter.
