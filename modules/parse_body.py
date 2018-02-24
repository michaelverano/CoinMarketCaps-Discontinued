#!/usr/bin/python3
#parse_body.py - parses the body from coinmarket cap.

from bs4 import BeautifulSoup

def main(body):

    row_agregate = []
    for number, row in enumerate(body):
        print('parsing coin rankd ' + str(number))
        column = {}
        soup = BeautifulSoup(str(row), 'lxml')

        column['rank'] = parse_rank_number(soup)
        column['name'] = parse_name(soup)
        column['symbol'] = parse_symbol(soup)
        column['market_cap'] = parse_market_cap(soup)
        column['price'] = parse_price(soup)
        column['circulating_supply'] = parse_circulating_supply(soup)
        column['_24hr_volume'] = parse_24hr_volume(soup)
        column['_1hr_percent_volume'] = parse_1hr_percent_volume(soup)
        column['_24hr_percent_volume'] = parse_24hr_percent_volume(soup)
        column['_7day_percent_volume'] = parse_7day_percent_volume(soup)

        row_agregate.append(column)
    return row_agregate
        
# parse rank (#)
def parse_rank_number(soup):
    rank = soup.find(class_='text-center')
    return rank.text.strip()

# parse name
def parse_name(soup):
    name = soup.find(class_='currency-name-container')
    return name.text.strip()

# parse symbol
def parse_symbol(soup):
    symbol = soup.find(class_='text-left col-symbol')
    return symbol.text.strip()

# parse market cap
def parse_market_cap(soup):
    market_cap = soup.find(class_='no-wrap market-cap text-right')
    str_mcap = market_cap.text.strip()
    int_mcap = process_int(str_mcap)
    return [str_mcap, int_mcap]

# parse price
def parse_price(soup):
    price = soup.find(class_='price')
    str_price = price.text.strip()
    float_price = process_float(str_price)
    return [str_price, float_price]
    
# parse circulating supply
def parse_circulating_supply(soup):
    circulating_supply = soup.find(class_='no-wrap text-right circulating-supply')
    str_supply = circulating_supply.text.split()[0]
    int_supply = process_int(str_supply)
    return [str_supply, int_supply]
    
# parse volume (24)
def parse_24hr_volume(soup):
    _24hr_volume = soup.find(class_='volume')
    str_supply = _24hr_volume.text.strip()
    int_supply = process_int(str_supply)
    return [str_supply, int_supply]


# parse%1h
def parse_1hr_percent_volume(soup):
    percentages  = soup.find_all('td')
    percent_str = percentages[7].text
    percent_float = process_float(percent_str)
    return [percent_str, percent_float]
    
# parse %24h
def parse_24hr_percent_volume(soup):
    percentages = soup.find_all('td')
    percent_str = percentages[8].text
    percent_float = process_float(percent_str)
    return [percent_str, percent_float]

# parse %7d
def parse_7day_percent_volume(soup):
    percentages = soup.find_all('td')
    percent_str = percentages[9].text
    percent_float = process_float(percent_str)
    return [percent_str, percent_float]

# process ints
def process_int(string_numbers):
    if string_numbers == '?':
        return 'N/A'

    if string_numbers == 'Low Vol':
        return 'Low Volume'

    try:
        remove_currency = string_numbers.strip('>$%?')
        remove_commas = remove_currency.replace(',', '')
        
        #quickfix for floats that happen to be here.
        try:
            str_to_int = int(remove_commas)
        except (ValueError, UnboundLocalError):
            process_float(remove_commas)

        
    except ValueError:
        print('error on {}, {}'.format(string_numbers, 'integer'))        
        return 0

    
# process floats
def process_float(string_numbers):
    if string_numbers == '?':
        return 'N/A'

    if string_numbers == 'Low Vol':
        return 'Low Volume'
    
    try:
        remove_currency = string_numbers.strip('>$%?')
        remove_commas = remove_currency.replace(',', '')
        str_to_float = float(remove_commas)
        return str_to_float
    except ValueError:
        print('error on {}, {}'.format(string_numbers, 'float'))
        return 0.00
