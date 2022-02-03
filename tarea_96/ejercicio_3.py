txt = input('Introduce una palabra: ')

if list(txt) == [letra for letra in reversed(list(txt))]:
    print('Es palindromo')
else:
    print("No es palindromo")