from base.baseResultWidget import Ui_ResultWidget
from PyQt5.Qt import QWidget


class ResultWidget(Ui_ResultWidget, QWidget):

    def __init__(self, leftUpX, leftUpY, rightDownX, rightDownY, srcLang, dstLang, father):
        super().__init__()
        self.setupUi(self)
        # 设置变量
        self.leftUpX = leftUpX
        self.leftUpY = leftUpY
        self.rightDownX = rightDownX
        self.rightDownY = rightDownY
        self.srcLang = srcLang
        self.dstLang = dstLang
        self.father = father
        # 初始化界面控件
        self.initUI()
        # 显示widget
        self.show()

    def initUI(self):
        pass
