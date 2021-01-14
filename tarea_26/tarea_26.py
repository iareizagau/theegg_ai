import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime


class covid19:
    def __init__(self):
        path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr.json'
        self.path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr-positives.json'
        self.path_file_json = 'data.json'
        self.df = pd.DataFrame()

    def get_data(self):
        response = requests.get(self.path_json)
        data = response.json()
        return data

    def process_data(self):
        json_data = self.get_data()
        self.df = pd.DataFrame(
            {'dates': json_data['dates'],
             'menCount': json_data['menCount'],
             'womenCount': json_data['womenCount'],
             'age_0_9_Count': json_data['age_0_9_Count'],
             'age_10_19_Count': json_data['age_10_19_Count'],
             'age_20_29_Count': json_data['age_20_29_Count'],
             'age_30_39_Count': json_data['age_30_39_Count'],
             'age_40_49_Count': json_data['age_40_49_Count'],
             'age_50_59_Count': json_data['age_50_59_Count'],
             'age_60_69_Count': json_data['age_60_69_Count'],
             'age_70_79_Count': json_data['age_70_79_Count'],
             'age_80_89_Count': json_data['age_80_89_Count'],
             'age_90_X_Count': json_data['age_90_X_Count']}
        )
        # print(self.df['dates'].values[0], type(self.df['dates'].values[0]))
        # print(self.df['dates'].values)
        self.df['month'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').strftime('%B') for date in self.df['dates'].values]
        print(self.df.head())

    def plot(self):
        self.process_data()
        # self.df.plot(kind='line', y=['menCount', 'womenCount'])
        self.df.plot(kind='line', x='month',
                     y=["age_0_9_Count", "age_10_19_Count", "age_20_29_Count", "age_30_39_Count",
                        "age_40_49_Count", "age_50_59_Count", "age_60_69_Count", "age_70_79_Count",
                        "age_80_89_Count", "age_90_X_Count"],
                     figsize=(40, 20))
        plt.xticks(rotation=0)
        plt.xlabel('Date')
        plt.ylabel('Infectios per day')
        plt.show()


if __name__ == '__main__':
    covid = covid19()
    covid.plot()
