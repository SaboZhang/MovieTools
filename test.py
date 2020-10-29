#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------
# @Author: 张涛
# @Date: 2020-10-29 16:52:22
# @LastEditTime: 2020-10-29 16:57:34
# @LastEditors: 张涛
# @Description: 程序启动主入口测试
# @FilePath: \test.py
# @世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
#----------------------------------------

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow 


class initializeWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(initializeWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 初始化ui
        # 在这里，可以做一些UI的操作了，或者是点击事件或者是别的
        # 也可以另外写方法，可以改变lable的内容
        
 
 
if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    win = initializeWindow()
    win.show()
    sys.exit(app.exec_())

