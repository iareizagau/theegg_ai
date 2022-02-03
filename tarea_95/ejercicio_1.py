def check(a, b):
    if a == b:
        print(f'Dos numeros iguales {a} = {b}')

    if a != b:
        print(f'Dos numeros diferentes {a} != {b}')

    if a > b:
        print(f'{a} es mayor que {b}')

    if b >= a:
        print(f'{b} es mayor o igual que {a}')


if __name__ == '__main__':
    num1 = input('Introduce numero 1: ')
    num2 = input('Introduce numero 2: ')
    check(num1, num2)