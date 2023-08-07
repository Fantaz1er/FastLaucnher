# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QVariantAnimation, QAbstractAnimation, QEvent
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self._animation = QVariantAnimation(
            startValue=QColor("white"),
            endValue=QColor("#898a8c"),
            valueChanged=self._on_value_changed,
            duration=300,
        )
        self._on_value_changed(self._animation.endValue())

    def _on_value_changed(self, color: QColor) -> None:
        self.setStyleSheet(
            """QPushButton{
                font-family: Rubik;
                color: %s;
                background-color: none;
                border: none;
                font-size: 10pt;
                font-weight: bold;
                text-decoration: none;
            }
            """
            % color.name()
        )

    def enterEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(a0)
