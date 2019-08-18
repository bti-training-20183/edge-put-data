import requests
import os
import json
import sys
sys.path.append(os.getcwd())
import config



params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" :  "MSFT",
    "outputsize" : "compact",
    "datatype" : "CSV",
    "apikey" : config.API_KEY
}

r = requests.get(config.API_ENDPOINT, params=params)
print(r.url)