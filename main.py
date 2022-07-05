'''
import requests
import pandas as pd
import sqlalchemy as db


#creating data frame to add data to
col_names = ['Title', 'Author', 'Link']
df  = pd.DataFrame(columns = col_names)

engine = db.create_engine('sqlite:///hackernews.db')
df.to_sql('stories', con=engine, if_exists='replace', index=False)
print(df)
'''
print('in main.py') 
