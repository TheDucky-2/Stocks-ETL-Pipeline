from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task

from include.constants import  POSTGRES_CONN_ID


## ---------- LOADING DATA INTO POSTGRES--------------        

@task()
def load_stocks_data(transformed_data):
    """Load data into PostgresQL DB after transformation"""

    pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID
    )
    connection = pg_hook.get_conn()

    cursor = connection.cursor() 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks(
                    stocks TEXT,
                    duration TEXT,
                    date TIMESTAMP,
                    volume BIGINT,
                    open FLOAT,
                    close FLOAT,
                    high FLOAT,
                    low FLOAT
                    )""")
    
    cursor.execute("""
    INSERT INTO TABLE stocks (stocks, duration, date, volume, open, close, high, low) VALUES(%s,%s, %s, %s, %s, %s, %s, %s)
    """, transformed_data["stock"], transformed_data["duration"], transformed_data["date"], transformed_data["volume"],
    transformed_data["open"], transformed_data["close"], transformed_data["high"], transformed_data["low"])

    connection.commit()