# -*- coding: utf-8 -*-
import re
import webbrowser
import shelve
import os
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets

import ui.res_rc  # type: ignore
from bin import launcher
from bin import win
from ui.dialog import Dialog
from ui.handlers import WindowMovement, PushButton, PushButtonHead, ListWidget


class UiFastLauncher(QtWidgets.QWidget, WindowMovement.PressEvent):
    TIME = 5
    font = QtGui.QFont()
    font.setFamily("Rubik")
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.setFixedSize(950, 650)
        self.setWindowIcon(QtGui.QIcon(":/favicon/favicon.ico"))

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setStyleSheet("QScrollBar:vertical {\n"
                           "    margin: 10px 0 15px 0;\n"
                           "    width: 4px;\n"
                           " }\n"
                           "\n"
                           "/*  HANDLE BAR VERTICAL */\n"
                           "QScrollBar::handle:vertical {    \n"
                           "    background-color: rgb(80, 80, 122);\n"
                           "    min-height: 30px;\n"
                           "    border-radius: 2px;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:vertical:hover{    \n"
                           "    background-color: rgb(255, 0, 127);\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:vertical:pressed {    \n"
                           "    background-color: rgb(185, 0, 92);\n"
                           "}\n"
                           "\n"
                           "/* BTN TOP - SCROLLBAR */\n"
                           "QScrollBar::sub-line:vertical {\n"
                           "    border: none;\n"
                           "    background-color: none;\n"
                           "    height: 15px;\n"
                           "    border-top-left-radius: 7px;\n"
                           "    border-top-right-radius: 7px;\n"
                           "    subcontrol-position: top;\n"
                           "    subcontrol-origin: margin;\n"
                           "}\n"
                           "QScrollBar::sub-line:vertical:hover {    \n"
                           "    background-color: none;\n"
                           "}\n"
                           "QScrollBar::sub-line:vertical:pressed {    \n"
                           "    background-color: none;\n"
                           "}\n"
                           "\n"
                           "/* BTN BOTTOM - SCROLLBAR */\n"
                           "QScrollBar::add-line:vertical {\n"
                           "    border: none;\n"
                           "    background-color: none;\n"
                           "    height: 15px;\n"
                           "    border-bottom-left-radius: 7px;\n"
                           "    border-bottom-right-radius: 7px;\n"
                           "    subcontrol-position: bottom;\n"
                           "    subcontrol-origin: margin;\n"
                           "}\n"
                           "QScrollBar::add-line:vertical:hover {    \n"
                           "    background-color: rgb(255, 0, 127);\n"
                           "}\n"
                           "QScrollBar::add-line:vertical:pressed {    \n"
                           "    background-color: rgb(185, 0, 92);\n"
                           "}\n"
                           "\n"
                           "/* RESET ARROW */\n"
                           "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                           "    background: none;\n"
                           "}\n"
                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                           "    background: none;\n"
                           "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings = QtCore.QSettings("Fastlauncher", "fastlauncher")
        if self.settings.contains("data/place"):
            self.setGeometry(self.settings.value("data/place"))
        self.main = QtWidgets.QWidget(self)
        self.main.setStyleSheet("background-color: #181a1d;")
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QWidget(self.main)
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setStyleSheet("background-color: rgba(0,0,0, 40);\n"
                                  "border-radius: 6px;\n"
                                  "")
        self.header.setObjectName("header")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setStyleSheet("background-color: none;\n"
                                "border:none;")
        self.logo.setPixmap(QtGui.QPixmap(":/images/FastLauncherLogo.png"))
        self.horizontalLayout_3.addWidget(self.logo)
        self.tools = QtWidgets.QWidget(self.header)
        self.tools.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tools.setStyleSheet("background-color: none;")
        self.tools.setObjectName("tools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tools)
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_news = PushButtonHead.PushButton(self.tools)
        self.btn_news.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  # type: ignore
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-news.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_news.setIcon(icon)
        self.btn_news.setObjectName("btn_news")
        self.horizontalLayout_2.addWidget(self.btn_news)
        self.btn_settings = PushButtonHead.PushButton(self.tools)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-настройки.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_2.addWidget(self.btn_settings)
        self.btn_discord = PushButtonHead.PushButton(self.tools)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-discord.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_discord.setIcon(icon2)
        self.btn_discord.setObjectName("btn_discord")
        self.horizontalLayout_2.addWidget(self.btn_discord)
        self.btn_shutdown = PushButtonHead.PushButton(self.tools)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-выключение-системы-50 (1).png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_shutdown.setIcon(icon3)
        self.btn_shutdown.setIconSize(QtCore.QSize(16, 16))
        self.btn_shutdown.setObjectName("btn_shutdown")
        self.horizontalLayout_2.addWidget(self.btn_shutdown)
        self.horizontalLayout_3.addWidget(self.tools)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.header)
        self.body = QtWidgets.QWidget(self.main)
        self.body.setStyleSheet("background-color: rgba(0,0,0, 40);\n"
                                "border-radius: 6px;\n")
        self.body.setObjectName("body")
        self.btn_play = PushButton.PushButton(
            QtGui.QColor("#26272a"),
            QtGui.QColor("#df005b"),
            parent=self.body,
        )
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  # type: ignore
        self.btn_play.setEnabled(False)
        self.btn_play.setGeometry(QtCore.QRect(280, 450, 75, 23))
        self.btn_play.setObjectName("btn_play")
        self.btn_play.setCheckable(True)
        self.lbl_count = QtWidgets.QLabel(self.body)
        self.lbl_count.setGeometry(QtCore.QRect(-70, 279, 191, 70))
        self.lbl_count.setStyleSheet("background-color: #cc0053;\n"
                                     "font-family: Rubik;\n"
                                     "font-size: 24pt;\n"
                                     "font-weight: bold;\n"
                                     "color: white;\n"
                                     "padding: 10px;")
        self.lbl_count.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)  # type: ignore
        self.lbl_count.setObjectName("lbl_count")
        self.img_play = QtWidgets.QLabel(self.body)
        self.img_play.setGeometry(QtCore.QRect(5, 295, 51, 41))
        self.img_play.setStyleSheet("background-color: none;\n"
                                    "border: none;")
        self.img_play.setPixmap(QtGui.QPixmap(":/icons/icons8-ps-controller-50.png"))
        self.img_play.setObjectName("img_play")
        self.img_game = QtWidgets.QLabel(self.body)
        self.img_game.setStyleSheet("background-color: none;")
        self.img_game.setObjectName("img_game")
        self.img_game.setFont(self.font)
        self.img_game.setStyleSheet("color: white; font-size: 32pt; background: none; padding: 160px 110px;")
        self.img_game.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.widget = QtWidgets.QWidget(self.body)
        self.widget.setFixedWidth(659)
        self.widget.setFixedHeight(488)
        self.widget.setVisible(False)
        self.widget.setStyleSheet("QWidget{\n"
                                  "background-color: #16171a;\n"
                                  "}\n"
                                  "QLabel{\n"
                                  "color: white;\n"
                                  "font-family: Rubik;\n"
                                  "font-size: 14pt;\n"
                                  "}")
        self.widget.setObjectName("widget")
        self.pushButton = PushButtonHead.PushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(14, 10, 171, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-стрелка-влево-в-круге-50.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButto")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 633, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(138)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setStyleSheet(
            """
            QCheckBox::indicator:unchecked{
                image: url(:/icons/icons8-отмеченный-чекбокс-2.svg);
            }
            QCheckBox::indicator:checked{
                image: url(:/icons/icons8-галочка.svg);
            }"""
        )
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)
        if self.settings.contains('data/state_1'):
            state = self.settings.value('data/state_1')
            self.hideLauncherOnPlay = bool(state)
            self.checkBox.setCheckState(state)
        else:
            self.checkBox.setCheckState(2)  # type: ignore
            self.hideLauncherOnPlay = bool(self.checkBox.checkState())
        self.checkBox.clicked.connect(self.saveBoxState_hide)  # type: ignore
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setMaximumSize(QtCore.QSize(600, 16777215))
        self.line.setStyleSheet("background-color: #2e2f31;\n")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(108)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setStyleSheet(
            """
            QCheckBox::indicator:unchecked{
                image: url(:/icons/icons8-отмеченный-чекбокс-2.svg);
            }
            QCheckBox::indicator:checked{
                image: url(:/icons/icons8-галочка.svg);
            }"""
        )
        self.checkBox_2.setObjectName("checkBox_2")
        if self.settings.contains('data/state_2'):
            state = self.settings.value('data/state_2')
            self.launchOnStart = bool(state)
            self.checkBox_2.setCheckState(state)
        else:
            self.checkBox_2.setCheckState(0)  # type: ignore
            self.launchOnStart = bool(self.checkBox_2.checkState())
        self.checkBox_2.clicked.connect(self.saveBoxState_load)  # type: ignore
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.line_2.setStyleSheet("background-color: #2e2f31;\n")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setMaxLength(2)
        self.line_edit.setFixedSize(103, 40)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(14)
        font.setBold(True)
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("QLineEdit {border: none; color: white;}")
        if self.settings.contains("data/shutdown"):
            self.TIME = abs(int(self.settings.value("data/shutdown")))
            self.line_edit.setText(str(self.TIME))
        else:
            self.line_edit.setText(str(self.TIME))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_7.addWidget(self.line_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setMaximumSize(QtCore.QSize(600, 16777215))
        self.line_3.setStyleSheet("background-color: #2e2f31;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.img_game.raise_()
        self.lbl_count.raise_()
        self.img_play.raise_()
        self.btn_play.raise_()
        self.widget.raise_()
        self.verticalLayout_2.addWidget(self.body)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.choice = QtWidgets.QWidget(self.main)
        self.choice.setMaximumSize(QtCore.QSize(250, 16777215))
        self.choice.setStyleSheet("")
        self.choice.setObjectName("choice")
        self.btn_close = PushButton.PushButton(
            QtGui.QColor("#181a1d"),
            QtGui.QColor("#DB3E26"),
            stylesheet="border-radius: 15px;",
            parent=self.choice
        )
        self.btn_close.setGeometry(QtCore.QRect(215, 0, 30, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/close_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName("btn_close")
        self.btn_hide = PushButton.PushButton(
            QtGui.QColor("#181a1d"),
            QtGui.QColor("#121316"),
            stylesheet="border-radius: 15px;",
            parent=self.choice
        )
        self.btn_hide.setGeometry(QtCore.QRect(180, 0, 31, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/remove_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # type: ignore
        self.btn_hide.setIcon(icon6)
        self.btn_hide.setIconSize(QtCore.QSize(24, 24))
        self.btn_hide.setObjectName("btn_hide")
        self.game_list = ListWidget.ListWidget(self.choice)
        for e in set(file.split('.')[0] for file in os.listdir(win.createFolder())):
            element = QtWidgets.QListWidgetItem()
            element.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            element.setFont(self.font)
            with shelve.open(os.path.join(win.TEMP_DIR, e)) as states:
                element.setText(states['keyword'])
            self.game_list.addItem(element)
        # Search panel
        self.le_list = QtWidgets.QLineEdit(self.choice)
        self.le_list.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.le_list.setGeometry(QtCore.QRect(-7, 32, 191, 41))
        self.le_list.setStyleSheet("color: white;\n"
                                   "font-family: Rubik;\n"
                                   "font-size: 16pt;\n"
                                   "font-weight: bold;\n"
                                   "background-color: #2f3033;\n"
                                   "border-radius: 6px;\n"
                                   "\n"
                                   "")
        self.le_list.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.le_list.setObjectName("le_list")
        self.btn_add = PushButton.PushButton(
            QtGui.QColor("#26272a"),
            QtGui.QColor("#df005b"),
            parent=self.choice
        )
        self.btn_add.setGeometry(QtCore.QRect(-5, 562, 250, 30))
        self.horizontalLayout.addWidget(self.choice)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lbl_version = QtWidgets.QLabel(self.main)
        self.lbl_version.setMaximumSize(QtCore.QSize(16777215, 10))
        self.lbl_version.setStyleSheet("color: #898a8c;\n"
                                       "font-size: 6pt;\n"
                                       "font-weight: bold;")
        self.lbl_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)  # type: ignore
        self.lbl_version.setObjectName("lbl_version")
        self.verticalLayout_3.addWidget(self.lbl_version)
        self.verticalLayout.addWidget(self.main)

        self.retranslateUi()

        self.dialog_window = Dialog(self.TIME)

        self.btn_close.clicked.connect(self.close)  # type: ignore
        self.btn_hide.clicked.connect(  # type: ignore
            lambda: self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized))  # type: ignore
        self.btn_settings.clicked.connect(self.open_settings_menu)  # type: ignore
        self.pushButton.clicked.connect(self.open_settings_menu)  # type: ignore
        self.btn_shutdown.clicked.connect(lambda: self.dialog_window.show())  # type: ignore
        self.btn_news.clicked.connect(lambda: webbrowser.open("https://www.python.org/blogs/"))  # type: ignore
        self.btn_discord.clicked.connect(lambda: webbrowser.open("https://discord.gg/Fj6gyJ43M"))  # type: ignore
        self.game_list.clicked.connect(lambda: self.btn_play.setEnabled(True))  # type: ignore
        self.game_list.doubleClicked.connect(lambda: self.open_bind(self.game_list.currentItem()))  # type: ignore
        self.btn_play.clicked.connect(lambda: self.open_bind(self.game_list.currentItem()))  # type: ignore
        self.btn_add.clicked.connect(self.addItem)  # type: ignore
        self.line_edit.textChanged.connect(self.changeValueTime)  # type: ignore
        self.le_list.textChanged.connect(self.findBind)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self) -> None:
        """
        Give name for everyone object in App
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FastLauncher", "FastLauncher"))
        self.btn_news.setText(_translate("FastLauncher", "Новости"))
        self.btn_news.setShortcut(_translate("FastLauncher", "Ctrl+N"))
        self.btn_settings.setText(_translate("FastLauncher", "Настройки"))
        self.btn_settings.setShortcut(_translate("FastLauncher", "Ctrl+S"))
        self.btn_discord.setText(_translate("FastLauncher", "Discord"))
        self.btn_discord.setShortcut(_translate("FastLauncher", "Ctrl+D"))
        self.btn_shutdown.setText(_translate("FastLauncher", "Shutdown"))
        self.btn_shutdown.setShortcut(_translate("FastLauncher", "Ctrl+Q"))
        self.btn_play.setText(_translate("FastLauncher", "LAUNCH"))
        self.btn_add.setText(_translate("FastLauncher", "Добавить"))
        self.lbl_count.setText(_translate("FastLauncher", f"{self.game_list.count()}"))
        self.pushButton.setText(_translate("FastLauncher", "На главную страницу"))
        self.label.setText(_translate("FastLauncher", "Сворачивать лаунчер после запуска бинда"))
        self.label_2.setText(_translate("FastLauncher", "Запускать лаунчер после запуска компьютера"))
        self.label_3.setText(_translate("FastLauncher", "Время до выключения компьютера"))
        self.le_list.setPlaceholderText(_translate("FastLauncher", "Найти..."))
        self.lbl_version.setText(_translate("FastLauncher", "v0.0.7"))

    def saveBoxState_load(self) -> None:
        """
        Save in regedit state from QCheckBox
        :return: None
        """
        self.settings.beginGroup("data")
        self.settings.setValue("state_2", self.checkBox_2.checkState())
        self.settings.endGroup()
        win.autoLaunch(bool(self.checkBox_2.checkState()))

    def saveBoxState_hide(self) -> None:
        """
        Save in regedit state from QCheckBox
        :return: None
        """
        self.settings.beginGroup("data")
        self.settings.setValue("state_1", self.checkBox.checkState())
        self.settings.endGroup()
        self.hideLauncherOnPlay = bool(self.checkBox.checkState())

    def open_settings_menu(self) -> None:
        """
        Open extra menu for App
        :return: None
        """
        if not self.widget.isVisible():
            self.widget.setVisible(True)
        else:
            self.widget.setVisible(False)

    def open_bind(self, _item: QtWidgets.QListWidgetItem) -> None:
        """
        Open bind/game/script
        :param _item: current QListWidgetItem
        :return: None
        """
        if self.hideLauncherOnPlay:
            self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized)  # type: ignore
        th = Thread(target=launcher.openBind, args=(_item.text().strip(),))
        th.start()

    def addItem(self) -> None:
        """
        Add item to game/bind/script list in the App
        :return: None
        """
        item_name = self.game_list.currentItem().text()
        try:
            data = launcher.findBindOnRequest(item_name)
            if data['keyword'] == 'error':
                return
        except AttributeError:
            return
        else:
            with shelve.open(os.path.join(win.createFolder(), f"save_{item_name.upper().split()[1]}")) as states:
                if not states:
                    states["keyword"] = data["keyword"]
                    states["modify_path"] = data["modify_path"]
            element = QtWidgets.QListWidgetItem()
            element.setFont(self.font)
            element.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            element.setText(item_name)
            self.game_list.show()
            self.game_list.takeItem(self.game_list.currentRow())
            self.le_list.clear()
            self.game_list.addItem(element)
            self.game_list.setCurrentRow(-1)

    def changeValueTime(self, x: str) -> None:
        """
        Change shutdown time
        :param x: string value from QLineEdit chane time edit
        :return: None
        """
        try:
            self.TIME = abs(int(x)) if x else 0
        except ValueError:
            self.TIME = 5
        finally:
            self.dialog_window = Dialog(self.TIME)

    def findBind(self, x: str) -> None:
        """
        Find on computer script/bind/game
        :param x: string value signal from QLineEdit
        :return: None
        """
        global item
        if x:
            try:
                bind = launcher.findBindOnRequest(x)
            except re.error:
                bind = {'keyword': 'error'}
            if 'error' in bind['keyword']:
                return
            if self.game_list.findItems(bind['keyword'], QtCore.Qt.MatchContains):  # type: ignore
                return
            else:
                item = QtWidgets.QListWidgetItem()
                item.setText(bind['keyword'])
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                item.setFont(self.font)
                self.game_list.addItem(item)
        else:
            pass
            try:
                self.game_list.takeItem(self.game_list.indexFromItem(item).row())
            except NameError:
                pass
        self.lbl_count.setText(str(self.game_list.count()))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """
        Save data in regedit on the QCloseEvent
        :param a0: Signal shutdown the App
        :return: None
        """
        self.settings.beginGroup("data")
        self.settings.setValue("place", self.geometry())
        self.settings.setValue("shutdown", self.line_edit.text())
        self.settings.endGroup()
