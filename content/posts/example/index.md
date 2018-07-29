---
title: "Example"
date: 2018-07-28T17:22:22-04:00
draft: false
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

This one uses Hugo's built-in `highlight` [shortcode](https://gohugo.io/content-management/shortcodes/). It's good for highlighting specific lines.

{{< highlight python "hl_lines=2 8-9" >}}
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

![](800x400.png)

![](400x200.png)

![](200x200.png)

Resize to width and height of 200px without preserving aspect ratio:

![]({{< imgproc 800x400 Resize 200x200 >}})

Resize to width of 200px while preserving aspect ratio:

![]({{< imgproc 800x400 Resize 200x >}})

Resize to height of 200px while preserving aspect ratio:

![]({{< imgproc 800x400 Resize x200 >}})

Scale down to 200x200 while preserving aspect ratio:

![]({{< imgproc 800x400 Fit 200x200 >}})

Scale up (resize and crop) to 800x400 while preserving aspect ratio:

![]({{< imgproc 200x200 Fill 800x400 >}})

Same operation, anchored to the center:

![]({{< imgproc 200x200 Fill "800x400 Center" >}})

See the Hugo [docs](https://gohugo.io/content-management/image-processing) for more details!

### Tables

Here's how you make a table:

   Name | Age
--------|------
    Bob | 27
  Alice | 23

[^1]: Here's the footnote text!