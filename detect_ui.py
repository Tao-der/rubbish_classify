# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\rubbish_classify\detect_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1100, 844)
        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(980, 550, 75, 41))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(980, 480, 75, 41))
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_preview = QtWidgets.QLabel(self.centralwidget)
        self.label_preview.setGeometry(QtCore.QRect(30, 30, 451, 431))
        self.label_preview.setStyleSheet("background-color: rgb(240, 237, 255);")
        self.label_preview.setText("")
        self.label_preview.setObjectName("label_preview")
        self.label_video = QtWidgets.QLabel(self.centralwidget)
        self.label_video.setGeometry(QtCore.QRect(510, 30, 551, 431))
        self.label_video.setStyleSheet("background-color: rgb(240, 237, 255);")
        self.label_video.setText("")
        self.label_video.setObjectName("label_video")
        self.flag = QtWidgets.QLabel(self.centralwidget)
        self.flag.setGeometry(QtCore.QRect(30, 510, 91, 41))
        self.flag.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag.setAlignment(QtCore.Qt.AlignCenter)
        self.flag.setObjectName("flag")
        self.flag_status = QtWidgets.QLabel(self.centralwidget)
        self.flag_status.setGeometry(QtCore.QRect(170, 510, 91, 41))
        self.flag_status.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_status.setObjectName("flag_status")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(30, 490, 251, 281))
        self.background.setStyleSheet("background-color: rgb(238, 239, 255);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.flag_kehuishou = QtWidgets.QLabel(self.centralwidget)
        self.flag_kehuishou.setGeometry(QtCore.QRect(40, 560, 81, 31))
        self.flag_kehuishou.setFocusPolicy(QtCore.Qt.NoFocus)
        self.flag_kehuishou.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_kehuishou.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_kehuishou.setObjectName("flag_kehuishou")
        self.flag_youhai = QtWidgets.QLabel(self.centralwidget)
        self.flag_youhai.setGeometry(QtCore.QRect(40, 610, 81, 31))
        self.flag_youhai.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_youhai.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_youhai.setObjectName("flag_youhai")
        self.flag_chuyu = QtWidgets.QLabel(self.centralwidget)
        self.flag_chuyu.setGeometry(QtCore.QRect(40, 660, 81, 31))
        self.flag_chuyu.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_chuyu.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_chuyu.setObjectName("flag_chuyu")
        self.flag_qita = QtWidgets.QLabel(self.centralwidget)
        self.flag_qita.setGeometry(QtCore.QRect(40, 710, 81, 31))
        self.flag_qita.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_qita.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_qita.setObjectName("flag_qita")
        self.flag_qita_value = QtWidgets.QLabel(self.centralwidget)
        self.flag_qita_value.setGeometry(QtCore.QRect(170, 710, 81, 31))
        self.flag_qita_value.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_qita_value.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_qita_value.setObjectName("flag_qita_value")
        self.flag_youhai_value = QtWidgets.QLabel(self.centralwidget)
        self.flag_youhai_value.setGeometry(QtCore.QRect(170, 610, 81, 31))
        self.flag_youhai_value.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_youhai_value.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_youhai_value.setObjectName("flag_youhai_value")
        self.flag_chuyu_value = QtWidgets.QLabel(self.centralwidget)
        self.flag_chuyu_value.setGeometry(QtCore.QRect(170, 660, 81, 31))
        self.flag_chuyu_value.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_chuyu_value.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_chuyu_value.setObjectName("flag_chuyu_value")
        self.flag_kehuishou_value = QtWidgets.QLabel(self.centralwidget)
        self.flag_kehuishou_value.setGeometry(QtCore.QRect(170, 560, 81, 31))
        self.flag_kehuishou_value.setFocusPolicy(QtCore.Qt.NoFocus)
        self.flag_kehuishou_value.setStyleSheet("font: 12pt \"Agency FB\";")
        self.flag_kehuishou_value.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_kehuishou_value.setObjectName("flag_kehuishou_value")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(300, 480, 661, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.background.raise_()
        self.pushButton_stop.raise_()
        self.pushButton_start.raise_()
        self.label_preview.raise_()
        self.label_video.raise_()
        self.flag.raise_()
        self.flag_status.raise_()
        self.flag_kehuishou.raise_()
        self.flag_youhai.raise_()
        self.flag_chuyu.raise_()
        self.flag_qita.raise_()
        self.flag_qita_value.raise_()
        self.flag_youhai_value.raise_()
        self.flag_chuyu_value.raise_()
        self.flag_kehuishou_value.raise_()
        self.tableWidget.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "垃圾分类系统"))
        self.pushButton_stop.setText(_translate("mainWindow", "停止"))
        self.pushButton_start.setText(_translate("mainWindow", "开始"))
        self.flag.setText(_translate("mainWindow", "垃圾桶"))
        self.flag_status.setText(_translate("mainWindow", "是否满载"))
        self.flag_kehuishou.setText(_translate("mainWindow", "回收(蓝)"))
        self.flag_youhai.setText(_translate("mainWindow", "有害(红)"))
        self.flag_chuyu.setText(_translate("mainWindow", "厨余(绿)"))
        self.flag_qita.setText(_translate("mainWindow", "其他(灰)"))
        self.flag_qita_value.setText(_translate("mainWindow", "是"))
        self.flag_youhai_value.setText(_translate("mainWindow", "是"))
        self.flag_chuyu_value.setText(_translate("mainWindow", "是"))
        self.flag_kehuishou_value.setText(_translate("mainWindow", "是"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "种类"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "重量"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "数量"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "分类成功与否"))

