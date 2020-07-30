# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
from mainwindows import Ui_MainWindow
from Basescenario import Ui_BaseScenario
import scenario_classes
import image_generate
from excel_input import ExcelInput


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # 父类方法的初始化
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.win_base = QtGui.QMainWindow()
        self.ui_base = Ui_BaseScenario()
        self.ui_base.setupUi(self.win_base)  # 只有setupUi以后，user_actions中才能找到对应的界面元素
        self.description = []
        self.base_initial()
        self.user_actions()

    # 显示初始图片
    def base_initial(self):
        img = image_generate.base_generate(None)
        # img_show = QtGui.QPixmap()
        # img_show.load(img)  # load方法改变的是对象本身，没有返回值
        img_show_item = QtGui.QGraphicsPixmapItem()
        # img_show_item.setPixmap(img_show.scaled(548,  229.9))
        img_show_item.setPixmap(QtGui.QPixmap(img).scaled(548,  229.9))
        """上述语句中QtGui.QPixmap(img).scaled(548,  229.9)的作用是加载图片，并自定义图片展示尺寸,
        上述语句的效果相当于上面注释掉的三句"""
        scene_img = QtGui.QGraphicsScene()
        scene_img.addItem(img_show_item)
        self.ui_base.graphicsView.setScene(scene_img)

    def user_actions(self):
        self.connect(self.ui_main.BaseButton, QtCore.SIGNAL('clicked()'), self.base_scenario)
        self.connect(self.ui_base.pushButton1, QtCore.SIGNAL('clicked()'), self.base_display)
        self.connect(self.ui_base.pushButton1, QtCore.SIGNAL('clicked()'), self.base_graph_display)
        self.connect(self.ui_base.pushButton2, QtCore.SIGNAL('clicked()'), self.excel_input_click)

    def base_scenario(self):
        self.win_base.show()

    # 单独定义一个函数，而不是在第41行的语句中
    def excel_input_click(self):
        input_click = ExcelInput(self.description)
        input_click.excel_write()

    def base_display(self):
        base_class = scenario_classes.ScenarioClass(int(self.ui_base.lineEdit2.text()),
                                                    [int(self.ui_base.lineEdit3_1.text()),
                                                     int(self.ui_base.lineEdit3_2.text())],
                                                    [int(self.ui_base.lineEdit4_1.text()),
                                                     int(self.ui_base.lineEdit4_2.text())])
        self.description = base_class.catalog()  # base_class是一个对象，运行其catalog方法才能得到描述
        self.ui_base.lineEdit5.setText(self.description[4])
        self.ui_base.lineEdit5.setCursorPosition(0)
        self.ui_base.lineEdit6.setText(self.description[5])
        self.ui_base.lineEdit6.setCursorPosition(0)  # 使文本从最左侧开头开始显示
        self.ui_base.lineEdit7.setText("")
        self.ui_base.lineEdit7.setCursorPosition(0)
        self.ui_base.lineEdit8.setText(self.description[7])
        self.ui_base.lineEdit8.setCursorPosition(0)
        self.ui_base.textEdit.setText(self.description[3])
        self.ui_base.textEdit_2.setText(self.description[6])

    def base_graph_display(self):
        v_position = [[2, 2], [3, int(self.ui_base.lineEdit2.text())], [int(self.ui_base.lineEdit3_1.text()),
                                                                        int(self.ui_base.lineEdit3_2.text())], [int(self.ui_base.lineEdit4_1.text()),
                                                                                                                int(self.ui_base.lineEdit4_2.text())]]
        img = image_generate.base_generate(self.description[0], v_position)
        img_show_item = QtGui.QGraphicsPixmapItem()
        img_show_item.setPixmap(QtGui.QPixmap(img).scaled(548, 229.9))
        scene_img = QtGui.QGraphicsScene()
        scene_img.addItem(img_show_item)
        self.ui_base.graphicsView.setScene(scene_img)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
