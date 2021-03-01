# db/db.py

import sqlite3
from os.path import join, split

# this file is external to the code
SQLITE_DATABASE_NAME = 'sqlite-sakila.sq'

def dictionary_factory(cursor, row):
  """
  Create a dictionary from rows in a cursor result.
  The keys will be the column names
  :param cursor   a cursor from which a query row has just been fetched
  :param row      the row that was fetched
  :return         A dictionary associating column names to values
  """
  col_names = [d[0].lower() for d in cursor.description]
  return dict(zip(col_names, row))

def get_connection():
  fname = SQLITE_DATABASE_NAME
  conn = sqlite3.connect(fname)
  conn.row_factory = dictionary_factory
  return conn

def do_command(cmd, args=[]):
  """
  Takes a SQL command and returns a list of results.
  Allows for arguments, providing a default value of []
  """
  try:
    conn = get_connection()
    crs = conn.cursor()
    crs.execute(cmd, args)
    return crs.fetchall()
  finally:
    conn.close()
