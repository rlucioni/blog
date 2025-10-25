---
title: Example
description: Sandbox for testing static site generation features
date: 2025-10-13T20:00:00-04:00
draft: true
---

This is an example post to showcase Markdown and other markup rendering.

_Here's some italicized text._ **And here's some bolded text.** ~~Here's some strikethrough.~~ "This text has some quotes around it."

> Here's a block quote. Wow, amazing! What a great block quote. What if it gets really long? It should wrap around to the next line.

Hyphens - should be converted -- like this. And also --- like this.

This is a footnote.[^1] [And this should be a really long link that if we're lucky might get broken onto another line](https://www.merriam-webster.com/dictionary/long).

Let's see how an unordered list looks.

- first item
- another item
- final item

What a great list. What about an ordered list?

1. first item
2. another item
3. final item

## H2 Heading (with id!)

This is an h2. It's smaller than an h1. All headers should have an ID assigned to them.

### H3 Heading

This is an h3. Getting smaller.

#### H4 Heading

This is an h4. As small as we get!

##### H5 Heading

This is an h5. No difference.

###### H6 Heading

This is an h6. No difference.

## Code

Now let's look at some code. Here's some `inline code`. What about code blocks? This one uses code fences. It should have syntax highlighting.

```python
import os
from sys import path

# an example comment
if True and True:
    path.append('foo')

# another really long comment that just won't end for some reason; wow it really keeps going and going and going, hopefully you had to scroll horizontally to get here without it running off the page
def foo(bar):
    return bar

if __name__ == '__main__':
    foo('baz')
```

What about diffs?

```diff-js
function foo() {
-  return false;
+  return true;
}
```

### Images

Here are some images.

![](200x200.png)

![](400x200.png)

![](800x400.png)

They can be automatically processed into better file formats and resized, such as to a width of 200px while preserving aspect ratio:

<img src="800x400.png" alt="800x400 resized to width of 200px" width="200">

### Tables

You can create tables with pipes `|` and hyphens `-`. Pipes separate each column. Hyphens create each column's header.

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |

Phew, that was a lot of examples.

[^1]: Here's the footnote text!
