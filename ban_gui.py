# Form implementation generated from reading ui file 'ban_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainBan(object):
    def setupUi(self, MainBan):
        MainBan.setObjectName("MainBan")
        MainBan.resize(325, 200)
        MainBan.setMinimumSize(QtCore.QSize(325, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainBan)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.ban_user_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ban_user_btn.setStyleSheet("\n"
"background-color: rgb(255, 85, 127);")
        self.ban_user_btn.setObjectName("ban_user_btn")
        self.gridLayout.addWidget(self.ban_user_btn, 5, 0, 1, 1)
        self.ban_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ban_label.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.ban_label.setObjectName("ban_label")
        self.gridLayout.addWidget(self.ban_label, 0, 0, 1, 1)
        self.name_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 2, 0, 1, 1)
        self.enter_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.enter_label.setObjectName("enter_label")
        self.gridLayout.addWidget(self.enter_label, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainBan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainBan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 18))
        self.menubar.setObjectName("menubar")
        MainBan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainBan)
        self.statusbar.setObjectName("statusbar")
        MainBan.setStatusBar(self.statusbar)

        self.retranslateUi(MainBan)
        QtCore.QMetaObject.connectSlotsByName(MainBan)

    def retranslateUi(self, MainBan):
        _translate = QtCore.QCoreApplication.translate
        MainBan.setWindowTitle(_translate("MainBan", "MainWindow"))
        self.pushButton.setText(_translate("MainBan", "Check username"))
        self.ban_user_btn.setText(_translate("MainBan", "Ban"))
        self.ban_label.setText(_translate("MainBan", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">BAN</span></p></body></html>"))
        self.enter_label.setText(_translate("MainBan", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-style:italic;\">Enter username to ban</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBan = QtWidgets.QMainWindow()
    ui = Ui_MainBan()
    ui.setupUi(MainBan)
    MainBan.show()
    sys.exit(app.exec())