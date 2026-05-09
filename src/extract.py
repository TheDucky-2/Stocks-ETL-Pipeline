from airflow.providers.http.hooks.http import HttpHook
from airflow.decorators import task

from include.constants import DURATION, SYMBOL,API_ENDPOINT, API_KEY, api_connection_id 


## ----------EXTRACTION --------------
@task()
def extract_stocks_data():
    """Extract Stocks Data from Alpha Vantage API using Airflow"""

    http_hook = HttpHook(
        http_conn_id = api_connection_id,
        method = "GET"
    )

    response = http_hook.run(API_ENDPOINT)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}. Failed to fetch stocks data.")
    