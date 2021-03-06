# Expresiones Regulares o Regex

Mediante técnicas de Regex calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso
del siguiente texto. La aplicación debe servir para cualquier otro texto.

>"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."



# Pasos para resolver la tarea
>![imagen_etl](diagrama_flujo_tarea_41.png)

### Para ejecutar el código
    1. Descargar la carpeta tarea_41
    
    2. Crear un entorno virtual
       Pip install virtualenvwrapper-win
       mkvirtualenv --python==path\to\python.exe envname --> C:\usuarios\xxxx\envs

    3. Activar entorno virtual
       workon env

    4. Instalar librerías
       cd path/to/requermients.txt
       pip install -r requeriments.txt
 
    5. Ejecutar el código
       cd path/to/gui.py
       workon env
       python gui.py


### Herramientas para probar sintaxis para expresiones regulares
* https://regex101.com/
* https://www.online-toolz.com/langs/es/tool-es-regexp-editor.html
* https://www.metriplica.com/informes-y-estudios-de-analitica-digital/recursos-herramientas-deanalitica/expresiones-regulares/

## Expresiones Regulares
* **.** Representa cualquier caracter excepto el salto de línea
* **\w** Representa cualquier letra o número
* **\W** Representa cualquier caracter que no sea una letra o un numero.
* **\d** Representa cualquier numero del 0 al 9
* **\D** Representa cualquier caracter que no sea un numero del 0 al 9
* **\s** Representa un espacio en blanco
* **\S** Representa cualquier caracter que no sea un espacio en blanco.
* **$** Representa que ahí finaliza el texto, por ejemplo la expresión com$ busca que com sea lo último en el texto. Este caracter solo puede usarse al final de la expresión regular.
* **^** Representa el inicio del texto, por ejemplo la expresión ^hola busca que el texto inicie con hola, este caracter solo puede usarse al inicio de la expresión regular.
* **\b** Representa que ahí inicia o finaliza una palabra, por ejemplo la expresión 
* **\b[A-Z][a-z]** busca palabras que inicien con una letra mayúscula y luego lleven cualquier cantidad de letras minúsculas. 
* **\w*os\b** busca palabras que finalicen en os.

### Expresiones Regulares usados en la tarea:

<div align="center">

| Funcion                       | Expresión                                   |
| :---------------------------- | :------------------------------------------ |
| **Encontrar carácteres**      | **re.findall(r".", txt)**                   |
| **Carácteres sin espacios**   | **re.sub(r"\s+", "", txt)**                 |
| **Palabras**                  | **re.findall(r"\w+", txt)**                 |
| **Contar palabras repetidas** | **re.findall(r'\b{}\b'.format(word), txt)** |

</div>