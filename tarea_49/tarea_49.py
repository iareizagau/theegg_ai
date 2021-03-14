class Persona:
    mayor_de_edad = 18

    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print('incorrecto')
        self.__edad = edad

    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()

    def mostrar(self):
        print(f'nombre {self.nombre}, edad {self.edad}, DNI {self.dni}')

    def es_mayor_de_edad(self):
        return self.edad >= self.mayor_de_edad

    def validar_dni(self):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        if len(self.__dni) == 9:
            letraControl = self.__dni[8].upper()
            dni = self.__dni[:8]
            if len(dni) == len([n for n in dni if n in numeros]):
                if tabla[int(dni) % 23] == letraControl:
                    print(f'el dni {self.__dni} es correcto')
                else:
                    print(f'el dni {self.__dni} es incorrecto')


class Cuenta:
    def __init__(self, titular='', cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f'titular {self.titular} cantidad {self.cantidad}')

    def ingresar(self, cantidad):
        self.__cantidad += cantidad
        self.mostrar()

    def retirar(self, cantidad):
        self.__cantidad -= cantidad
        self.mostrar()


if __name__ == '__main__':
    persona = Persona(nombre='Imanol', edad=28, dni='44566583N')
    persona.mostrar()
    cuenta = Cuenta(titular='Imanol', cantidad=1000.0)
    cuenta.ingresar(100)
    cuenta.retirar(50)
