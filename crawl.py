import requests
import os
import json
import sys
sys.path.append(os.getcwd())
import config
import time
import csv
import schedule
from utils.datastore_handler import Minio_Handler
from utils.database_handler import Database_Handler

params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" :  "MSFT",
    "apikey" : config.API_KEY,
    "datatype" : "csv"
}

def crawl_data(params, filename):
    response = requests.get(config.API_ENDPOINT, params=params)
    print(response.url)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for line in response.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))

def save(filename):
    to_path = 'data/' + filename
    Minio_Handler.upload(filename,to_path)
    logs = {
        "filename" : filename,
        "file_uri" : to_path
    }
    Database_Handler.insert(config.MONGO_COLLECTION, logs)
    
def do_job(params, filename):
    crawl_data(params,filename)
    save(filename)

schedule.every(15).seconds.do(do_job, params = params, filename = time.ctime())

while True:
    schedule.run_pending()
