# db/customer.api.py

from .db import do_command

def get_all_customers_and_rentals():
  """Queries the database for all customers, addresses, and their rental counts
  :returns a list of dictionaries like {customer_id, last_name, first_name, rental_count, address}
  """
  customers = get_all_customers()
  for c in customers:
    c['rental_count'] = get_rental_count_for_customer(c['customer_id'])
  return customers

def get_all_customers():
  """Queries the database for all customers and addresses
  :returns a list of dicts like {customer_id, last_name, first_name, address}
  """
  return do_command("""SELECT customer_id, last_name, first_name, address
  from customer INNER JOIN address ON customer.address_id = address.address_id""")

def get_customer_by_id(customer_id):
  return do_command("select customer_id, last_name, first_name from customer where customer_id = ?", [customer_id])

def get_rental_count_for_customer(customer_id):
  return do_command("select count(all) as rental_count from rental where inventory_id = ?", [customer_id])[0]['rental_count']
