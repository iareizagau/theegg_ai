"""
Tarea 22
Usted es un original empresario de Azkoitia, y tiene la brillante idea de abrir una tienda de la leche en la
Plaza del pueblo. Como es una persona muy prudente, desea que la leche que venderá sea
perfectamente natural y fresca, y por esa razón, va a traer unas sanísimas vacas de desde Tolosa.
Dispone de un camión con un cierto límite de peso, y un grupo de vacas disponibles para la venta. Cada
vaca puede tener un peso distinto, y producir una cantidad diferente de leche al día.
Debes elegir qué vacas comprar y llevar en su camión, de modo que pueda maximizar la producción de
leche, observando el límite de peso del camión.
1.- Para este propósito tienes que definir las siguientes entradas:
Entrada: Número total de vacas en la zona de Tolosa que están a la venta.
Entrada: Peso total que el camión puede llevar.
Entrada: Lista de pesos de las vacas.
Entrada: Lista de la producción de leche por vaca, en litros por día.
2.- El algoritmo que programes tiene que calcular la siguiente salida:
Salida: Cantidad máxima de producción de leche se puede obtener."""

import itertools
import pandas as pd


class Lechero:
    def __init__(self):
        self.col = ['id', 'kg_total', 'litros_total']
        self.df = pd.DataFrame(columns=self.col)

    def __init__data(self):
        self.kg_max_camion = float(input("Peso total que el camión puede llevar: "))
        self.n_vacas_venta = int(input('Nº de vacas en venta en Tolosa: '))
        self.lista_vacas = []
        for i in range(self.n_vacas_venta):
            print('vaca {}'.format(i + 1))
            self.lista_vacas.append(dict(id_vaca=i + 1, kg=float(input("Kg: ")), litros=float(input("litros/dia: "))))

    def combinations(self):
        for r in range(0, len(self.lista_vacas) + 1):
            for subset in itertools.combinations(self.lista_vacas, r):
                kg = 0
                litros = 0
                id = ''
                for data in subset:
                    kg += data['kg']
                    litros += data['litros']
                    id += "{}_".format(data['id_vaca'])

                if kg >= self.kg_max_camion:
                    continue
                df_new = pd.DataFrame([[id, kg, litros]], columns=self.col)
                self.df = self.df.append(df_new)

    def select_optimo(self):
        self.__init__data()
        self.combinations()
        x = self.df.loc[self.df['litros_total'] == self.df['litros_total'].max()]
        id_list = x['id'].values[0].split('_')

        print('###########')
        for id in range(len(id_list) - 1):
            print('id_vaca: {}'.format(id_list[id]))
        print('litros leche total: {}'.format(x['litros_total'].values[0]))
        print('peso total: {}'.format(x['kg_total'].values[0]))
        print('###########')


if __name__ == '__main__':
    lechero = Lechero()
    lechero.select_optimo()
