"""
https://geekytheory.com/como-subir-tu-propio-paquete-a-pypi
"""
import pandas as pd
import matplotlib.pyplot as plt


class Pandas:
    def __init__(self, ddbb):
        self.db = ddbb

    @staticmethod
    def delete_nan_rows(df):
        return df.dropna()

    @staticmethod
    def select_where(df, conditions):
        for column, data in conditions.items():
            df = df.loc[df[column] == data]

    @staticmethod
    def orderby(df, data):
        return df.sort_values(data)

    @staticmethod
    def group_data(df, data, method):
        if method == 'sum':
            return df.groupby([data]).sum()
        elif method == 'mean':
            return df.groupby([data]).mean()

    @staticmethod
    def rename_column(df, col_old, col_new):
        return df.rename(columns={col_old: col_new})

    @staticmethod
    def select_row_on_condition(df, column, value):
        return df.loc[df[column] == value]

    @staticmethod
    def set_index(df, index_col):
        return df.set_index(index_col)

    @staticmethod
    def merge_two_df(df1, df2, col_name):
        return pd.merge(df1, df2, on=col_name)

    def get_dataframe_db(self, sql):
        return pd.read_sql_query(sql, self.db.connect())

    def read_csv(self, path, delimiter):
        return pd.read_csv(path, delimiter)

    def read_excel(self, path, sheet):
        return pd.read_excel(path, sheet_name=sheet)

    @staticmethod
    def plot_analisis(df, sort_variable,
                      kind, x, y, xlabel, ylabel, title, figsize, ylim, rot, stacked, fontsize, xlim=None):
        if sort_variable is not None:
            df = df.sort_values(sort_variable)
        return df.plot(kind=kind,
                       x=x, y=y,
                       xlabel=xlabel,
                       ylabel=ylabel,
                       title=title,
                       figsize=figsize,
                       xlim=xlim,
                       ylim=ylim,
                       rot=rot,
                       stacked=stacked,
                       fontsize=fontsize)

        # plt.show()
        # plt.savefig(f'plot/{title.replace(" ", "_")}.jpg')
        # plt.close()
