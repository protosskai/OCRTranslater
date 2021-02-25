from PyQt5 import QtCore, QtWidgets
from MainWindow import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow(app)
    ui.show()
    app.setQuitOnLastWindowClosed(True)
    sys.exit(app.exec_())
