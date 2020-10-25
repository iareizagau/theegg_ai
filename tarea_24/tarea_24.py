"""
enviado un valor decimal a una función
este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor
analógico digital mediante un programa (software). El hardware lo dejamos para otro día.
"""


def main():
    bn = Binario()
    op = 1
    while op == 1:
        binario, decimal = bn.decimal2binario()
        print('decimal {} binario {}'.format(decimal, binario))
        try:
            op = int(input('Try again? YES (1) NO (anything else): '))
        except Exception as e:
            print('ERROR: {}'.format(e))
            break


class Binario:
    def __init__(self):
        self.resto = []
        self.binaryarray = []
        self.cociente = 0

    def __init__data(self):
        self.resto = []

    def decimal2binario(self):
        self.__init__data()
        decimal = self.check_valid_number()

        while self.cociente >= 2:
            self.resto.append(self.cociente % 2)
            self.cociente = self.cociente // 2

        self.binaryarray = self.resto
        self.binaryarray.append(self.cociente)
        return self.create_binary_num(), decimal

    def check_valid_number(self):
        while True:
            try:
                self.cociente = int(input('Introduce un nº decimal: '))
                return self.cociente
            except Exception as e:
                print('Not valid number. Try again')

    def create_binary_num(self):
        return int(''.join(map(str, self.binaryarray[::-1])))


if __name__ == '__main__':
    main()
