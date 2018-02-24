#!usr/bin/python3.6
#output.py - creates output test file to show me what was output from the code.

import csv
import os
import datetime

def datafile(data):
    if 'data' not in os.listdir(os.getcwd()):
        create_data_directory()

    data_name = str(datetime.datetime.now()) + '_CoinMarketCap.csv'
    datafile = open('./data/' + data_name, 'a')
    
    for items in data:    
        datawriter = csv.writer(datafile)
        datawriter.writerow([str(items)])

    datafile.close()
    
    
def create_data_directory():
    os.mkdir('data')

def log_():
    if 'logs' not in os.listdir():
        create_log_directory()

    create_log_file()
        
def create_log_directory():
    os.mkdir('logs')

def create_log_file():
    logfile = open('./logs/log_file.csv', 'a')
    logwrite = csv.writer(logfile)
    logwrite.writerow(['Coin Market Cap parsed on ' + str(datetime.datetime.now())])
    logfile.close()
