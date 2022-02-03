asignaturas = ['Matematicas', "Fisica", "Quimica", "Lengua", "Filosofia"]
aprobado = []

for asignatura in asignaturas:
    nota = float(input(f'Que nota has sacado en {asignatura}? '))
    if nota >= 5:
        aprobado.append(asignatura)


for asignatura in aprobado:
    asignaturas.remove(asignatura)
print(f'Tienes que repetir {asignaturas}')