def suma(a, b):
    if is_number(a) and is_number(b):
        return a + b
    else:
        return 'valores incorrectos'


def resta(a, b):
    if is_number(a) and is_number(b):
        return a - b
    else:
        return 'valores incorrectos'


def producto(a, b):
    if is_number(a) and is_number(b):
        return a * b
    else:
        return 'valores incorrectos'


def division(a, b):
    if is_number(a) and is_number(b):
        return a / b
    else:
        return 'valores incorrectos'


def is_number(a):
    return type(a) == int or type(a) == float


def is_zero(a):
    return a == 0
