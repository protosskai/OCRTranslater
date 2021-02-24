from base.baseMainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):

    def __init__(self, MainWindow):
        super().__init__()
        self.mainWindow = MainWindow
        self.setupUi(MainWindow)
        # 初始化界面各个控件
        self.initUI()

    def initUI(self):
        """
        初始化界面的各个控件
        """
        self.cutButton.clicked.connect(self.cutScreen)

    def cutScreen(self):
        print("截图按钮被点击")
