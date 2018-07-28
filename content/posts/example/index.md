---
title: "Example"
date: 2018-07-28T17:22:22-04:00
draft: true
---

This is an example post to showcase Markdown rendering. Hugo's built-in Markdown rendering engine is called [Blackfriday](https://gohugo.io/getting-started/configuration/#configure-blackfriday).

*Here's some italicized text.* **And here's some bolded text.** ~~Here's some strikethrough.~~

> Here's a pull quote. Wow, amazing! What a great pull quote.

Hyphens - should be converted -- like this. And also --- like this.

This is a footnote.[^1]

Let's see how an unordered list looks.

- first item
- another item
- final item

What a great list. What about an ordered list?

1. first item
2. another item
3. final item

## H2 Heading (with id!)

Now let's look at some code. Here's some `inline code`.

### H3 Heading

What about code blocks? This one uses code fences. I hope it has [syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/)!

```py
import os
from sys import path

# an example comment
if True and True:
    path.append('foo')

def foo(bar):
    return bar

if __name__ == '__main__':
    foo('baz')
```

This one uses Hugo's built-in `highlight` [shortcode](https://gohugo.io/content-management/shortcodes/), which can add line numbers and highlight lines.

{{< highlight python "linenos=table,hl_lines=2 8-9" >}}
import os
from sys import path

# an example comment
if True and True:
    path.append('foo')

def foo(bar):
    return bar

if __name__ == '__main__':
    foo('baz')
{{< /highlight >}}

### Images

Here are some images. They should be loaded from the [page bundle](https://gohugo.io/content-management/page-bundles/).

![](200x200.png)

![](400x200.png)

![](800x400.png)

TODO: Image processing/resizing examples, might require shortcodes.

### Tables

Here's how you make a table:

   Name | Age
--------|------
    Bob | 27
  Alice | 23

[^1]: Here's the footnote text!
