from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, *a0: QColor, parent=None, **kwargs):
        super().__init__(parent)
        self.stylesheet = kwargs['stylesheet'] if kwargs else ''
        self._animation = QVariantAnimation(
            startValue=QColor(a0[1]),
            endValue=QColor(a0[0]),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QColor("gray"), a0[0])
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def _on_value_changed(self, color) -> None:
        foreground = (
            QColor("gray")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
        self._update_stylesheet(foreground, color)

    def _update_stylesheet(self, foreground: QColor, color: QColor) -> None:
        self.setStyleSheet(
            "QPushButton{"
            f"color: {foreground.name()};"
            f"background: {color.name()};"
            "border: none;"
            "text-decoration: none;"
            "border-radius: 0px;"
            "font-family: Rubik;"
            "font-weight: bold;"
            f"{self.stylesheet}"
            "}"
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)
