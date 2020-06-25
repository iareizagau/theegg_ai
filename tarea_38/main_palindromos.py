"""
Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras.
Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000.
Usted debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.
Por ejemplo, si N es 31, entonces la respuesta es 101.
Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.
Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
"""


def main():
    es_palindromo = False
    while True:
        try:
            numero = int(input('Numero entero: '))
            for i in range(numero, 1000000):
                pl = Palindromo(i)
                if pl.palindromo() and pl.es_primo():
                    print('{} es Palindromo de {}'.format(numero, i))
                    es_palindromo = True
                    break
            if es_palindromo is False:
                print('{} no es Palindromo '.format(numero))
            try:
                op = int(input('Seguir? SI (1) NO (anything else)'))
                if op != 1:
                    break

            except Exception as e:
                break

        except Exception as e:
            print('Try again. ERROR {}'.format(e))


class Palindromo:
    def __init__(self, number):
        self.number = number

    def check_valid_number(self):
        if 1 <= self.number <= 1000000:
            not_valid = False
        else:
            print('Error: Number not valid. Try again')
            not_valid = True
        return not_valid

    def palindromo(self):
        self.check_valid_number()
        number_invert = int(''.join(map(str, list(str(self.number))[::-1])))
        if number_invert == self.number:
            return True
        else:
            return False

    def numero_primo(self):
        if self.number < 2:
            return False
        for i in range(2, self.number):
            print(i, self.number)
            if self.number % i == 0:
                return False
        return True

    def es_primo(self):
        # Comprobamos si n es 2 (unico primo par)
        if self.number == 2:
            return True

        # Comprobamos si es menor de 2 o es par
        if self.number < 2 or not self.number % 2:
            return False

        # Comprobamos si es divisible entre cualquier entero impar entre 3 y sqrt(n)
        return not any(self.number % i == 0 for i in range(3, int(self.number ** 0.5) + 1, 2))

    def __del__(self):
        pass


if __name__ == '__main__':
    main()
