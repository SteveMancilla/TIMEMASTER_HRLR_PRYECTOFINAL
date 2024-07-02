#NO BORRAR
import sys
from PyQt5.QtWidgets import QApplication
from Alarma import Ui_Dialog

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Ui_Dialog()
    window.show()
    app.exec()