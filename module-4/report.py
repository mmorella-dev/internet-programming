# report.py

from db import db_access, customer_api

# Make a database query
customers = customer_api.get_all_customers_and_rentals()

# Attempt to nicely format the output as a table
print(f"{'ID':>3}|{'FirstName':>10}|{'LastName':14}|{'Rentals':3}\t|{'Address'}")
print('=' * 80)
for c in customers:
    print(f"{c['customer_id']:>3} {c['first_name']:>10} {c['last_name']:14} {c['rental_count']:3}\t{c['address']}")
