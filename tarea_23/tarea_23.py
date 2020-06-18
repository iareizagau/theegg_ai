"""
construir una comunicación cifrada entre dos funciones
utilizando el algoritmo del solitario:
1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la
función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings,
enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de
tipo String.
2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo
"""
import numpy as np

def main():
    # frase = list(input('Escribe una frase: '))
    frase = ['A', 7, 2, 'B', 9, 4, 1]
    frase = [3, 'A', 'B', 8, 9, 6]
    frase = [2, 4, 6, 'B', 5, 8, 7, 1, 'A', 3, 9]
    frase = ['B', 5, 8, 7, 1, 'A', 3, 9]
    frase = 'hola imanol'
    solitario = Solitario()
    solitario.cifrado(frase)
    pass


class Solitario:
    def __init__(self):
        self.abc = list("abcdefghijklmnñopqrstuvxyz")
        self.numeros = []
        self.baraja = []
        self.trebol = 0
        self.diamantes = 13
        self.corazones = 26
        self.picas = 39
        self.comodin = 53
        self.solitario = []
        self.suma = []
        self.modulo = 26
        self.numeros_fin = []
        self.tipo = ''

    def cifrado(self, frase):
        self.baraja = list(''.join(frase.lower().split()))
        print(self.baraja)
        self.letras2numeros()
        # self.intercambiar_comodin_A()
        # self.intercambiar_comodin_B()
        self.cortar_barra_en_3()

    def letras2numeros(self):
        self.numeros = [self.abc.index(letra)+1 for letra in self.baraja]

        print(self.numeros)
        print(len(self.baraja), len(self.numeros))

    def numeros2letras(self):
        frase_fin = [self.abc[numero-1] for numero in self.numeros_fin]

    def sumar_original_solitario(self):
        self.suma = np.array(self.numeros) + np.array(self.solitario)
        suma_bool = self.suma > self.modulo
        self.suma = self.suma - suma_bool + self.modulo


    def encuentra_comodin_A(self):
        return self.baraja.index('A')

    def intercambiar_comodin_A(self):
        index = self.encuentra_comodin_A()
        self.baraja.pop(index)
        self.baraja.insert(index + 1, 'A')
        print(self.baraja)

    def encuentra_comodin_B(self):
        return self.baraja.index('B')

    def intercambiar_comodin_B(self):
        index = self.encuentra_comodin_B()
        self.baraja.pop(index)
        self.baraja.insert(index + 2, 'B')
        print(self.baraja)

    def cortar_barra_en_3(self):
        index_max = max(self.encuentra_comodin_A(), self.encuentra_comodin_B())
        index_min = min(self.encuentra_comodin_A(), self.encuentra_comodin_B())
        bar = []
        bar.extend(self.baraja[index_max+1:])
        bar.extend(self.baraja[index_min:index_max+1])
        bar.extend(self.baraja[:index_min])
        print(bar)
        pass

    def ultima_carta(self):
        return self.baraja[-1]

    def num_1_53(self, carta):
        sum = 0
        if carta == ('A' or 'B'):
            self.tipo = 'comodin'
            sum = 53
        if 0 <= carta <= 13:
            self.tipo = 'trebol'
            sum = 0
        elif 13 < carta <= 26:
            self.tipo = 'diamantes'
            sum = 13
        elif 26 < carta <= 39:
            self.tipo = 'corazones'
            sum = 26
        elif 39 < carta <= 52:
            self.tipo = 'picas'
            sum = 39

        return self.ultima_carta() + sum

    def cortar_carta_ulitma(self):
        corte = self.num_1_53(self.ultima_carta())
        a = self.baraja[:corte]

    def primera_carta(self):
        return self.baraja[0]

    def corte_carta_primera(self):
        corte = self.num_1_53(self.primera_carta())
        a = self.baraja[:corte]


    def descifrado(self):
        pass


if __name__ == '__main__':
    main()
