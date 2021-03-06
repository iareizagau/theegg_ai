# Tarea 38

## Para ejecutar el programa
* Python3.x y la librería pandas

Pasos a seguir:
1. Crear un entorno virtual
    Pip install virtualenvwrapper-win
    mkvirtualenv --python==path\to\python.exe envname --> C:\usuarios\xxxx\envs

2. Activar entorno virtual
    workon env

3. Instalar librerías
    cd path/to/requermients.txt
    pip install -r requeriments.txt

4. Ejecutar el código
    cd path/to/file.py
    workon env
    python file.py
    
## El biólogo
<div align="center">

>Eres un biólogo que examina secuencias de ADN de formas de vida diferentes. Se te darán dos secuencias de ADN,
y el objetivo es encontrar el conjunto ordenado de bases adyacentes de mayor tamaño que es común en ambos ADNs.
Las secuencias de ADN se darán como conjuntos ordenados de bases de nucleótidos: adenina (abreviado A), citosina (C),
guanina (G) y timina (T):
>ATGTCTTCCTCGA TGCTTCCTATGAC
Para el ejemplo anterior, el resultado es CTTCCT porque que es el conjunto ordenado de bases adyacentes de mayor tamaño
 que se encuentra en ambas formas de vida.
>### Ejemplos de entradas y salidas
| Entrada      | Salida |
| ----------- | ----------- |
| ctgactga actgagc      | actga       |
| cgtaattgcgat cgtacagtagc   | cgta        | 
| ctgggccttgaggaaaactg gtaccagtactgatagt   | actg        |


>![imagen_etl](tarea38_el_biologo.JPG)
 </div>

## Invertir palabras
<div align="center">

>Dada una serie de palabras separadas por espacios, escribir la frase formada por las mismas palabras en orden inverso.
Cada palabra estará formada exclusivamente por letras, y existirá exactamente un espacio entre cada pareja de palabras.
La salida debe ser "Case #" seguido del número de caso, de un símbolo de "dos puntos", de un espacio en blanco
y de la frase invertida.
>### Ejemplos de entradas y salidas
| Entrada      | Salida |
| ----------- | ----------- |
| this is a test      | test a is this       |
| foobar  | foobar   | 
| all your base  | base your all   |

>![imagen_etl](tarea38_invertirpalabras.JPG)
 </div>
 
## Palíndromos
<div align="center">

>Un entero se dice que es un palíndromo si es igual al número que se obtiene al invertir el orden de sus cifras.
Por ejemplo, 79197 y 324423 son palíndromos. En esta tarea se le dará un entero N, 1 <= N <= 1.000.000.
Usted debe encontrar el menor entero M tal que M <= N que es primo y M es un palíndromo N.
Por ejemplo, si N es 31, entonces la respuesta es 101.
Formato de entrada:
Un solo entero N, (1 <= N <= 1.000.000), en una sola línea.
Formato de salida:
Su salida debe consistir en un solo número entero, el más pequeño palíndromo primo mayor que o igual a N.
>### Ejemplos de entradas y salidas
| Entrada      | Salida |
| ----------- | ----------- |
| 31      | 101       |
| 456789  | 1003001   |

>![imagen_etl](tarea38_palindromo.JPG)

 </div>