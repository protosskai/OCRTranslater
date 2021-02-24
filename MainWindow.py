from base.baseMainWindow import Ui_MainWindow
from tools.system_tools import screen_shot_save_qt


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
        self.beginTranslateButton.clicked.connect(self.cutScreen)

    def cutScreen(self):
        screen_shot_save_qt("./1.png")
