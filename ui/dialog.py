from PyQt5 import QtWidgets, QtGui, QtCore
from ui.shutdowndialog import UiShutdownDialog
from ui.handlers.WindowMovement import PressEvent


class Dialog(QtWidgets.QDialog, PressEvent):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.dialog_ui = UiShutdownDialog()
        self.dialog_ui.setupUi(self)

        QtGui.QFontDatabase.addApplicationFont(r'..\static\fonts\Rubik-Regular.ttf')
