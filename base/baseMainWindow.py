# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 284)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.label.setObjectName("label")
        self.MousePos = QtWidgets.QLabel(self.centralwidget)
        self.MousePos.setGeometry(QtCore.QRect(150, 20, 261, 41))
        self.MousePos.setObjectName("MousePos")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 151, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 91, 41))
        self.label_4.setObjectName("label_4")
        self.leftUpXEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.leftUpXEdit.setGeometry(QtCore.QRect(260, 80, 91, 21))
        self.leftUpXEdit.setObjectName("leftUpXEdit")
        self.leftUpYEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.leftUpYEdit.setGeometry(QtCore.QRect(470, 80, 91, 21))
        self.leftUpYEdit.setObjectName("leftUpYEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 70, 91, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 120, 91, 41))
        self.label_6.setObjectName("label_6")
        self.rightDownXEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rightDownXEdit.setGeometry(QtCore.QRect(260, 130, 91, 21))
        self.rightDownXEdit.setObjectName("rightDownXEdit")
        self.rightDownYEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rightDownYEdit.setGeometry(QtCore.QRect(470, 130, 91, 21))
        self.rightDownYEdit.setObjectName("rightDownYEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 120, 91, 41))
        self.label_7.setObjectName("label_7")
        self.beginTranslateButton = QtWidgets.QPushButton(self.centralwidget)
        self.beginTranslateButton.setGeometry(QtCore.QRect(20, 220, 111, 31))
        self.beginTranslateButton.setObjectName("beginTranslateButton")
        self.stopTranslateButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopTranslateButton.setGeometry(QtCore.QRect(170, 220, 111, 31))
        self.stopTranslateButton.setObjectName("stopTranslateButton")
        self.srcLangComBox = QtWidgets.QComboBox(self.centralwidget)
        self.srcLangComBox.setGeometry(QtCore.QRect(130, 170, 111, 21))
        self.srcLangComBox.setObjectName("srcLangComBox")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.srcLangComBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 111, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 160, 111, 41))
        self.label_9.setObjectName("label_9")
        self.dstLangComBox = QtWidgets.QComboBox(self.centralwidget)
        self.dstLangComBox.setGeometry(QtCore.QRect(400, 170, 111, 21))
        self.dstLangComBox.setObjectName("dstLangComBox")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        self.dstLangComBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR翻译器"))
        self.label.setText(_translate("MainWindow", "当前鼠标位置："))
        self.MousePos.setText(_translate("MainWindow", "X坐标：100；Y坐标：100"))
        self.label_3.setText(_translate("MainWindow", "输入截取屏幕区域："))
        self.label_4.setText(_translate("MainWindow", "左上X坐标："))
        self.label_5.setText(_translate("MainWindow", "左上Y坐标："))
        self.label_6.setText(_translate("MainWindow", "右下Y坐标："))
        self.label_7.setText(_translate("MainWindow", "右下X坐标："))
        self.beginTranslateButton.setText(_translate("MainWindow", "开始翻译"))
        self.stopTranslateButton.setText(_translate("MainWindow", "停止翻译"))
        self.srcLangComBox.setItemText(0, _translate("MainWindow", "汉语"))
        self.srcLangComBox.setItemText(1, _translate("MainWindow", "英语"))
        self.srcLangComBox.setItemText(2, _translate("MainWindow", "日语"))
        self.srcLangComBox.setItemText(3, _translate("MainWindow", "韩语"))
        self.srcLangComBox.setItemText(4, _translate("MainWindow", "法语"))
        self.srcLangComBox.setItemText(5, _translate("MainWindow", "西班牙语"))
        self.srcLangComBox.setItemText(6, _translate("MainWindow", "葡萄牙语"))
        self.srcLangComBox.setItemText(7, _translate("MainWindow", "德语"))
        self.srcLangComBox.setItemText(8, _translate("MainWindow", "意大利语"))
        self.srcLangComBox.setItemText(9, _translate("MainWindow", "俄语"))
        self.label_8.setText(_translate("MainWindow", "源语言："))
        self.label_9.setText(_translate("MainWindow", "目标语言："))
        self.dstLangComBox.setItemText(0, _translate("MainWindow", "汉语"))
        self.dstLangComBox.setItemText(1, _translate("MainWindow", "英语"))
        self.dstLangComBox.setItemText(2, _translate("MainWindow", "日语"))
        self.dstLangComBox.setItemText(3, _translate("MainWindow", "韩语"))
        self.dstLangComBox.setItemText(4, _translate("MainWindow", "法语"))
        self.dstLangComBox.setItemText(5, _translate("MainWindow", "西班牙语"))
        self.dstLangComBox.setItemText(6, _translate("MainWindow", "葡萄牙语"))
        self.dstLangComBox.setItemText(7, _translate("MainWindow", "德语"))
        self.dstLangComBox.setItemText(8, _translate("MainWindow", "意大利语"))
        self.dstLangComBox.setItemText(9, _translate("MainWindow", "俄语"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
