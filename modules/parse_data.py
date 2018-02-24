#!/usr/bin/python3.6
#parse_data.py - parses data on coinmarketcap

from bs4 import BeautifulSoup

def load_data(data):
    #soup = BeautifulSoup(data.read(), 'lxml') # for testing
    soup = BeautifulSoup(data, 'lxml') # for production
    return soup

def reprocess_data(data):
    soup = BeautifulSoup(data, 'lxml')
    return soup

def find_main_table(soup):
    table = soup.find(id='currencies-all')
    return table

def cycle_rows(table, soup):
    #soup = reprocess_data(table)
    rows = soup.find_all('tr')
    return rows

def separate_headers_and_body(rows):
    headers = rows[0]
    body = rows[1:]
    return headers, body
