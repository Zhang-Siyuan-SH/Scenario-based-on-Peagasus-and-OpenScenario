# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindows.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("VW.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.BaseButton = QtGui.QPushButton(self.centralwidget)
        self.BaseButton.setGeometry(QtCore.QRect(250, 150, 300, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.BaseButton.setFont(font)
        self.BaseButton.setObjectName(_fromUtf8("BaseButton"))
        self.VariantButton = QtGui.QPushButton(self.centralwidget)
        self.VariantButton.setGeometry(QtCore.QRect(250, 250, 300, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.VariantButton.setFont(font)
        self.VariantButton.setObjectName(_fromUtf8("VariantButton"))
        self.LogicalButton = QtGui.QPushButton(self.centralwidget)
        self.LogicalButton.setGeometry(QtCore.QRect(250, 350, 300, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LogicalButton.setFont(font)
        self.LogicalButton.setObjectName(_fromUtf8("LogicalButton"))
        self.ConcreteButton = QtGui.QPushButton(self.centralwidget)
        self.ConcreteButton.setGeometry(QtCore.QRect(250, 450, 300, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ConcreteButton.setFont(font)
        self.ConcreteButton.setObjectName(_fromUtf8("ConcreteButton"))
        self.project = QtGui.QLabel(self.centralwidget)
        self.project.setGeometry(QtCore.QRect(250, 50, 300, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.project.setFont(font)
        self.project.setAlignment(QtCore.Qt.AlignCenter)
        self.project.setObjectName(_fromUtf8("project"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Scenario Generation Tool", None))
        self.BaseButton.setText(_translate("MainWindow", "Base Scenario", None))
        self.VariantButton.setText(_translate("MainWindow", "Variant Scenario", None))
        self.LogicalButton.setText(_translate("MainWindow", "Logical Scenario", None))
        self.ConcreteButton.setText(_translate("MainWindow", "Concrete Scenario", None))
        self.project.setText(_translate("MainWindow", "RHP Scenario", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())