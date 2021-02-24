from PyQt5.QtWidgets import QApplication


def screen_shot_qt():
    """
    获取桌面的截图，返回img对象
    :return: 桌面截图的img对象(QImage)
    """
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(0).toImage()
    return img


def screen_shot_save_qt(output_path):
    """
    获取桌面的截图，并保存到文件
    """
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(0).toImage()
    img.save(output_path)
