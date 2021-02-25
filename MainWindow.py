from base.baseMainWindow import Ui_MainWindow
from tools.system_tools import *
from tools.str_tools import *
from PyQt5 import QtCore
from PyQt5.Qt import QCursor, QMessageBox
from api.BaiduOCR import *


class MainWindow(Ui_MainWindow):

    def __init__(self, MainWindow):
        super().__init__()
        self.mainWindow = MainWindow
        self.setupUi(MainWindow)
        # 初始化类实例变量
        self.MouseX = 0
        self.MouseY = 0
        self.leftUpX = 0
        self.leftUpY = 0
        self.rightDownX = 0
        self.rightDownY = 0
        # 初始化界面各个控件
        self.initUI()
        # 初始化定时器，用来更新UI
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.updateUI)
        self.timer.setInterval(20)
        self.timer.start()

    def initUI(self):
        """
        初始化界面的各个控件
        """
        self.beginTranslateButton.clicked.connect(self.cutScreen)

    def updateUI(self):
        self.updateMousePos()

    def updateMousePos(self):
        """
        更新鼠标位置坐标
        """
        self.MouseX = QCursor.pos().x()
        self.MouseY = QCursor.pos().y()
        s = "X坐标：{}；Y坐标：{}".format(self.MouseX, self.MouseY)
        self.MousePos.setText(s)

    def cutScreen(self):
        # 读取截取区域的坐标值
        self.leftUpX = str2int(self.leftUpXEdit.text())
        self.leftUpY = str2int(self.leftUpYEdit.text())
        self.rightDownX = str2int(self.rightDownXEdit.text())
        self.rightDownY = str2int(self.rightDownYEdit.text())
        # 检查输入是否有误
        if self.leftUpX is None or self.leftUpY is None or self.rightDownX is None or self.rightDownY is None:
            QMessageBox(QMessageBox.Warning, '警告', '请检查你输入的坐标值是否有误!').exec_()
            return
        w = self.rightDownX - self.leftUpX
        h = self.rightDownY - self.leftUpY
        # 截取屏幕区域截图
        img = screen_shot_rect_qt(self.leftUpX, self.leftUpY, h, w)
        # 图片转base64
        img = qimage2base64(img, "PNG")
        # 调用OCR接口识别文字
        res = get_ocr_result(img)
        print(res)
