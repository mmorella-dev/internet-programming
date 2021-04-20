#!/usr/bin/env python

import os
import cgi
import io
import cgitb
import random
cgitb.enable(True) # uncomment for debugging

OUTFILE_NAME = "address.csv"

# create CGI header
print ("Content-Type: text/html; charset=UTF-8")
print()


# get data from form submission
form = cgi.FieldStorage()
order_num = random.randrange(100000, 999999)
shipping_name = form.getfirst("shipping-name", None)
shipping_zip = form.getfirst("shipping-zip", None)
billing_name = form.getfirst("billing-name", shipping_name)
billing_zip = form.getfirst("billing-zip", shipping_zip)

if not shipping_name and billing_name:
   print(f"<h1>Error: Invalid data</h1>")
   print(f"<p>Your order could not be completed.</p>")
   exit(1)

# Create a file, if it
try:
    with open(OUTFILE_NAME, "x") as outfile:
        # write header
        print("OrderNumber,ShippingName,ShippingZip,BillingName,BillingZip", file=outfile)
except (FileExistsError):
    pass

with open(OUTFILE_NAME, "a+") as outfile:

    print(order_num, shipping_name, shipping_zip, billing_name, billing_zip, sep=",", file=outfile)

print("")
# print to user
print(f"<h1>Your order #{order_num} was confirmed!</h1>")
print("<h2>Shipping info</h2>")
print(f"<address>{shipping_name}<br>{shipping_zip}</address>")
print("<h2>Billing info</h2>")
print(f"<address>{billing_name}<br>{billing_zip}</address>")
