---
title: Assignment 5
layout: code-page
permalink: /module-5/
description: curly.py - A very simple HTTP client
---

## Output

```bash
$ ./curly.py --help
# usage: curly.py [-h] [-v] URL [file]
#
# Retrieves a single webpage, and writes it to a file.
#
# positional arguments:
#   URL A URL to send a request to
#   file Output file to write to.
#
# optional arguments:
#   -h, --help show this help message and exit
#   -v, --verbose Prints connection headers
```

```bash
$ ./curly.py https://kennesaw.edu/ out.html
# Writing response data to out.html (31771 bytes)
$ cat out.html | head -n 5
# <!DOCTYPE html>
# <html lang="en" id="_63608cfd-163b-4208-b021-dd4e916bb815">
# <head>
#  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
#  <title>Kennesaw State University in Georgia</title>
```

```bash
$ ./curly.py https://placekitten.com/300/300 kitten.jpg
# Writing response data to kitten.jpg (8425 bytes)
$ imgcat kitten.jpg
```


<pre class="language-bash"><code class="language-bash">$ ./curly.py https://placekitten.com/300/300 kitten.jpg<br><span class="token comment"># Writing response data to kitten.jpg (8425 bytes)</span><br>$ imgcat kitten.jpg</code> <img style="display: block;" src="kitten.jpg" alt="an image of a kitten"></pre>



## Source code

```py
{% include curly.py %}
```