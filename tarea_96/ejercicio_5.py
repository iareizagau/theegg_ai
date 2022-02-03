import string

txt = input('Introduce una palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in ['a', 'e', 'i', 'o', 'u']:
    count = txt.lower().count(vocal)
    print(f'vocal {vocal} aparece {count} veces')