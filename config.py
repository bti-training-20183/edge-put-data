from os import environ

MINIO_ACCESS_KEY = environ["MINIO_ACCESS_KEY"] if environ.get(
    "MINIO_ACCESS_KEY") else "6D8D341ABA51C6ED"
MINIO_SECRET_KEY = environ["MINIO_SECRET_KEY"] if environ.get(
    "MINIO_SECRET_KEY") else "HYOjcwvYuPhS6qbXS42YNkKWKfcDnV9E"
MINIO_URL = environ["MINIO_URL"] if environ.get(
    "MINIO_URL") else "play.min.io:9000"
MINIO_BUCKET = environ["MINIO_BUCKET"] if environ.get(
    "MINIO_BUCKET") else "brains"
MONGO_URL = environ["MONGO_URL"] if environ.get("MONGO_URL") else "mongodb://localhost:27017" 
MONGO_DB = environ["MONGO_DB"] if environ.get("MONGO_DB") else "logsDB"

API_ENDPOINT = environ["API_ENDPOINT"] if environ.get("API_ENDPOINT") else "https://www.alphavantage.co/query"
API_KEY = environ["API_KEY"] if environ.get("API_KEY") else "KFPBCODIA6K92KZF"
