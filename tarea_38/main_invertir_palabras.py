# -*- coding: utf-8 -*-
"""
Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso.
Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras.
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco
y de la frase invertida.
"""


def main():
    palabras = InvertirPalabras()
    while True:
        try:
            n_frases = int(input('Cantidad de valores que se van a analizar: '))
            palabras.invertir(n_frases)
            try:
                op = int(input('Seguir con otras frases? SI (1) NO (anything else)'))
                if op != 1:
                    break
            except Exception as e:
                break
        except Exception as e:
            print('Value not valid. Try again')


class InvertirPalabras:
    def __init__(self):
        self.n_frases = 0

    def __init__data(self):
        self.frases = []

    def numero_frases(self):
        self.__init__data()
        for i in range(self.n_frases):
            self.frases.append(input('Frase {}: '.format(i+1)))

    def invertir(self, n_frases):
        self.n_frases = n_frases
        self.numero_frases()
        for i, frase in enumerate(self.frases):
            result = ' '.join(map(str, frase.split()[::-1]))
            print('Case #{}: {}'.format(i+1, result))

    def __del__(self):
        pass


if __name__ == '__main__':
    main()
