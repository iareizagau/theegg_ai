import random


def main():
    pikachu = Pokemon('Pikachu', ataque=55)
    jigglypuff = Pokemon('Jigglypuff', ataque=45)
    combate = Combate(pikachu, jigglypuff)
    combate.combate()


class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.vida = 100
        self.ataque = ataque

    def __del__(self):
        pass


class Combate:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def combate(self):
        turno = int(round(random.random()))
        turno_count = 0
        while self.pokemon1.vida > 0 and self.pokemon2.vida > 0:
            if turno == 1:
                self.pokemon2.vida = self.pokemon2.vida - self.pokemon1.ataque
                turno = 0

            elif turno == 0:
                self.pokemon1.vida = self.pokemon1.vida - self.pokemon2.ataque
                turno = 1
            print('turno {} {} vida {} {} vida {}'.format(turno_count,
                                                          self.pokemon1.nombre,
                                                          self.pokemon1.vida,
                                                          self.pokemon2.nombre,
                                                          self.pokemon2.vida))
            turno_count += 1
        self.fin()

    def fin(self):
        if self.pokemon1.vida <= 0:
            print('Ha ganado {}'.format(self.pokemon2.nombre))
        else:
            print('Ha ganado {}'.format(self.pokemon1.nombre))

    def __del__(self):
        pass


if __name__ == '__main__':
    main()
