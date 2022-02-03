asignaturas = ['Matematicas', "Fisica", "Quimica", "Lengua", "Filosofia"]
notas = []

for asignatura in asignaturas:
    nota = input(f'Que nota has sacado en {asignatura}? ')
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f'En {asignaturas[i]} has sacado {notas[i]}')