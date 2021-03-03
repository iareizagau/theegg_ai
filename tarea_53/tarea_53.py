poblacion = 600
muestra = 20
seccion_a_N = 200
seccion_b_N = 150
seccion_c_N = 150
seccion_d_N = 100
N_estratos = [seccion_a_N, seccion_b_N, seccion_c_N, seccion_d_N]

N = poblacion
n = muestra
n_muestras = []
for N_estrato in N_estratos:
    n_muestras.append(N_estrato * n / N)
print(f'muestras {sum(n_muestras)}')