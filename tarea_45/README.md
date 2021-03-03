# Búsqueda secuencial y binaria
<div align="center">

| Búsqueda| Definición| Ventajas | Desventajas | Ejemplo |
|:-------:|:---------:|:--------:|:-----------:|:-------:|
|secuencial  |El algoritmo compara uno a uno los elementos del array hasta dar con el elemento en caso del que exista.|El vector no tiene que estar ordenado| Es lento. Más iteraciones |11 iteraciones |
|Binaria|Divide el array para encontrar el elemento|Más eficiente. Menos iteraciones|Tiene que estar ordenado| 4 iteraciones
</div> 
*ejemplo: buscar 874 en [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

<div align="center">

<br></br>
![gif](secuencial_binario.gif)
</div>

# Análisis en Notación Big O
<div align="center">

 ![jpg](plot_num_procesos.jpg)
 </div> 

 En esta gráfica podemos observar que cuando aumentamos el número de elementos en el array la búsqueda secuencial tiene una pendiente mucho más pronunciada que la búsqueda binaria. Esto es, para el mismo número de elementos la búsqueda secuencial tiene que realizar muchas más iteraciones que la búsqueda binaria.

# Referencias
- https://stackabuse.com/sorting-algorithms-in-python/
- https://realpython.com/sorting-algorithms-python/