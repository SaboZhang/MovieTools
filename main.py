#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: 张涛
@Date: 2020-10-29 16:52:22
@LastEditTime: 2020-11-24 17:57:41
@LastEditors: 张涛
@Description: 一句话描述
@FilePath: /main.py
@世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QStackedLayout
from ui import Ui_MainWindow
from utils.FlowLayout import FlowLayout
from home_page import Ui_Form


class FrameHomePage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class initializeWindow(QMainWindow, Ui_MainWindow):
    """
    初始化窗口UI
    """
    def __init__(self, *args, **kwargs):
        super(initializeWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        # 在这里，可以做一些UI的操作了，或者是点击事件或者是别的
        # 也可以另外写方法，可以改变lable的内容
         # 实例化一个堆叠布局
        self.qsl = QStackedLayout(self.frame)
        # 实例化分页面
        self.home = FrameHomePage()
        # 加入到布局中
        self.qsl.addWidget(self.home)
        # 控制函数
        self.controller()
      
    def controller(self):
        self.homeButton.clicked.connect(self.switch)

    def switch(self):
        sender = self.sender().objectName()

        index = {
            "homeButton": 0,
            "pushButton_blog": 1,
            "pushButton_contact": 2,
        }

        self.qsl.setCurrentIndex(index[sender])


if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./style/UnFrameStyle.qss").read())
    win = initializeWindow()
    win.show()
    sys.exit(app.exec_())
