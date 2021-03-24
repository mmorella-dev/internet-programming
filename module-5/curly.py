#! /usr/bin/env python
# File: curly.py
# Author: Mae Morella
#
# A very simple HTTPS client, using the Python requests module
# Extends the code in requests_client.py

import sys
import requests
import argparse
import logging
import pprint

# Take URL and file input by parsing command-line args

parser = argparse.ArgumentParser(
    description='Retrieves a single webpage, and writes it to a file.')
parser.add_argument('-v', '--verbose', action='store_true',
                    help="Prints connection headers")
parser.add_argument('url', metavar="URL", type=str,
                    help='A URL to send a request to')
parser.add_argument('file', nargs="?", help='Output file to write to.',
                    type=argparse.FileType('wb'), default=sys.stdout)

args = parser.parse_args()
url = args.url
outfile = args.file

logging.basicConfig(format="",
                    level=(logging.DEBUG if args.verbose else logging.INFO))

try:
    # Send HTTP GET request
    res = requests.get(url)

    # Print debug info
    elapsed_ms = int(res.elapsed.total_seconds() * 1000)
    logging.debug(
        f"Got response status {res.status_code} in {elapsed_ms} ms")
    logging.debug(res.headers)
    # for stdout, decode response
    if (outfile is sys.stdout):
      print(res.text)
    else:
      logging.info(
          f"Writing response data to {outfile.name} ({len(res.content)} bytes)")
      outfile.write(res.content)
    sys.exit(0)
except Exception as e:
    print("ERR:", e, file=sys.stderr)
    sys.exit(1)
