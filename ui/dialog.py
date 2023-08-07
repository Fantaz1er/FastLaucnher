# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore

from ui.handlers.WindowMovement import PressEvent
from ui.shutdowndialog import UiShutdownDialog


class Dialog(QtWidgets.QDialog, PressEvent):
    def __init__(self, time: int, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.dialog_ui = UiShutdownDialog()
        self.dialog_ui.setupUi(self, time)

        QtGui.QFontDatabase.addApplicationFont(r'..\static\fonts\Rubik-Regular.ttf')
