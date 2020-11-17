#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------
# @Author: 张涛
# @Date: 2020-11-06 12:58:04
# @LastEditTime: 2020-11-06 12:58:16
# @LastEditors: 张涛
# @Description: 一句话描述
# @FilePath: \test.py
# @世界上最遥远的距离不是生与死，而是你亲手制造的BUG就在你眼前，你却怎么都找不到她
#----------------------------------------
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
 
class MyWindow(QtWidgets.QWidget):
  def __init__(self):
    super(MyWindow,self).__init__()
    self.resize(900, 600)
    self.myButton = QtWidgets.QPushButton(self)
    self.myButton.setObjectName("myButton")
    self.myButton.setText("click")
    self.myButton.clicked.connect(self.msg)
 
  def msg(self):
    #directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","./")   #起始路径
    #print(directory1)
 
    fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件","./", "All Files (*);;Excel Files (*.xls)")  #设置文件扩展名过滤,注意用双分号间隔
    print(fileName1,filetype)
 
    #files, ok1 = QFileDialog.getOpenFileNames(self,"多文件选择", "./", "All Files (*);;Text Files (*.txt)")
    #print(files,ok1)
 
    #fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存", "./","All Files (*);;Text Files (*.txt)")
 
if __name__=="__main__":
  import sys
  app=QtWidgets.QApplication(sys.argv)
  myshow=MyWindow()
  myshow.msg()
  myshow.show()
  sys.exit(app.exec_())