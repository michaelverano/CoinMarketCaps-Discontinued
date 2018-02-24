#!/home/mverano/Projects/CoinMarktCaps/bin/python3.6
# make_test_file.py - creates a test file in order to parse data.

import requests

r = requests.get('https://coinmarketcap.com/coins/views/all/')

localfile = open('testfile.html', 'w')
localfile.write(r.text)

localfile.close()
