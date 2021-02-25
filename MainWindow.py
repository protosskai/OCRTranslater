import threading
import time
import sys
from base.baseMainWindow import Ui_MainWindow
from tools.system_tools import *
from tools.str_tools import *
from PyQt5 import QtCore
from PyQt5.Qt import QCursor, QMessageBox, QMainWindow
from api.BaiduOCR import *
from ResultWidget import ResultWidget
from api.BaiduTranslate import *


class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        # 初始化类实例变量
        self.app = app
        self.MouseX = 0
        self.MouseY = 0
        self.leftUpX = 0
        self.leftUpY = 0
        self.rightDownX = 0
        self.rightDownY = 0
        # 保存一个翻译子线程的引用
        self.resultThread = None
        # 标记是否应该运行翻译子线程
        self.isTranslating = False
        # 上一张截图的base64字符串
        self.lastStrBase64 = ""
        # 上一次识别出的文字
        self.lastOCRResult = ""
        # 初始化界面各个控件
        self.initUI()
        # 初始化定时器，用来更新UI
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateUI)
        self.timer.setInterval(20)
        self.timer.start()

    def closeEvent(self, event):
        sys.exit()

    def initUI(self):
        """
        初始化界面的各个控件
        """
        self.beginTranslateButton.clicked.connect(self.startTranslate)
        self.stopTranslateButton.clicked.connect(self.stopTranslate)

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

    def get_OCR_result(self):
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
        imgBase64 = qimage2base64(img, "PNG")
        if str(imgBase64) != str(self.lastStrBase64):
            # 保存本次base64结果
            self.lastStrBase64 = imgBase64
            # 调用OCR接口识别文字
            res = get_ocr_result(imgBase64, ocr_map[self.srcLang])
            # 提取识别出的文字
            res_str = ""
            words_result_num = res["words_result_num"]
            for i in range(0, words_result_num):
                res_str += res["words_result"][i]["words"]
            self.lastOCRResult = res_str
            return res_str
        return self.lastOCRResult

    def update_translate_widget(self):
        """
        更新翻译widget
        """
        while self.isTranslating:
            ocrResult = self.get_OCR_result()
            translateResult = get_translate_result(ocrResult, translate_lang_map[self.srcLang],
                                                   translate_lang_map[self.dstLang])
            self.resultWidget.resultLabel.setText(translateResult)
            time.sleep(1)

    def startTranslate(self):
        # 读取截取区域的坐标值
        self.leftUpX = str2int(self.leftUpXEdit.text())
        self.leftUpY = str2int(self.leftUpYEdit.text())
        self.rightDownX = str2int(self.rightDownXEdit.text())
        self.rightDownY = str2int(self.rightDownYEdit.text())
        # 读取源语言和目标语言数据
        self.srcLang = self.srcLangComBox.currentText()
        self.dstLang = self.dstLangComBox.currentText()
        # 检查输入是否有误
        if self.leftUpX is None or self.leftUpY is None or self.rightDownX is None or self.rightDownY is None:
            QMessageBox(QMessageBox.Warning, '警告', '请检查你输入的坐标值是否有误!').exec_()
            return
        # 创建翻译widget
        self.resultWidget = ResultWidget(self.leftUpX, self.leftUpY, self.rightDownX, self.rightDownY, self.srcLang,
                                         self.dstLang, self)
        # 开启翻译线程
        self.isTranslating = True
        # 创建线程，线程内部更新翻译widget
        self.resultThread = threading.Thread(target=self.update_translate_widget)
        self.resultThread.setDaemon(True)
        self.resultThread.start()

    def stopTranslate(self):
        # 关闭翻译线程
        self.isTranslating = False
        # 关闭窗口
        self.resultWidget.close()
        self.resultWidget = None
