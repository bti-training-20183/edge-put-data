import requests
import os
import json
import sys
sys.path.append(os.getcwd())
import config
import time
import csv


params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" :  "MSFT",
    "apikey" : config.API_KEY,
    "datatype" : "csv"
}

response = requests.get(config.API_ENDPOINT, params=params)
print(response.url)
filename = 'test'+'.csv'
with open(filename, 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))

