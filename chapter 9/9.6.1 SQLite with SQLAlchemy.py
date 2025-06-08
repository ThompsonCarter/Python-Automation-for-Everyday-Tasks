from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(os.getenv("DB_URL"), echo=False)

df.to_sql("items", engine, if_exists="replace", index=False)