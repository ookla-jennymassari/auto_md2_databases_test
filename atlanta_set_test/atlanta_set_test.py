import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

# Debugging: Print the connection string
connection_string = os.getenv("RSR_SVC_CONN")
# print("RSR_SVC_CONN:", connection_string)

# Test the connection
try:
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        print("Connection to the database was successful!")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
    exit(1)



df_atlanta_sql = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319;",
                           con=os.getenv('RSR_SVC_CONN'))

print(df_atlanta_sql)