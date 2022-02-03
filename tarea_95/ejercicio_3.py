def is_number(a):
    return type(a) == int or type(a) == float


def tabla_multiplicacion(num):
    if is_number(num) and 0 < num < 99:
        for tabla in range(1, 10):
            print(f'{num} * {tabla} = {num * tabla}')


if __name__ == '__main__':
    num = int(input('Introduce un valor entre 0 y 99: '))
    tabla_multiplicacion(num)
