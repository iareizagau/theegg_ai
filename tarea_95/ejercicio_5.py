def _check(a):
    if a.isdigit():
        return int(a) % 2 == 0
    else:
        return True


if __name__ == '__main__':
    check = True
    while check:
        num = input('Introduce un numero impar: ')
        check = _check(num)
    print('Numero impar introducido correctamente')