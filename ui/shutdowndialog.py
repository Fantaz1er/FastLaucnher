# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from bin.launcher import *


class UiShutdownDialog:
    def setupUi(self, window, time: int):
        window.setWindowIcon(QtGui.QIcon(":/favicon/favicon.ico"))
        window.setObjectName("window")
        window.setWindowTitle("Выключить компьютер")
        window.setFixedSize(320, 240)
        window.verticalLayout = QtWidgets.QVBoxLayout(window)
        window.verticalLayout.setObjectName("verticalLayout")
        window.widget = QtWidgets.QWidget(window)
        window.widget.setStyleSheet("background-color: #181a1d")
        window.widget.setObjectName("widget")
        window.buttonBox = QtWidgets.QDialogButtonBox(window.widget)
        window.buttonBox.setGeometry(QtCore.QRect(-20, 182, 311, 41))
        window.buttonBox.setStyleSheet("QPushButton {\n"
                                       "background-color: #26272a;\n"
                                       "color: gray;\n"
                                       "font-family: Rubik;\n"
                                       "font-size: 10pt;\n"
                                       "font-weight: bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #df005b;\n"
                                       "color: white;\n"
                                       "}")
        window.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        window.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        window.textBrowser = QtWidgets.QTextBrowser(window.widget)
        window.textBrowser.setGeometry(QtCore.QRect(8, 60, 281, 131))
        window.textBrowser.setStyleSheet("border: none;")
        window.textBrowser.setObjectName("textBrowser")
        window.logo = QtWidgets.QLabel(window.widget)
        window.logo.setGeometry(QtCore.QRect(10, -10, 226, 80))
        window.logo.setStyleSheet("background-color: none;\n"
                                  "border:none;")
        window.logo.setPixmap(QtGui.QPixmap(":/images/FastLauncherLogo.png"))
        window.verticalLayout.addWidget(window.widget)

        window.buttonBox.accepted.connect(lambda: shutdownComputer(time))  # type: ignore
        window.buttonBox.rejected.connect(window.close)  # type: ignore

        window.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                   "type=\"text/css\">\n"
                                   "p, li { white-space: pre-wrap; }\n"
                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                   "font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                   "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                   "font-family:\'Rubik\'; font-size:12pt; font-weight:600; "
                                   "color:#ffffff;\">Вы действительно хотите выключить свой компьютер?<br "
                                   f"/><br /><br />Выключение произойдёт через: {time}"
                                   " секунд.</span></p></body></html>")

        QtCore.QMetaObject.connectSlotsByName(window)
