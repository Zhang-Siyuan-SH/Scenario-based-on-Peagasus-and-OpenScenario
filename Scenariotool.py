# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from mainwindows import Ui_MainWindow
from Basescenario import Ui_BaseScenario


class MainWindow(QtGui.QMainWindow):
    def __int__(self):
        super(MainWindow, self).__init__()  # 父类方法的初始
        self.user_clicked()

    def user_clicked(self):
        self.connect(self.BaseButton, QtCore.SIGNAL('clicked()'), self.base_scenario())

    @staticmethod
    def base_scenario():
        # app_base = QtGui.QApplication(sys.argv)
        win_base = QtGui.QMainWindow()
        ui_base = Ui_BaseScenario()
        ui_base.setupUi(win_base)
        win_base.show()
        # sys.exit(app_base.exec_())


app = QtGui.QApplication(sys.argv)
main = MainWindow()
ui = Ui_MainWindow()  # 利用创建的界面类创建一个对象
ui.setupUi(main)  # 将创建的界面嵌入MainWindow（也即QtGui.QMainWindow）类创建的对象）
main.show()
sys.exit(app.exec_())
