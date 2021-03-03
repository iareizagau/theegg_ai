import pandas as pd
import numpy as np
from utils_pandas import Pandas
import matplotlib.pyplot as plt
import seaborn as sns

desired_width = 270
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 21)


class AutomotiveSmartFactory:
    def __init__(self, pandas):
        self.pd = pandas
        self.path_excel = '32_1.xlsx'
        self.sheet_espesor_entrada = 'Espesor (Entrada)'
        self.sheet_parametros_prensa = 'Parametros prensa (Entrada)'
        self.sheet_soldadura_entrada = 'Soldadura (Entrada)'
        self.sheet_pieza_estampada = 'Pieza estampada (Salida)'
        self.sheet_pieza_soldada = 'Pieza soldada (salida)'
        self.sheet_datos_soldadura = 'Datos soldadura (Salida)'
        self.sheets = [self.sheet_espesor_entrada,
                       self.sheet_parametros_prensa,
                       self.sheet_soldadura_entrada,
                       self.sheet_pieza_estampada,
                       self.sheet_pieza_soldada,
                       self.sheet_datos_soldadura]
        self.index_col = 'PartId'

    def _read_excel(self):
        df_dict = {}
        for sheet in self.sheets:
            df = self.pd.read_excel(self.path_excel, sheet)
            df = self.clean_df(df)
            # print(f'sheet {sheet}\n{df}')
            df_dict.update({sheet: df})
        return df_dict

    def clean_df(self, df):
        df.columns.str.match("Unnamed")
        df = df.loc[:, ~df.columns.str.match("Unnamed")]
        return self.pd.delete_nan_rows(df)

    def all_sheet_info(self):
        df_dict = self._read_excel()
        df1 = df_dict[self.sheet_espesor_entrada]
        df2 = df_dict[self.sheet_parametros_prensa]
        df3 = df_dict[self.sheet_soldadura_entrada]
        df4 = df_dict[self.sheet_pieza_estampada]
        df5 = df_dict[self.sheet_pieza_soldada]
        df6 = df_dict[self.sheet_datos_soldadura]

        df7 = self.pd.merge_two_df(df1, df2, col_name=self.index_col)
        df8 = self.pd.merge_two_df(df7, df3, col_name=self.index_col)
        df9 = self.pd.merge_two_df(df8, df4, col_name=self.index_col)
        df10 = self.pd.merge_two_df(df9, df5, col_name=self.index_col)
        df11 = self.pd.merge_two_df(df10, df6, col_name=self.index_col)
        # self.print_info(df11)

        df_entrada = df8
        df_salida = self.pd.merge_two_df(df4, df5, col_name=self.index_col)
        df_salida = self.pd.merge_two_df(df_salida, df6, col_name=self.index_col)
        self.print_info(df_entrada)
        self.print_info(df_salida)

        for sheet, df in df_dict.items():
            print(f'### DATAFRAME ### sheet: {sheet}')
            self.show_plots(df, 'pairplot')
            # self.print_info(df)

    @staticmethod
    def print_info(df):
        print(f'shape: {df.shape}')
        print(f'columns: {df.columns}')
        print(f'missing values: \n{df.isnull().sum()}')
        print(f'example data \n{df.head()}')
        print(f'statistics: \n{df.describe()}')
        print(f'corr pearson: \n{df.corr(method="pearson")}')
        print(f'corr kendall: \n{df.corr(method="kendall")}')
        print(f'covarianza: \n{df.cov()}')
        print(f'rolling: \n{df.rolling(window=3).mean()}')

    def show_plots(self, df, type_plot):
        if type_plot == 'pairplot':
            sns.pairplot(df, palette='Blues')
        elif type_plot == 'regression':
            sns.regplot(df)


if __name__ == '__main__':
    pandas = Pandas(None)
    asf = AutomotiveSmartFactory(pandas)
    asf.all_sheet_info()
