# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from mainwindows import Ui_MainWindow
from Basescenario import Ui_BaseScenario
import scenario_classes


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # 父类方法的初始化
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.win_base = QtGui.QMainWindow()
        self.ui_base = Ui_BaseScenario()
        self.ui_base.setupUi(self.win_base)
        self.description = []
        self.user_actions()

    def user_actions(self):
        self.connect(self.ui_main.BaseButton, QtCore.SIGNAL('clicked()'), self.base_scenario)
        self.connect(self.ui_base.pushButton1, QtCore.SIGNAL('clicked()'), self.base_display)

    def base_scenario(self):
        self.win_base.show()

    def base_display(self):
        base_class = scenario_classes.ScenarioClass(int(self.ui_base.lineEdit2.text()),
                                                    [int(self.ui_base.lineEdit3_1.text()),
                                                     int(self.ui_base.lineEdit3_2.text())],
                                                    [int(self.ui_base.lineEdit4_1.text()),
                                                     int(self.ui_base.lineEdit4_2.text())])
        self.description = base_class.catalog()
        self.ui_base.lineEdit5.setText(self.description[4])
        self.ui_base.lineEdit5.setCursorPosition(0)
        self.ui_base.lineEdit6.setText(self.description[5])
        self.ui_base.lineEdit6.setCursorPosition(0)
        self.ui_base.lineEdit7.setText("")
        self.ui_base.lineEdit7.setCursorPosition(0)
        self.ui_base.lineEdit8.setText(self.description[7])
        self.ui_base.lineEdit8.setCursorPosition(0)
        self.ui_base.textEdit.setText(self.description[3])
        self.ui_base.textEdit_2.setText(self.description[6])


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
