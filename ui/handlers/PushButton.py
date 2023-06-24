from PyQt5 import QtWidgets, QtCore


class PushButton(QtWidgets.QPushButton):
    hover = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        pass

    def enterEvent(self, event):
        self.hover.emit("enterEvent")

    def leaveEvent(self, event):
        self.hover.emit("leaveEvent")
