# -*- coding: utf-8 -*-
"""
Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN,
y el objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.
Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C),
guanina (G) y timina (T):
ATGTCTTCCTCGA TGCTTCCTATGAC
Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño
 que se encuentra en ambas formas de vida.
"""
import pandas as pd


def main():
    # adn1 = 'ATGTCTTCCTCGA'
    # adn2 = 'TGCTTCCTATGAC'
    while True:
        print('Introducir secuencias de adn')
        secuencia_adn = SecuenciasADN(input('Secuencia ADN1: '), input('Secuencia ADN2: '))
        secuencia_adn.comparar()
        try:
            op = int(input('Seguir comparando secuencias de adn? SI (1) NO (anything else)'))
            if op != 1:
                break

        except Exception as e:
            break


class SecuenciasADN:
    def __init__(self, secuencia1, secuencia2):
        self.nucleotidos = 'ATCG'
        self.secuencia1 = secuencia1.upper()
        self.secuencia2 = secuencia2.upper()
        self.col = ['id', 'secuencia', 'len']
        self.df = pd.DataFrame(columns=self.col)

    def adn_valido(self):
        sec = [self.secuencia1, self.secuencia2]
        for i, s in enumerate(sec):
            for nucleotidos in s:
                if nucleotidos not in self.nucleotidos:
                    print('secuencia {} -> {} no válida'.format(i+1, s))
                    return False
        return True

    def comparar(self):
        if self.adn_valido():
            id = 0
            for ini in range(len(self.secuencia1)):
                for fin in range(len(self.secuencia1)-ini-1):
                    sec = self.secuencia1[ini:ini+fin+2]
                    if sec in self.secuencia2:
                        df_new = pd.DataFrame([[id, sec, len(sec)]], columns=self.col)
                        self.df = self.df.append(df_new)
                        id += 1
            self.max_conjunto_ordenado_bases_adyacentes()

    def max_conjunto_ordenado_bases_adyacentes(self):
        max_secuencia = self.df.loc[self.df['len'] == self.df['len'].max()]
        print('RESULTADO: secuencia {} conjunto ordenado de bases adyacentes {}'.format(max_secuencia['secuencia'].values[0],
                                                                                        max_secuencia['len'].values[0]))

    def __del__(self):
        pass


if __name__ == '__main__':
    main()
