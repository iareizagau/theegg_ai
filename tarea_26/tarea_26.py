import pandas as pd
import requests
import json

url = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr.json'
response = requests.get(url)
data = response.json()
print(data)
df = pd.json_normalize(data, 'features')
df.head(10)
data = json.dumps(data)
print(data, type(data))
df = pd.read_json()
print(df)

