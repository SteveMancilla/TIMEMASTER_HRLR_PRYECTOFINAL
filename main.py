#NO BORRAR -nnn
import sys
from PyQt5.QtWidgets import QApplication
from login import Ui_MainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    app.exec()