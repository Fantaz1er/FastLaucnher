from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QVariantAnimation(
            startValue=QColor("white"),
            endValue=QColor("#898a8c"),
            valueChanged=self._on_value_changed,
            duration=300,
        )
        self._update_stylesheet(QColor("#898a8c"))
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color) -> None:
        self._update_stylesheet(color)

    def _update_stylesheet(self, color) -> None:
        self.setStyleSheet(
            """QPushButton{
                font-family: Rubik;
                color: %s;
                background-color: none;
                border: none;
                font-size: 9pt;
                font-weight: bold;
                text-decoration: none;
            }
            """
            % color.name()
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)
