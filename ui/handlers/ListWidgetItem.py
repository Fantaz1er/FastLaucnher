from PyQt5 import QtWidgets, QtCore, QtGui


class ListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            endValue=QtGui.QColor("#16171a"),
            startValue=QtGui.QColor("#1f2124"),
            valueChanged=self._on_value_changed,
            duration=500,
        )
        self._update_stylesheet(QtGui.QColor("#16171a"))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalScrollBar().setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.setSpacing(9)

    def _on_value_changed(self, color: QtGui.QColor) -> None:
        self._update_stylesheet(color)

    def _update_stylesheet(self, color: QtGui.QColor) -> None:
        self.setStyleSheet(
            """QListWidget{
                border: none;
            }
            QListWidget::item{
                background: %s;
                color: white;
                height: 75px;
            }
            QListWidget::item:selected{
                border: 2px solid white;
            }
            """
            % color.name()
        )

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(a0)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(a0)
