import airtable
import pandas as pd
import json


#Get configuration from config.json
f = open('config.json')
config = json.load(f)
f.close()

API_KEY = config['api_key']
BASE_ID = config['base_id']
table_name = config['table_name']

#Connection Object
at = airtable.Airtable(BASE_ID, API_KEY)

#Get all records and create the panda dataframe
df = pd.DataFrame()
for r in at.iterate(table_name, max_records=5): 
  df = df.append(r["fields"], ignore_index = True)

print(df)