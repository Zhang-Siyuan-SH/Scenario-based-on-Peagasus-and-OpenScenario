# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from mainwindows import Ui_MainWindow
from Basescenario import Ui_BaseScenario


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # 父类方法的初始化
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.win_base = QtGui.QMainWindow()
        self.ui_base = Ui_BaseScenario()
        self.user_click()

    def user_click(self):
        self.connect(self.ui_main.BaseButton, QtCore.SIGNAL('clicked()'), self.base_scenario)

    def base_scenario(self):
        self.ui_base.setupUi(self.win_base)
        self.win_base.show()


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
