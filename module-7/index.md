---
title: Assignment 7
description: A basic HTML + Python app, using Common Gateway Interface and the Apache HTTP Server.
layout: code-page
github-url: https://github.com/morellam-dev/cs-4720-internet-programming/tree/main/module-7
---

### htdocs/form.html

![A screenshot of the main form page](screenshot-form.png)

````html
{% include htdocs/form.html | escape %}
````

<style>
img {
  display: block;
  max-width: 80%;
  margin: 0 auto;
}
</style>

### htdocs/cgi-bin/submit.py

![A screenshot of the form after submission](screenshot-submit.png)

````py
{% include htdocs/cgi-bin/submit.py | escape %}
````
### htdocs/cgi-bin/dump_data.py

![A screenshot of the data dump](screenshot-dump.png)


````py
{% include htdocs/cgi-bin/dump_data.py | escape %}
````
