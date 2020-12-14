import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QWidget
from tarea_41.tarea_41_ import Regex


class GraphicUserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.reg = Regex()

        path_ui = './tarea_41_gui.ui'
        uic.loadUi(path_ui, self)
        self.setWindowTitle('Tarea 41 - Expresiones Regulares')

        # Buttons
        self.count_characters.setEnabled(True)
        self.count_words.setEnabled(True)
        self.ranking.setEnabled(True)
        self.exit.setEnabled(True)

        self.count_characters.clicked.connect(self.btn_count_characters)
        self.count_words.clicked.connect(self.btn_count_words)
        self.ranking.clicked.connect(self.btn_ranking)
        self.exit.clicked.connect(self.btn_exit)

        # Output
        txt = """En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
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
        self.textEdit.setText(txt)

    def btn_count_characters(self):
        txt = self.textEdit.toPlainText()
        self.reg.normalize(txt)
        result = self.reg.count_characters()
        self.lcdCharacter.display(result['characters'])

    def btn_count_words(self):
        txt = self.textEdit.toPlainText()
        self.reg.normalize(txt)
        result = self.reg.count_words()
        self.lcdWords.display(result)

    def btn_ranking(self):
        txt = self.textEdit.toPlainText()
        self.reg.normalize(txt)
        result = self.reg.ranking_words_frequency()
        self.result_txt.setText(str(result))

    @staticmethod
    def btn_exit():
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = GraphicUserInterface()
    GUI.show()
    sys.exit(app.exec_())
