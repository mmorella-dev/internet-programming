#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable(True)  # uncomment for debugging

SUPER_SECRET_ADMIN_PASSWORD = "admin123"
OUTFILE_NAME = "address.csv"

# create CGI header
print("Content-Type: text/plain; charset=UTF-8")
print()


# get data from form submission
form = cgi.FieldStorage()

if (form.getfirst("password") == SUPER_SECRET_ADMIN_PASSWORD):
    with open(OUTFILE_NAME, "r") as address_file:
        print(address_file.read())
else:
    print("Invalid password.")

