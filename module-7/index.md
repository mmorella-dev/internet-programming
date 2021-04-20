---
title: Assignment 7
description: A basic HTML + Python app, using Common Gateway Interface and the Apache HTTP Server.
layout: code-page
github-url: https://github.com/morellam-dev/cs-4720-internet-programming/tree/main/module-7
---

## Screenshots

![A screenshot of the main form page](screenshot-form.png)

![A screenshot of the form after submission](screenshot-submit.png)

<style>
img {
  display: block;
  max-width:100%;
}
</style>

## Apache code

### htdocs/cgi-bin/submit.py

````py
{% include htdocs/cgi-bin/submit.py | escape %}
````

### htdocs/form.html

````html
{% include htdocs/form.html | escape %}
````
