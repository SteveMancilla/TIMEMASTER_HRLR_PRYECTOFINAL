#NO BORRAR -nnn
import sys
from PyQt5.QtWidgets import QApplication
from Pomodoro import Ui_windowPomodoro

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Ui_windowPomodoro()
    window.show()
    app.exec()