import time
import matplotlib.pyplot as plt
import pandas as pd


class BigO:
    def __init__(self):
        self.cantidad = 1000000
        self.cantidad_ = []
        self.time_lineal = []
        self.time_constane = []
        self.suma_lineal_ = []
        self.suma_constante_ = []
        pass

    @staticmethod
    def suma_lineal(n):
        suma = 0
        for i in range(1, n + 1):
            suma += i
        return suma

    @staticmethod
    def suma_constante(n):
        return (n / 2) * (n + 1)

    def main(self):
        for i in range(4):
            t0 = time.time()
            self.suma_lineal_.append(self.suma_lineal(self.cantidad))

            t1 = time.time()
            self.suma_constante_.append(self.suma_constante(self.cantidad))

            t2 = time.time()
            self.time_lineal.append(t1 - t0)
            self.time_constane.append(t2 - t1)

            self.cantidad_.append(self.cantidad)
            self.cantidad *= 10

            # print("{} - {}".format(self.suma_lineal_[i], t1-t0))
            # print("{} - {}".format(self.suma_constante_[i], t2 - t1))

        df = pd.DataFrame({'time_lineal': self.time_lineal,
                           'time_constante': self.time_constane,
                           'suma_lineal': self.suma_lineal_,
                           'suma_constante': self.suma_constante_,
                           'cantidad': self.cantidad_})
        # print(df)

        ax = df.plot(kind='line', x='cantidad', y=['suma_lineal', 'suma_constante'],
                     # xlim=(), ylim=(),
                     figsize=(6, 4),
                     title='Nº de procesos',
                     xlabel='cantidad', ylabel='nº procesos',
                     secondary_y='suma_constante', mark_right=True,
                     fontsize=10, rot=0)
        ax.right_ax.set_ylim(0, 1e20)
        plt.savefig('plot_num_procesos.jpg')
        df.plot(kind='line', x='cantidad', y=['time_lineal', 'time_constante'], figsize=(6, 4))
        plt.title('Tiempo de ejecución')
        plt.xlabel('cantidad')
        plt.ylabel('tiempo')
        plt.savefig('plot_time_ejecucion.jpg')
        # plt.show()
        return str(df)
