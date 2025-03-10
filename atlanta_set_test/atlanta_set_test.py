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

# print(df_atlanta_sql)

#Using AND/ OR operator to restrict the results to a smaller set
df_atlanta_sql_and_operator = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 and carrier = 'Verizon'; ",
                           con=os.getenv('RSR_SVC_CONN'))

# print(df_atlanta_sql_and_operator)

df_atlanta_sql_or_operator = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 and carrier = 'Verizon' or carrier = 'T-Mobile'; ",
                           con=os.getenv('RSR_SVC_CONN'))
# print(df_atlanta_sql_or_operator)

#Using NOT logical operator
# df_atlanta_sql_not_operator = pd.read_sql("select * from auto.test_summary_reporting where not collection_set_id = 12319 and carrier = 'Verizon'; ",
#                            con=os.getenv('RSR_SVC_CONN'))
# print(df_atlanta_sql_not_operator)

# Ordering a result alphabetically by a specific field

df_atlanta_sql_ordered = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 order by carrier;",
                           con=os.getenv('RSR_SVC_CONN'))
# print(df_atlanta_sql_ordered)

# By default the numerically order is ascending to change the order to be descending:

df_atlanta_sql_descending = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 order by test_event_id desc;",
                           con=os.getenv('RSR_SVC_CONN'))

# print(df_atlanta_sql_descending)

#Order rows by NULL value
df_atlanta_sql_null = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 order by access_success nulls first;",
                           con=os.getenv('RSR_SVC_CONN'))
# print(df_atlanta_sql_null)

#Limit the numbers of records to retrieve from a table
df_atlanta_sql_limited_by = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 limit 5;",
                           con=os.getenv('RSR_SVC_CONN'))
print(df_atlanta_sql_limited_by)

# Skip a number of rows, start after that offset
df_atlanta_sql_offset = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319 offset 5;",
                           con=os.getenv('RSR_SVC_CONN'))
print(df_atlanta_sql_offset)

#Retrieving the data from specific columns
df_atlanta_sql_columns= pd.read_sql("select carrier, carrier_id from auto.test_summary_reporting where collection_set_id = 12319 limit 2;",
                           con=os.getenv('RSR_SVC_CONN'))
print(df_atlanta_sql_columns)