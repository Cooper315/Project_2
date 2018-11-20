from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///NSF_data.db', echo=False)

chunks = pd.read_csv('db/NSF_expenditures.csv', chunksize=2000)
for chunk in chunks:
    chunk.to_sql(name='NSF', if_exists='append', con=engine)