# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FridayGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FridayGUI(object):
    def setupUi(self, FridayGUI):
        FridayGUI.setObjectName("FridayGUI")
        FridayGUI.resize(1989, 1054)
        self.centralwidget = QtWidgets.QWidget(FridayGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1540, 980, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("alternate-background-color: rgb(255, 255, 0);background:transparent;\n"
"border-radius:none;\n"
"color: rgb(124, 124, 124);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1660, 980, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("alternate-background-color: rgb(255, 255, 127);\n"
"background:transparent;\n"
"border-radius:none;\n"
"color: rgb(170, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1991, 1061))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("files/icons/IRONMAN-HUD-2K.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1600, 820, 481, 101))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:maroon;\n"
"font-size:50px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1600, 890, 481, 101))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:dimgrey;\n"
                                       "font-size:50px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 10, 251, 101))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(24)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setAutoFillBackground(False)
        self.textBrowser_3.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:red;\n"
                                       "font-size:30px;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 70, 311, 41))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(24)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setAutoFillBackground(False)
        self.textBrowser_4.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:maroon;\n"
                                       "font-size:50px;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 331, 891))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("files/icons/vertical window.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 220, 261, 351))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:red;\n"
                                       "font-size:30px;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 600, 261, 41))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:orange;\n"
                                       "font-size:30px;")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 660, 261, 351))
        font = QtGui.QFont()
        font.setFamily("DS-Digital")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;\n"
                                       "color:dimgrey;\n"
                                       "font-size:30px;")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1370, 10, 551, 301))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("files/icons/horizontal window.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 910, 761, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("files/icons/sound_wave.gif"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        self.label_2.raise_()
        self.textBrowser_5.raise_()
        self.textBrowser_6.raise_()
        self.textBrowser_7.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        FridayGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(FridayGUI)
        QtCore.QMetaObject.connectSlotsByName(FridayGUI)

    def retranslateUi(self, FridayGUI):
        _translate = QtCore.QCoreApplication.translate
        FridayGUI.setWindowTitle(_translate("FridayGUI", "MainWindow"))
        self.pushButton.setText(_translate("FridayGUI", "RUN"))
        self.pushButton_2.setText(_translate("FridayGUI", "TERMINATE"))
        self.textBrowser_3.setHtml(_translate("FridayGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DS-Digital\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; color:#aa0000;\">friday</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("FridayGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DS-Digital\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#878787;\">developed at euforis</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("FridayGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DS-Digital\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("FridayGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DS-Digital\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("FridayGUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DS-Digital\'; font-size:24pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FridayGUI = QtWidgets.QMainWindow()
    ui = Ui_FridayGUI()
    ui.setupUi(FridayGUI)
    FridayGUI.show()
    sys.exit(app.exec_())
