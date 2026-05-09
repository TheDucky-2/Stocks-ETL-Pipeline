from airflow.providers.http.hooks.http import HttpHook
from airflow.decorators import task

from datetime import datetime, timedelta

from include.constants import SYMBOL, DURATION


## ---------- TRANSFORMATION --------------

@task()
def transform_stocks_data(stocks_data, days_filter:int = 365):
    """Transform the extracted data from Alpha Vantage API."""

    all_data = stocks_data["Monthly Time Series"]

    filtered_data = [
        (key, value) for key, value in all_data.items()
        if datetime.strptime(key, "%Y-%m-%d") > (datetime.now() - timedelta(days=days_filter))
    ]

    for date, price in filtered_data:
        transformed_data= {
            "stock": SYMBOL,
            "duration": DURATION,
            "date": date,
            "volume": price["5. volume"],
            "open": price["1. open"],
            "close": price["4. close"],
            "high": price["2. high"],
            "low": price["3. low"]
        }
    return transformed_data
    