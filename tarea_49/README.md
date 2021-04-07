# Conceptos Programación Orientada a Objetos (POO)
Clase: Tipo de dato que contiene un esquema de métodos y propiedades que se usarán para construir un objeto.
Objeto: Una clase que se ha inicializado, es decir, existe y tiene nombres y apellidos propios en su ejecucioń.
Herencia: Propiedades o métodos que ha recibido una clase hija por parte de una clase padre, esto no quiere decir que vaya a heredar todos los métodos y propiedades, solo aquellos que se le permitan.
Encapsulación: La habilidad de enseñar aquello que solo se pueda mostrar y esconder lo que no nos interesa visibilizar.
Polimorfismo: La capacidad que tiene un objeto para cambiar su rol al mismo tiempo, puede actuar de un rol y en otro rol al mismo tiempo.
* Método
* Propiedad/Atributo
* Instancia
* Constructor
  en python: método __init__. 
  Este método constructor (que permite inicializar un objeto) asigna valores a las propiedades del objeto cuando se construye
* Instancia

Los “Getters” y “Setters” se utilizan en POO para garantizar el principio de la encapsulación de datos.
Claramente el getter se emplea para obtener los datos y el setter para cambiar el valor de los datos. 
Son decoradores y se identifican por tener un @.
Por lo general, estos se usan en Python:

Si queremos añadir una lógica de validación para obtener y establecer un valor.
Para evitar el acceso directo a un atributo de clase (un usuario externo no puede acceder directamente a
las variables privadas ni modificarlas).

Python @property es uno de los decoradores integrados. El propósito principal de cualquier decorador es cambiar 
los métodos o atributos de su clase de tal manera que el usuario de su clase no necesite hacer ningún cambio en su código

## Nueva metodología

## Ejercicios
1. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes
métodos para la clase:
   - Un constructor, donde los datos pueden estar vacíos.
    - Los setters y getters (métodos set y get) para cada uno de los atributos. Hay que validar las entradas de
datos.
    - mostrar(): muestra los datos de la persona.
    - esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad.
2. Crea una clase llamada Cuenta que tendrá los siguientes atributos:
    - titular (que es una persona)
    - cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
    - Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo
ingresando o retirando dinero.
    - mostrar(): muestra los datos de la cuenta.
    - Ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se
hará nada.
    - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.