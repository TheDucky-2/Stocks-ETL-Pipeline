import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
api_connection_id = os.getenv("API_CONN_ID")
POSTGRES_CONN_ID = os.getenv("POSTGRES_ID")

SYMBOL = "AAPL"
DURATION = "TIME_SERIES_MONTHLY"
API_ENDPOINT = f'https://www.alphavantage.co/query?function={DURATION}&symbol={SYMBOL}&apikey={API_KEY}'