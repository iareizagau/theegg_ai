import logging
import operator
import pandas as pd
import re
import string

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    level='INFO',
    datefmt='%d/%m/%Y %X')

logger = logging.getLogger(__name__)


class Regex:
    def __init__(self):
        self.words = []
        self.characters_non_space = 0
        self.characters = 0
        self.ranking_words = pd.DataFrame(columns=['word', 'frequency', 'regex', 'diferencia'])
        self.txt = ''

    def count_characters(self, txt):
        self.txt = txt
        self.characters = len(re.findall(r".", self.txt))
        self.characters_non_space = len(re.sub(r"\s+", "", self.txt))
        logger.info('número de caracteres {} (sin espacio {})'.format(
            self.characters, self.characters_non_space))

    def count_words(self, txt):
        palabras = len(re.findall(r"\w+", self.txt))
        self.txt = txt
        chars = re.escape(string.punctuation)
        self.words = re.sub(r'['+chars+"«»\n"+']', "", txt)
        self.words = self.words.lower()
        self.words = self.words.split(' ')
        logger.info('número de palabras {}'.format(len(self.words)))

    def ranking_words_frequency(self):
        for word in self.words:
            if word != '' and word not in self.ranking_words.values:
                word_count = self.words.count(word)
                word_count2 = len(re.findall(r'\b{}\b'.format(word), self.txt.lower()))
                df = {'word': word, 'frequency': word_count,
                      'regex': word_count2,
                      'diferencia': word_count - word_count2}
                self.ranking_words = self.ranking_words.append(df, ignore_index=True)
        self.sort_words_by_frequency()

    def sort_words_by_frequency(self):
        self.ranking_words = self.ranking_words.sort_values('frequency', ascending=False)
        logger.info(self.ranking_words)


if __name__ == "__main__":
    text = """
    En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
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
    Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."""
    reg = Regex()
    reg.count_characters(text)
    reg.count_words(text)
    reg.ranking_words_frequency()
