from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QRect
from PyQt5 import QtCore


def screen_shot_qt():
    """
    获取桌面的截图，返回img对象
    :return: 桌面截图的img对象(QImage)
    """
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(0).toImage()
    return img


def screen_shot_rect_qt(x, y, h, w):
    """
    获取桌面指定位置的截图，返回img对象
    :param x: 左上横坐标
    :param y: 左上纵坐标
    :param h: 截取区域的高度
    :param w: 截取区域的宽度
    :return: 桌面截图的img对象(QImage)
    """
    img = screen_shot_qt()
    rect = QRect(x, y, w, h)
    img = img.copy(rect)
    return img


def screen_shot_save_qt(output_path):
    """
    获取桌面的截图，并保存到文件
    :param output_path: 图片文件保存路径
    """
    img = screen_shot_qt()
    img.save(output_path)


def screen_shot_rect_save_qt(output_path, x, y, h, w):
    """
    获取指定区域桌面的截图，并保存到文件
    :param output_path: 图片文件保存路径
    :param x: 左上横坐标
    :param y: 左上纵坐标
    :param h: 截取区域的高度
    :param w: 截取区域的宽度
    """
    img = screen_shot_rect_qt(x, y, h, w)
    img.save(output_path)


def qimage2base64(img, format):
    """
    将QImage对象转为base64字符串
    :param img: QImage对象
    :param format: 图片要转换为的格式："PNG", "JPG" ......
    :return: 转换后的字符串
    """
    data = QtCore.QByteArray()
    buf = QtCore.QBuffer(data)
    img.save(buf, format)
    s = bytes(data.toBase64())
    return s
