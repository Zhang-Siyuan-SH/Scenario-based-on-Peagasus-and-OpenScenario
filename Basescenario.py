# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Basescenario.ui'
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

class Ui_BaseScenario(object):
    def setupUi(self, BaseScenario):
        BaseScenario.setObjectName(_fromUtf8("BaseScenario"))
        BaseScenario.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        BaseScenario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("VW.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BaseScenario.setWindowIcon(icon)
        BaseScenario.setInputMethodHints(QtCore.Qt.ImhPreferLowercase)
        self.centralwidget = QtGui.QWidget(BaseScenario)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.lineEdit1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(240, 100, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setInputMask(_fromUtf8(""))
        self.lineEdit1.setText(_fromUtf8(""))
        self.lineEdit1.setReadOnly(True)
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(530, 310, 441, 41))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 100, 200, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 140, 220, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.lineEdit2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(240, 140, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit2"))
        self.label4 = QtGui.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(10, 230, 220, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.lineEdit3_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit3_1.setGeometry(QtCore.QRect(60, 270, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit3_1.setFont(font)
        self.lineEdit3_1.setObjectName(_fromUtf8("lineEdit3_1"))
        self.lineEdit3_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit3_2.setGeometry(QtCore.QRect(240, 270, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit3_2.setFont(font)
        self.lineEdit3_2.setObjectName(_fromUtf8("lineEdit3_2"))
        self.label4_1 = QtGui.QLabel(self.centralwidget)
        self.label4_1.setGeometry(QtCore.QRect(20, 270, 40, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label4_1.setFont(font)
        self.label4_1.setObjectName(_fromUtf8("label4_1"))
        self.label4_2 = QtGui.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(200, 270, 40, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label4_2.setFont(font)
        self.label4_2.setObjectName(_fromUtf8("label4_2"))
        self.label5_2 = QtGui.QLabel(self.centralwidget)
        self.label5_2.setGeometry(QtCore.QRect(200, 340, 40, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label5_2.setFont(font)
        self.label5_2.setObjectName(_fromUtf8("label5_2"))
        self.lineEdit4_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit4_2.setGeometry(QtCore.QRect(240, 340, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit4_2.setFont(font)
        self.lineEdit4_2.setObjectName(_fromUtf8("lineEdit4_2"))
        self.label5 = QtGui.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(10, 300, 220, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label5.setFont(font)
        self.label5.setObjectName(_fromUtf8("label5"))
        self.lineEdit4_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit4_1.setGeometry(QtCore.QRect(60, 340, 113, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit4_1.setFont(font)
        self.lineEdit4_1.setObjectName(_fromUtf8("lineEdit4_1"))
        self.label5_1 = QtGui.QLabel(self.centralwidget)
        self.label5_1.setGeometry(QtCore.QRect(20, 340, 40, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label5_1.setFont(font)
        self.label5_1.setObjectName(_fromUtf8("label5_1"))
        self.pushButton2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(190, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(20, 470, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName(_fromUtf8("pushButton3"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(420, 21, 551, 231))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label6 = QtGui.QLabel(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(420, 270, 100, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setAutoFillBackground(False)
        self.label6.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204);"))
        self.label6.setFrameShape(QtGui.QFrame.NoFrame)
        self.label6.setObjectName(_fromUtf8("label6"))
        self.label7 = QtGui.QLabel(self.centralwidget)
        self.label7.setGeometry(QtCore.QRect(530, 270, 440, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setAutoFillBackground(False)
        self.label7.setStyleSheet(_fromUtf8("background-color: rgb(204, 204, 204);"))
        self.label7.setFrameShape(QtGui.QFrame.NoFrame)
        self.label7.setObjectName(_fromUtf8("label7"))
        self.label8 = QtGui.QLabel(self.centralwidget)
        self.label8.setGeometry(QtCore.QRect(420, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label8.setFont(font)
        self.label8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label8.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label8.setFrameShape(QtGui.QFrame.Box)
        self.label8.setLineWidth(1)
        self.label8.setObjectName(_fromUtf8("label8"))
        self.lineEdit5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(530, 360, 441, 21))
        self.lineEdit5.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
""))
        self.lineEdit5.setReadOnly(True)
        self.lineEdit5.setObjectName(_fromUtf8("lineEdit5"))
        self.lineEdit6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(530, 390, 441, 21))
        self.lineEdit6.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
""))
        self.lineEdit6.setReadOnly(True)
        self.lineEdit6.setObjectName(_fromUtf8("lineEdit6"))
        self.lineEdit7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit7.setGeometry(QtCore.QRect(530, 420, 441, 21))
        self.lineEdit7.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
""))
        self.lineEdit7.setReadOnly(True)
        self.lineEdit7.setObjectName(_fromUtf8("lineEdit7"))
        self.lineEdit8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit8.setGeometry(QtCore.QRect(530, 500, 441, 21))
        self.lineEdit8.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
""))
        self.lineEdit8.setReadOnly(True)
        self.lineEdit8.setObjectName(_fromUtf8("lineEdit8"))
        self.label9 = QtGui.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(420, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label9.setFont(font)
        self.label9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label9.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label9.setFrameShape(QtGui.QFrame.Box)
        self.label9.setLineWidth(1)
        self.label9.setObjectName(_fromUtf8("label9"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(530, 450, 441, 41))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label10 = QtGui.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(420, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label10.setFont(font)
        self.label10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label10.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label10.setFrameShape(QtGui.QFrame.Box)
        self.label10.setLineWidth(1)
        self.label10.setObjectName(_fromUtf8("label10"))
        self.label11 = QtGui.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(420, 390, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label11.setFont(font)
        self.label11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label11.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label11.setFrameShape(QtGui.QFrame.Box)
        self.label11.setLineWidth(1)
        self.label11.setObjectName(_fromUtf8("label11"))
        self.label12 = QtGui.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(420, 420, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label12.setFont(font)
        self.label12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label12.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label12.setFrameShape(QtGui.QFrame.Box)
        self.label12.setLineWidth(1)
        self.label12.setObjectName(_fromUtf8("label12"))
        self.label13 = QtGui.QLabel(self.centralwidget)
        self.label13.setGeometry(QtCore.QRect(420, 500, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label13.setFont(font)
        self.label13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label13.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label13.setFrameShape(QtGui.QFrame.Box)
        self.label13.setLineWidth(1)
        self.label13.setObjectName(_fromUtf8("label13"))
        BaseScenario.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BaseScenario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BaseScenario.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BaseScenario)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BaseScenario.setStatusBar(self.statusbar)

        self.retranslateUi(BaseScenario)
        QtCore.QMetaObject.connectSlotsByName(BaseScenario)

    def retranslateUi(self, BaseScenario):
        BaseScenario.setWindowTitle(_translate("BaseScenario", "Base Scenario", None))
        self.pushButton1.setText(_translate("BaseScenario", "Generate", None))
        self.label1.setText(_translate("BaseScenario", "Base Scenario", None))
        self.lineEdit1.setPlaceholderText(_translate("BaseScenario", "Default : 2", None))
        self.label2.setText(_translate("BaseScenario", "Ego car start position:", None))
        self.label3.setText(_translate("BaseScenario", "Ego car end position(lane):", None))
        self.lineEdit2.setPlaceholderText(_translate("BaseScenario", "Range [1,3]", None))
        self.label4.setText(_translate("BaseScenario", "Object car start position:", None))
        self.lineEdit3_1.setPlaceholderText(_translate("BaseScenario", "Range [1,4]", None))
        self.lineEdit3_2.setPlaceholderText(_translate("BaseScenario", "Range [1,4]", None))
        self.label4_1.setText(_translate("BaseScenario", "X :", None))
        self.label4_2.setText(_translate("BaseScenario", "Y :", None))
        self.label5_2.setText(_translate("BaseScenario", "Y :", None))
        self.lineEdit4_2.setPlaceholderText(_translate("BaseScenario", "Range [1,4]", None))
        self.label5.setText(_translate("BaseScenario", "Object car end position:", None))
        self.lineEdit4_1.setPlaceholderText(_translate("BaseScenario", "Range [1,4]", None))
        self.label5_1.setText(_translate("BaseScenario", "X :", None))
        self.pushButton2.setText(_translate("BaseScenario", "Export to excel", None))
        self.pushButton3.setText(_translate("BaseScenario", "Export all to excel", None))
        self.label6.setText(_translate("BaseScenario", "Key", None))
        self.label7.setText(_translate("BaseScenario", "Value", None))
        self.label8.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">Description</p></body></html>", None))
        self.label9.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">L4</p></body></html>", None))
        self.label10.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">L1</p></body></html>", None))
        self.label11.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">L2</p></body></html>", None))
        self.label12.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">L3</p></body></html>", None))
        self.label13.setText(_translate("BaseScenario", "<html><head/><body><p align=\"center\">L5</p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QMainWindow()
    ui = Ui_BaseScenario()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())