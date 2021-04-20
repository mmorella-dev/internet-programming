#!/usr/bin/env python

import os
import cgi
import cgitb
# cgitb.enable(True) # uncomment for debugging

# create CGI header
print ("Content-Type: text/html; charset=UTF-8")
print()
# get data from form submission
form = cgi.FieldStorage()
shipping_name = form.getfirst("shipping-name","not present")
shipping_zip = form.getfirst("shipping-zip","not present")
billing_name = form.getfirst("billing-name", shipping_name)
billing_zip = form.getfirst("billing-zip", shipping_zip)
# print to user
print("<h1>Your order was confirmed!</h1>")
print("<h2>Shipping info</h2>")
print(f"<address>{shipping_name}<br>{shipping_zip}</address>")
print("<h2>Billing info</h2>")
print(f"<address>{billing_name}<br>{billing_zip}</address>")
