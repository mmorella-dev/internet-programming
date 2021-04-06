---
layout: code-page
title: Assignment 4
description: Simple database and socket programs in Python
permalink: /module-4/
---

## Assignment 4: Database

<style>
.dirtree .folder {
  list-style-type: '📁';
}

.dirtree .file {
  list-style-type: '📄';
}
</style>

<h3>Program file structure</h3>
<ul class="dirtree">
  <li class="folder">
    <span>module-4/database</span>
    <ul>
      <li class="folder">
        <span>db</span>
        <ul>
          <li class="file">customer_api.py</li>
          <li class="file">db.py</li>
        </ul>
      </li>
      <li class="file">report.py</li>
      <li class="file">sqlite-sakila.sq</li>
    </ul>
  </li>
</ul>

## Output

```bash
database$ python report.py
#  ID| FirstName|LastName      |Rentals   |Address
# ==============================================================================
#  1       MARY SMITH            3       1913 Hanoi Way
#  2   PATRICIA JOHNSON          5       1121 Loja Avenue
#  3      LINDA WILLIAMS         2       692 Joliet Street
#  4    BARBARA JONES            2       1566 Inegl Manor
#  5  ELIZABETH BROWN            0       53 Idfu Parkway
#  6   JENNIFER DAVIS            5       1795 Santiago de Compostela Way
#  7      MARIA MILLER           4       900 Santiago de Compostela Parkway
#  8      SUSAN WILSON           2       478 Joliet Way
#  9   MARGARET MOORE            2       613 Korolev Drive
# 10    DOROTHY TAYLOR           3       1531 Sal Drive
# ... 400 more lines
```

### report.py

```py
{% include database/report.py %}
```

### db/customer_api.py

```py
{% include database/db/customer_api.py %}
```


### db/db.py

```py
{% include database/db/db.py %}
```

## Assignment 4: Sockets

<!-- File directory tree-->
<ul class="dirtree">
  <li class="folder">
    <span>module-4/sockets</span>
    <ul>
      <li class="folder">
        <span>simple_server</span>
        <ul>
          <li class="file">server.py</li>
        </ul>
      </li>
      <li class="folder">
        <span>polynomials</span>
        <ul>
          <li class="file">polynomials.py</li>
        </ul>
      </li>
      <li class="file">polynomial_client.py</li>
      <li class="file">polynomial_server.py</li>
    </ul>
  </li>
</ul>

### Output

```bash
sockets$ python polynomial_server.py &> /dev/null &
# (server running in background on port 12345)
sockets$ python polynomial_client.py
#📤 Sent: `E1.0 -945 1689 -950 230 -25 1`
#📩 Recv: `E0.0`
#✅ Matched expected response
#
#📤 Sent: `S0 2 -945 1689 -950 230 -25 1 1e-15`
#📩 Recv: `S1.0000000000000004`
#✅ Matched expected response
#
#📤 Sent: `G4.1 0 0`
#📩 Recv: `XIncorrect command type`
#✅ Matched expected response
#
#📤 Sent: `4 1 0`
#📩 Recv: `Xcould not convert string to float: ''`
#✅ Matched expected response
#
#📤 Sent: `E1.0`
#📩 Recv: `XToo few arguments`
#✅ Matched expected response
#
#📤 Sent: `S1.0`
#📩 Recv: `XToo few arguments`
#✅ Matched expected response
#
#📤 Sent: `S0 2 -945 1689 -950 230 -25 1 -1e-15`
#📩 Recv: `XInvalid tolerance`
#✅ Matched expected response
#
#📤 Sent: `Not a number`
#📩 Recv: `Xcould not convert string to float: 'ot'`
#✅ Matched expected response
#
#📤 Sent: `S0 2 -945 1689 -950 230 -25 1 0`
#📩 Recv: `XInvalid tolerance`
#✅ Matched expected response
#
#📤 Sent: `S0 2 -945 1689 -950 230 G 1 1e-15`
#📩 Recv: `Xcould not convert string to float: 'G'`
#✅ Matched expected response
```

### polynomial_client.py

```py
{% include sockets/polynomial_client.py %}
```

### polynomial_server.py

```py
{% include sockets/polynomial_server.py %}
```