import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

df_jenny_sql = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12319;",
                           con=os.getenv('RSR_SVC_CONN'))