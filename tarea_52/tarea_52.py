import numpy as np


class Listas:
    def __init__(self):
        self.lista = []
        self.break_numeros = 0
        self.break_nombres = '?x?'
        pass

    def solicitar_numeros_lista(self):
        print(f'Introduce {self.break_numeros} para terminar')
        while True:
            num = float(input('Introduce un numero para la listas: '))
            if num != self.break_numeros:
                self.lista.append(num)
                print(f'lista: {self.lista}')
            else:
                print(f'lista: {self.lista}')
                break

    def solicitar_numero(self):
        x = float(input('Introduce un numero: '))
        if x in self.lista:
            index = self.lista.index(x)
            print(f'El numero {x} esta en la lista en la posicion {index} lista: {self.lista}')
            self.lista.pop(index)

        else:
            print(f'El numero {x} no está en la listas {self.lista}')

    def sumatoria_elementos_lista(self):
        sum_lista = 0
        for i, value in enumerate(self.lista):
            sum_lista += value
            print(f'sumatoria de todos los elementos {sum_lista} | lista index {i} value: {value}')
        return sum_lista

    def solicitar_numero2(self):
        print('Crear una lista con los elementos de la listas original que sean menores que el número dado')
        np_lista = np.array(self.lista)
        num = float(input('Introduce nuevo numero para crear una lista: '))
        print(np_lista < num)
        np_lista = np_lista[np_lista < num]
        print(f'np_lista {np_lista}')
        for i, value in enumerate(np_lista):
            print(f'{i}, {value}')

    def generar_tupla(self):
        lista_tupla = []
        lista_distinct = list(set(self.lista))
        for value in lista_distinct:
            lista_tupla.append((value, self.lista.count(value)))

        for i, tupla in lista_tupla:
            print(f'{i}: {tupla}')

    def numeros(self):
        self.solicitar_numeros_lista()
        self.solicitar_numero()
        self.sumatoria_elementos_lista()
        self.solicitar_numero2()
        self.generar_tupla()

    def primaria(self):
        lista_primaria = []
        return self.solicitar_nombres(lista_primaria)

    def secundaria(self):
        lista_secundaria = []
        return self.solicitar_nombres(lista_secundaria)

    def solicitar_nombres(self, lista):
        print(f'Introduce {self.break_nombres} para terminar')
        while True:
            name = input('Introduce un nombre para la listas: ')
            if name != self.break_nombres:
                lista.append(name)
            else:
                break
        return lista

    def nombres(self):
        lista_primaria = self.primaria()
        lista_primaria_copy = lista_primaria.copy()
        lista_secundaria = self.secundaria()

        lista_nombres = []
        lista_nombres.extend(lista_primaria)
        lista_nombres.extend(lista_secundaria)

        self.nombres_sin_repeticiones(lista_nombres)

        for nombre_primaria in lista_primaria:
            if nombre_primaria in lista_secundaria:
                print(f'El nombre {nombre_primaria} se repite entre los alumnos de nivel primario y secundario')
                index = lista_primaria_copy.index(nombre_primaria)
                lista_primaria_copy.pop(index)

        print(f'Los nombres de nivel primario que no se repiten en en los de nivel secundario son \n'
              f' {lista_primaria_copy}')

    def nombres_sin_repeticiones(self, lista_nombres):
        lista_n = set(lista_nombres)
        print(lista_n)


if __name__ == '__main__':
    _list = Listas()
    _list.numeros()
    _list.nombres()
