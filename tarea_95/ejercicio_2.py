def check(txt):
    cond1 = False
    cond2 = False
    if len(txt) >= 5:
        cond1 = True
        if len(txt) > 10:
            cond2 = True
    return cond1, cond2


if __name__ == '__main__':
    txt = input('Escribe algo: ')
    cond1, cond2 = check(txt)
    if cond1 and not cond2:
        print('la longitud de texto es mayor o igual que 5 y menor que 10')
    elif cond1 and cond2:
        print('La longitud del texto es mayor que 10')
    elif not cond1:
        print('La longitud de texto es menor que 5')
