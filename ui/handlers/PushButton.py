# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation, QEvent
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, *a0: str, parent=None, **kwargs):
        super().__init__(parent)
        self.stylesheet = kwargs['stylesheet'] if kwargs else ''
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self._animation = QVariantAnimation(
            startValue=QColor(a0[1]),
            endValue=QColor(a0[0]),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._on_value_changed(self._animation.endValue())

    def _on_value_changed(self, color: QColor) -> None:
        foreground = (
            QColor("gray")
            if self._animation.direction() == QAbstractAnimation.Forward
            else QColor("white")
        )
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

    def enterEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(a0)
