#!/usr/bin/python3.6
# main.py - controller for program.

import pprint

from modules import *
# import file also checks if the test html file is in the same directory as main.py

# load test data onto memory.
# test mode only.


data = open('testfile.html')

# parse data
soup = parse_data.load_data(data)
table = parse_data.find_main_table(soup)
rows = parse_data.cycle_rows(table, soup)

headers, body = parse_data.separate_headers_and_body(rows)

clean_data = parse_body.main(body)

output.datafile(clean_data)

output.log_()
