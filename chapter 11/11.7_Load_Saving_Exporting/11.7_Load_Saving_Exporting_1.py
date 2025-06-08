from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db')
df.to_sql('sales', engine, if_exists='replace', index=False)