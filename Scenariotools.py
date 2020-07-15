# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from mainwindows import Ui_MainWindow
# from Basescenario import Ui_BaseScenario


class MainWindows(QtGui.QMainWindow, Ui_MainWindow):
    def __int__(self):
        super(MainWindows, self).__init__()  # 父类方法的初始
        self.ui = Ui_MainWindow()  # 利用创建的界面类创建一个对象
        self.ui.setupUi(self)  # 将创建的界面嵌入MainWindow（也即QtGui.QMainWindow）类创建的对象，即self）
    #     self.initUI()
    #
    # def initUI(self):
    #      self.connect(self.BaseButton, QtCore.SIGNAL("clicked()"), self.basescenario())
    #
    # def basescenario(self):
    #     appbase = QtGui.QApplication(sys.argv)
    #     win = QtGui.QMainWindow()
    #     ui = Ui_BaseScenario()
    #     ui.setupUi(win)
    #     win.show()
    #     sys.exit(appbase.exec_())


app = QtGui.QApplication(sys.argv)
main = MainWindows()
main.show()
sys.exit(app.exec_())
