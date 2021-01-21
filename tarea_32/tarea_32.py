import pandas as pd
import matplotlib.pyplot as plt


class AutomotiveSmartFactory:
    def __init__(self):
        self.path_excel = '32_1.xlsx'
        pass

    def read_excel(self):
        df = pd.read_excel(self.path_excel)
        print(df)


if __name__ == '__main__':
    asf = AutomotiveSmartFactory()
    asf.read_excel()
