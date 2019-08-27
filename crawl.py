from utils.database_handler import Database_Handler
from utils.datastore_handler import Minio_Handler
import schedule
import csv
import time
import config
import requests
import os
import json
import sys
sys.path.append(os.getcwd())

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol":  "AAME",
    "apikey": config.API_KEY,
    "datatype": "csv"
}


def crawl_data(params, filename):
    response = requests.get(config.API_ENDPOINT, params=params)
    print(response.url)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for i, line in enumerate(response.iter_lines()):
            if i == 91:
                break
            if i >= 1:
                writer.writerow(line.decode('utf-8').split(',')[1:])


def save(filename):
    to_path = 'data/' + filename
    Minio_Handler.upload(filename, to_path)
    logs = {
        "name": filename,
        "file_uri": to_path
    }
    os.remove(filename)
    Database_Handler.insert(config.MONGO_COLLECTION, logs)


def do_job(params, filename):
    crawl_data(params, filename)
    save(filename)


schedule.every(30).seconds.do(
    do_job, params=params, filename=time.strftime("%Y%m%d")+'.csv')

while True:
    schedule.run_pending()
