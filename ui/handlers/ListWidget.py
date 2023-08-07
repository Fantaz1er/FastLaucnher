# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import QVariantAnimation, QAbstractAnimation, QEvent, Qt, QRect
from PyQt5.QtGui import QCursor, QColor


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setGeometry(QRect(-5, 100, 250, 450))
        self.setObjectName("game_list")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFocusPolicy(Qt.NoFocus)
        self.verticalScrollBar().setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setSpacing(9)
        self._animation = QVariantAnimation(
            startValue=QColor("#1f2124"),  # type: ignore
            endValue=QColor("#16171a"),  # type: ignore
            valueChanged=self._on_value_changed,  # type: ignore
            duration=500  # type: ignore
        )
        self._on_value_changed(self._animation.endValue())

    def _on_value_changed(self, color: QColor) -> None:
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
            """ % color.name()
        )

    def enterEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Backward)  # type: ignore
        self._animation.start()
        super().enterEvent(a0)

    def leaveEvent(self, a0: QEvent) -> None:
        self._animation.setDirection(QAbstractAnimation.Forward)  # type: ignore
        self._animation.start()
        super().leaveEvent(a0)
