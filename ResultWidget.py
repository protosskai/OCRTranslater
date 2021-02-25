from base.baseResultWidget import Ui_ResultWidget
from PyQt5.Qt import QWidget


class ResultWidget(Ui_ResultWidget, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show()

    def initUI(self):
        pass
