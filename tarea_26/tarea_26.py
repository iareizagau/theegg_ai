import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
from datetime import datetime
from utils_pandas import Pandas
import numpy as np

pd.plotting.register_matplotlib_converters()
# %matplotlib inline
import seaborn as sns

desired_width = 270
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 21)


class Covid19:
    def __init__(self, pandas):
        self.pd = pandas
        path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr.json'
        self.path_json = ''
        self.path_file_json = 'data.json'
        self.df = pd.DataFrame()
        self.__init__fechas_clave()

    def __init__fechas_clave(self):
        self.estado_alarma1 = datetime.strptime('2020-03-14T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.desescalada_fase0 = datetime.strptime('2020-05-15T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.desescalada_fase1 = datetime.strptime('2020-05-20T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.desescalada_fase2 = datetime.strptime('2020-06-10T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.desescalada_fase3 = datetime.strptime('2020-06-21T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.restriccion_perimetral1_on = datetime.strptime('2020-10-31T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.restriccion_perimetral1_off = datetime.strptime('2020-12-12T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.restriccion_perimetral2_on = datetime.strptime('2021-01-25T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
        self.restriccion_perimetral2_off = datetime.strptime('2021-02-15T22:00:00Z', '%Y-%m-%dT%H:%M:%SZ')

    def covid19_pcr_positivos(self):
        self.path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-pcr-positives.json'
        json_data = self.get_data()
        self.df = pd.DataFrame({'date_time': json_data['dates'],
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
                                'age_90_X_Count': json_data['age_90_X_Count']})
        dates = self.df['date_time'].values
        self.df['month'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').strftime('%B') for date in dates]
        self.df['date'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').date() for date in dates]
        self.df['weeknumber'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').isocalendar()[1] for date in dates]
        self.df['all_infected'] = self.df['menCount'] + self.df['womenCount']
        df_mean_week = self.pd.group_data(self.df, 'weeknumber', 'mean')
        print(self.df.head())
        self.plot_weekly(df_mean_week)
        # self.plot_covid19_pcr_positivos(self.df)

    def covid19_deceased(self):
        self.path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-deceasedPeopleCount.json'
        json_data = self.get_data()
        self.df = pd.DataFrame({'dates': json_data['dates'],
                                'positiveCounts': json_data['positiveCounts']})
        last_update = json_data['lastUpdateDate']

    def covid19_hospital(self):
        self.path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-byhospital.json'
        json_data = self.get_data()
        data = {'deceasedHospital': json_data['byHospitalByDate']['deceasedPeopleCountByHospital'],
                'icuHospital': json_data['byHospitalByDate']['icuPeopleCountByHospital']}
        self.df = pd.DataFrame({'dates': data['deceasedHospital'][0]['dates']})
        for dat in data['deceasedHospital']:
            # d = {dat['dimension']: dat['values']}
            self.df[dat['dimension']] = dat['values']

        self.df['month'] = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').strftime('%B') for date in
                            self.df['dates'].values]
        print(self.df)
        last_update = json_data['lastUpdateDate']

    def covid19_epidemic_status(self):
        self.path_json = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/generated/covid19-epidemic-status.json'
        json_data = self.get_data()
        self.df = pd.DataFrame({'dates': json_data['dates'],
                                'pcrTestCount': json_data['pcrTestCount'],
                                'serologyTestCount': json_data['serologyTestCount'],
                                'pcrPositiveCount': json_data['pcrPositiveCount'],
                                'serologyPositiveCount': json_data['serologyPositiveCount'],
                                'totalPositiveCount': json_data['totalPositiveCount'],
                                'pcrPositiveCountAraba': json_data['pcrPositiveCountAraba'],
                                'pcrPositiveCountBizkaia': json_data['pcrPositiveCountBizkaia'],
                                'pcrPositiveCountGipuzkoa': json_data['pcrPositiveCountGipuzkoa'],
                                'recoveredCount': json_data['recoveredCount'],
                                'notRecoveredCount': json_data['notRecoveredCount'],
                                'deceasedCount': json_data['deceasedCount'],
                                'icuPeopleCount': json_data['icuPeopleCount'],
                                'r0': json_data['r0'],
                                'by100ThousandPeoplePositiveRateAR': json_data['by100ThousandPeoplePositiveRateAR'],
                                'by100ThousandPeoplePositiveRateBIZ': json_data['by100ThousandPeoplePositiveRateBIZ'],
                                'by100ThousandPeoplePositiveRateGI': json_data['by100ThousandPeoplePositiveRateGI']
                                })
        last_update = json_data['lastUpdateDate']

    def get_data(self):
        response = requests.get(self.path_json)
        data = response.json()
        return data

    def process_data(self):
        pass

    def plot_covid19_pcr_positivos(self, df):
        ax = self.pd.plot_analisis(df=df,
                                   sort_variable=None,
                                   kind='line',
                                   x='date',
                                   y=["age_0_9_Count", "age_10_19_Count", "age_20_29_Count", "age_30_39_Count",
                                      "age_40_49_Count", "age_50_59_Count", "age_60_69_Count", "age_70_79_Count",
                                      "age_80_89_Count", "age_90_X_Count"],
                                   xlabel='Date', ylabel='Infectios per day',
                                   title='Infectios per day', figsize=(40, 20), ylim=[0, 300],
                                   rot=0, stacked=False,
                                   fontsize=10, xlim=None)
        self.plot_fechas_clave(ax)
        plt.show()

    def plot_weekly(self, df):
        ax = self.pd.plot_analisis(df=df,
                                   sort_variable=None,
                                   kind='line',
                                   x='date',
                                   y=["all_infected"],
                                   xlabel='Date', ylabel='Infectios per day',
                                   title='Infectios per day', figsize=(40, 20), ylim=[0, 300],
                                   rot=0, stacked=False,
                                   fontsize=10, xlim=None)
        self.plot_fechas_clave(ax)
        plt.show()

    def plot_fechas_clave(self, ax):
        ax.axvline(self.estado_alarma1, color="red", linestyle="-")
        ax.axvline(self.desescalada_fase0, color="red", linestyle="--")
        ax.axvline(self.desescalada_fase1, color="orange", linestyle="--")
        ax.axvline(self.desescalada_fase2, color="yellow", linestyle="--")
        ax.axvline(self.desescalada_fase3, color="green", linestyle="--")
        ax.axvline(self.restriccion_perimetral1_on, color="black", linestyle="--")
        ax.axvline(self.restriccion_perimetral1_off, color="green", linestyle="--")
        ax.axvline(self.restriccion_perimetral2_on, color="black", linestyle="--")
        ax.axvline(self.restriccion_perimetral2_off, color="green", linestyle="--")


if __name__ == '__main__':
    pandas = Pandas(None)
    covid = Covid19(pandas)
    covid.covid19_pcr_positivos()
