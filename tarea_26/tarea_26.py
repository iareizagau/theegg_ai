import pandas as pd
import requests

path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr.json'
response = requests.get("http://httpbin.org/stream/1")
data = response.json()
df = pd.read_json(path_json)
print(df)

