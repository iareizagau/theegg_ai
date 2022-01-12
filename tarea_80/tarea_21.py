"""
Tarea 21
Un programa que dado un número introducido entre 0,0001 y 0,9999 (no más de 4 cifras decimales),
obtenga y muestre la correspondiente fracción irreducible.
Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La
fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre
sí.
"""


class Fraction:
    def __init__(self):
        self.number = 0
        self.numerator = 0
        self.denominator = 10000
        self.denominator_ini = 10000

    def ask_number(self):
        not_valid = True
        while not_valid:
            print("Input a number between 0.0001 and 0.9999")
            try:
                self.number = float(input("number: "))
            except Exception as e:
                print('Not valid number. {}'.format(e))
            not_valid = self.check_valid_number()
        self.irreducible_fraction()

    def check_valid_number(self):
        if 0.0001 <= self.number <= 0.9999:
            not_valid = False
            if round(self.number * 10000) % 1 != 0:
                print('Error1. Number not valid. Try again')
                not_valid = True
        else:
            print('Error2. Number not valid. Try again')
            not_valid = True
        return not_valid

    def irreducible_fraction(self):
        mcd = self.max_common_divisior()
        self.denominator = self.denominator_ini/mcd
        self.numerator = round(self.number*self.denominator_ini/mcd)
        print("{}/{} mcd = {}".format(self.numerator, self.denominator, mcd))

    def max_common_divisior(self):
        rest = 0
        mcd = round(self.number*self.denominator_ini)
        while self.denominator_ini > 0:
            rest = self.denominator_ini
            self.denominator_ini = mcd % self.denominator_ini
            mcd = rest
        self.denominator_ini = 10000
        return mcd

    def __del__(self):
        pass
        # print('Delete {} instance'.format(self.__class__.__name__))


if __name__ == "__main__":
    n = Fraction()
    while True:
        n.ask_number()
        if not int(input('Try again? YES (1) NO (0)')):
            break

