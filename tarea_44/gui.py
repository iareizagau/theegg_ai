import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from tarea_44 import BigO


class GraphicUserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        path_ui = './tarea_44_gui.ui'
        uic.loadUi(path_ui, self)
        self.setWindowTitle('Tarea 44 - Big O')
        # Buttons
        self.ButtonRun.setEnabled(True)
        self.exit.setEnabled(True)

        self.ButtonRun.clicked.connect(self.btn_run)
        self.exit.clicked.connect(self.btn_exit)

        self.photo.setPixmap(QtGui.QPixmap("./black.JPG"))
        self.photo_2.setPixmap(QtGui.QPixmap("./black.JPG"))

        # Output



    def btn_run(self):
        b = BigO()
        txt = b.main()
        self.textBrowser.setText(txt)
        self.photo.setPixmap(QtGui.QPixmap("./plot_num_procesos.jpg"))
        self.photo_2.setPixmap(QtGui.QPixmap("./plot_time_ejecucion.jpg"))


    @staticmethod
    def btn_exit():
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = GraphicUserInterface()
    GUI.show()
    sys.exit(app.exec_())
