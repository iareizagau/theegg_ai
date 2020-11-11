"""
construir una comunicación cifrada entre dos funciones
utilizando el algoritmo del solitario:
1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la
función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings,
enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de
tipo String.
2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo
"""
import string
import random


def main():
    sentence = input('Introduce sentence to encrypt: ')

    solitary = Solitary()
    encrypt = solitary.encrypt(sentence)
    decoded = solitary.decoded()
    adjust = len(sentence) + 5
    print('sentence'.ljust(adjust), 'encrypt'.ljust(adjust), 'decoded'.ljust(adjust))
    print(sentence.ljust(adjust), encrypt.ljust(adjust), decoded.ljust(adjust))


class Solitary:
    def __init__(self):
        self.abc = list(string.ascii_lowercase)
        self.numbers = []
        self.cards = []
        self.cards_original = []
        self.cards_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.trebol_min = 0
        self.trebol_max = 13
        self.diamantes_min = 13
        self.diamantes_max = 26
        self.corazones_min = 26
        self.corazones_max = 39
        self.picas_min = 39
        self.picas_max = 52
        self.comodin = 53
        self.solitario = []
        self.suma = []
        self.modulo = 26
        self.numeros_fin = []
        self.tipo = ''
        self.sentence = ''
        self.new_list = []
        self.last_card = 0
        self.sum_number = 0
        self.result = []
        self.new_list = []
        self.encrypted_sentence = []
        self.clave = 'aaaaaaaaa'

    def init_encryption(self, sentence):
        self.sentence = list(''.join(sentence.replace(' ', '').split()))
        self.create_deck()
        self.shuffle_clave(frase=input('frase clave: '))
        self.cards_original = self.cards.copy()
        self.letters2numbers()

    def init_decoded(self):
        self.sentence = self.encrypted_sentence
        # self.cards = self.cards_original
        self.shuffle_clave()
        self.letters2numbers()

    def find_key(self):
        self.change_joker_a()
        self.change_joker_b()
        self.cut_deck_in_3()
        self.cut_last_card()
        key = self.cut_first_card()
        return key

    def create_deck(self):
        self.cards = [element for element in range(1, 27)]
        self.add_joker()

    def add_joker(self):
        self.cards.append('A')
        self.cards.append('B')

    def shuffle_clave(self, frase=''):
        self.clave = self.clave if len(frase) < 2 else frase
        self.create_deck()
        self.letters2numbers()
        for i in range(len(self.clave)):
            self.change_joker_a()
            self.change_joker_b()
            self.cut_deck_in_3()
            self.cut_last_card()
            self.cut_letter_value(i)
        self.cards.remove('A')
        self.cards.remove('B')
        self.cards.insert(self.numbers_clave[-1], 'A')
        self.cards.insert(self.numbers_clave[-2], 'B')

    # def shuffle_clave_(self):
    #     random.shuffle(self.cards)

    def letters2numbers(self):
        self.numbers = [self.abc.index(letters) + 1 for letters in self.sentence]
        self.numbers_clave = [self.abc.index(letters) + 1 for letters in self.clave]

    def numbers2letters(self):
        self.encrypted_sentence = [self.abc[number - 1] for number in self.new_list]

    def index_joker_a(self):
        return self.cards.index('A')

    def change_joker_a(self):
        index = self.index_joker_a()
        if index == len(self.cards)-1:
            index = 0
        self.cards.pop(index)
        self.cards.insert(index + 1, 'A')

    def index_joker_b(self):
        return self.cards.index('B')

    def change_joker_b(self):
        index = self.index_joker_b()
        self.cards.pop(index)
        if index == len(self.cards)-1:
            index = 0
            self.cards.insert(index + 2, 'B')
        elif index == len(self.cards)-2:
            index = 1
            self.cards.insert(index, 'B')
        else:
            self.cards.insert(index + 2, 'B')

    def cut_deck_in_3(self):
        index_max = max(self.index_joker_a(), self.index_joker_b())
        index_min = min(self.index_joker_a(), self.index_joker_b())

        self.new_list = (self.cards[index_max + 1:])
        self.new_list.extend(self.cards[index_min:index_max + 1])
        self.new_list.extend(self.cards[:index_min])
        self.cards = self.new_list

    def num_1_53(self, card):
        self.sum_number = 0
        if card == 'A' or card == 'B' or card >= 53:
            self.tipo = 'joker'
            self.sum_number = 53
            card_value = 0
        else:
            card_value = self.cards_number[card]
            if self.trebol_min <= card <= self.trebol_max:
                self.tipo = 'trebol'
                self.sum_number = 0
            elif self.diamantes_min < card <= self.diamantes_max:
                self.tipo = 'diamantes'
                self.sum_number = 13
            elif self.corazones_min < card <= self.corazones_max:
                self.tipo = 'corazones'
                self.sum_number = 26
            elif self.picas_min < card <= self.picas_max:
                self.tipo = 'picas'
                self.sum_number = 39
            else:
                self.sum_number = 53
                card_value = 0

        return card_value + self.sum_number

    def new_list_(self, cut):
        self.new_list = self.cards[:cut]
        self.new_list.extend(self.cards[cut:-1])
        self.new_list.append(self.cards[-1])
        self.cards = self.new_list

    def cut_letter_value(self, i):
        cut = self.num_1_53(self.numbers_clave[i])
        self.new_list_(cut)

    def cut_last_card(self):
        cut = self.num_1_53(self.cards[-1])
        self.new_list_(cut)

    def cut_first_card(self):
        try:
            cut = self.num_1_53(self.cards[0])
            card = 53 if cut == 53 else self.cards[cut:][0]
            output = self.num_1_53(card)
        except Exception as e:
            print('Error {}'.format(e))
            output = 0
        return output

    def encrypt(self, sentence):
        self.init_encryption(sentence)
        for i in range(len(self.sentence)):
            self.result.append(self.find_key())
        sum_ = [x + y for x, y in zip(self.numbers, self.result)]
        self.new_list = [item - len(self.abc) if item > len(self.abc) else item for item in sum_]
        self.new_list = [item - len(self.abc) if item > len(self.abc) else item for item in self.new_list]
        self.numbers2letters()
        return ''.join(self.encrypted_sentence)

    def decoded(self):
        self.init_decoded()
        for i in range(len(self.sentence)):
            self.result.append(self.find_key())
        subtract = [x - y for x, y in zip(self.numbers, self.result)]
        self.new_list = [item + len(self.abc) if item < 0 else item for item in subtract]
        self.new_list = [item + len(self.abc) if item < 0 else item for item in self.new_list]
        self.numbers2letters()
        return ''.join(self.encrypted_sentence)

    def __del__(self):
        pass


if __name__ == '__main__':
    main()
