# -*- coding: utf-8 -*-
import ui.res_rc  # type: ignore
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.dialog import Dialog
from bin import win
from ui.handlers.WindowMovement import PressEvent
from webbrowser import open


class UiFastLauncher(QtWidgets.QWidget, PressEvent):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.setFixedSize(950, 650)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setStyleSheet("QScrollBar:vertical {\n"
                           "    margin: 9px 0 15px 0;\n"
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

        self.settings = QtCore.QSettings("Settings", "Using keys")

        if self.settings.contains('Window/Place'):
            self.setGeometry(self.settings.value('Window/Place'))

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
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/FastLauncherLogo.png"))
        self.horizontalLayout_3.addWidget(self.logo)
        self.tools = QtWidgets.QWidget(self.header)
        self.tools.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tools.setStyleSheet("background-color: none;")
        self.tools.setObjectName("tools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tools)
        self.horizontalLayout_2.setSpacing(24)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_news = QtWidgets.QPushButton(self.tools)
        self.btn_news.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_news.setStyleSheet("QPushButton{\n"
                                    "font-family: Rubik;\n"
                                    "color: #898a8c;\n"
                                    "background-color: none;\n"
                                    "border: none;\n"
                                    "font-size: 9pt;\n"
                                    "font-weight: bold;\n"
                                    "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-news.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_news.setIcon(icon)
        self.btn_news.setObjectName("btn_news")
        self.horizontalLayout_2.addWidget(self.btn_news)
        self.btn_settings = QtWidgets.QPushButton(self.tools)
        self.btn_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet("QPushButton{\n"
                                        "font-family: Rubik;\n"
                                        "color: #898a8c;\n"
                                        "background-color: none;\n"
                                        "border: none;\n"
                                        "font-size: 9pt;\n"
                                        "font-weight: bold;\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-настройки.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_2.addWidget(self.btn_settings)
        self.btn_discord = QtWidgets.QPushButton(self.tools)
        self.btn_discord.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_discord.setStyleSheet("QPushButton{\n"
                                       "font-family: Rubik;\n"
                                       "color: #898a8c;\n"
                                       "background-color: none;\n"
                                       "border: none;\n"
                                       "font-size: 9pt;\n"
                                       "font-weight: bold;\n"
                                       "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-discord.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_discord.setIcon(icon2)
        self.btn_discord.setObjectName("btn_discord")
        self.horizontalLayout_2.addWidget(self.btn_discord)
        self.btn_shutdown = QtWidgets.QPushButton(self.tools)
        self.btn_shutdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_shutdown.setStyleSheet("QPushButton{\n"
                                        "font-family: Rubik;\n"
                                        "color: #898a8c;\n"
                                        "background-color: none;\n"
                                        "border: none;\n"
                                        "font-size: 9pt;\n"
                                        "font-weight: bold;\n"
                                        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-выключение-системы-50 (1).png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_shutdown.setIcon(icon3)
        self.btn_shutdown.setIconSize(QtCore.QSize(16, 16))
        self.btn_shutdown.setObjectName("btn_shutdown")
        self.horizontalLayout_2.addWidget(self.btn_shutdown)
        self.horizontalLayout_3.addWidget(self.tools)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.header)
        self.body = QtWidgets.QWidget(self.main)
        self.body.setStyleSheet("background-color: rgba(0,0,0, 40);\n"
                                "border-radius: 6px;\n"
                                "")
        self.body.setObjectName("body")
        self.btn_play = QtWidgets.QPushButton(self.body)
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_play.setEnabled(True)
        self.btn_play.setGeometry(QtCore.QRect(280, 450, 75, 23))
        self.btn_play.setStyleSheet("QPushButton {\n"
                                    "background-color: #26272a;\n"
                                    "color: gray;\n"
                                    "font-family: Rubik;\n"
                                    "font-weight: bold;\n"
                                    "border-radius: 0px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "background-color: #df005b;\n"
                                    "color: white;\n"
                                    "}")
        self.btn_play.setObjectName("btn_play")
        self.lbl_count = QtWidgets.QLabel(self.body)
        self.lbl_count.setGeometry(QtCore.QRect(-70, 279, 191, 70))
        self.lbl_count.setStyleSheet("background-color: #cc0053;\n"
                                     "font-family: Rubik;\n"
                                     "font-size: 24pt;\n"
                                     "font-weight: bold;\n"
                                     "color: white;\n"
                                     "padding: 10px;")
        self.lbl_count.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbl_count.setObjectName("lbl_count")
        self.img_play = QtWidgets.QLabel(self.body)
        self.img_play.setGeometry(QtCore.QRect(5, 295, 51, 41))
        self.img_play.setStyleSheet("background-color: none;\n"
                                    "border: none;")
        self.img_play.setText("")
        self.img_play.setPixmap(QtGui.QPixmap(":/icons/icons8-ps-controller-50.png"))
        self.img_play.setObjectName("img_play")
        self.img_game = QtWidgets.QLabel(self.body)
        self.img_game.setGeometry(QtCore.QRect(10, -31, 631, 511))
        self.img_game.setStyleSheet("background-color: none;")
        self.img_game.setText("")
        self.img_game.setPixmap(QtGui.QPixmap(":/images/GTA-5-PNG-Image.png"))
        self.img_game.setObjectName("img_game")
        self.widget = QtWidgets.QWidget(self.body)
        self.widget.setVisible(False)
        self.widget.setGeometry(QtCore.QRect(0, 0, 651, 491))
        self.widget.setStyleSheet("QWidget{\n"
                                  "background-color: #16171a;\n"
                                  "}\n"
                                  "\n"
                                  "QLabel{\n"
                                  "color: white;\n"
                                  "font-family: Rubik;\n"
                                  "font-size: 14pt;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton{\n"
                                  "font-family: Rubik;\n"
                                  "color: #898a8c;\n"
                                  "background-color: none;\n"
                                  "border: none;\n"
                                  "font-size: 10pt;\n"
                                  "font-weight: bold;\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(14, 10, 171, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons_buttons/icons8-стрелка-влево-в-круге-50.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")
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
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_6.addWidget(self.checkBox)

        if self.settings.contains('Data2/State'):
            state = self.settings.value('Data2/State')
            self.hideLauncherOnPlay = bool(state)
            self.checkBox.setCheckState(state)
        else:
            self.hideLauncherOnPlay = bool(self.checkBox.checkState())
        self.checkBox.clicked.connect(self.saveBoxState_hide)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setMaximumSize(QtCore.QSize(600, 16777215))
        self.line.setStyleSheet("background-color: #2e2f31;\n"
                                "")
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
        self.checkBox_2.setObjectName("checkBox_2")
        if self.settings.contains('Data/State'):
            state = self.settings.value('Data/State')
            self.launchOnStart = bool(state)
            self.checkBox_2.setCheckState(state)
        else:
            self.launchOnStart = bool(self.checkBox_2.checkState())
        self.checkBox_2.clicked.connect(self.saveBoxState_load)  # type: ignore
        self.horizontalLayout_5.addWidget(self.checkBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.line_2.setStyleSheet("background-color: #2e2f31;\n"
                                  "")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
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
        self.btn_close = QtWidgets.QPushButton(self.choice)
        self.btn_close.setGeometry(QtCore.QRect(210, 0, 30, 30))
        self.btn_close.setStyleSheet("QPushButton{\n"
                                     "    color: white;\n"
                                     "    background-color: #181a1d;\n"
                                     "    border: none;\n"
                                     "    border-radius: 15px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover{\n"
                                     "    background-color: #121316;\n"
                                     "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/close_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(24, 24))
        self.btn_close.setObjectName("btn_close")
        self.btn_hide = QtWidgets.QPushButton(self.choice)
        self.btn_hide.setGeometry(QtCore.QRect(180, 0, 31, 30))
        self.btn_hide.setStyleSheet("QPushButton{\n"
                                    "    color: white;\n"
                                    "    background-color: #181a1d;\n"
                                    "    border: none;\n"
                                    "    border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: #121316;\n"
                                    "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/remove_white_24dp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hide.setIcon(icon6)
        self.btn_hide.setIconSize(QtCore.QSize(24, 24))
        self.btn_hide.setObjectName("btn_hide")
        self.game_list = QtWidgets.QListWidget(self.choice)
        self.game_list.setGeometry(QtCore.QRect(-12, 98, 260, 541))
        self.game_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.game_list.verticalScrollBar().setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.game_list.setSpacing(9)
        self.game_list.setStyleSheet("QListWidget{\n"
                                     "border: none;\n"
                                     "}\n"
                                     "\n"
                                     "QListWidget::item{\n"
                                     "background-color: #16171a;\n"
                                     "color: white;\n"
                                     "height: 75px;\n"
                                     "}\n"
                                     "\n"
                                     "QListWidget::item:hover{\n"
                                     "background-color: #1f2124;\n"
                                     "}")
        self.game_list.setObjectName("game_list")
        for _ in range(12):
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Rubik")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.NoBrush)
            item.setBackground(brush)
            self.game_list.addItem(item)
        self.lbl_list = QtWidgets.QLabel(self.choice)
        self.lbl_list.setGeometry(QtCore.QRect(-7, 32, 170, 41))
        self.lbl_list.setStyleSheet("color: white;\n"
                                    "font-family: Rubik;\n"
                                    "font-size: 16pt;\n"
                                    "font-weight: bold;\n"
                                    "background-color: #2f3033;\n"
                                    "border-radius: 6px;\n"
                                    "\n"
                                    "")
        self.lbl_list.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_list.setObjectName("lbl_list")
        self.horizontalLayout.addWidget(self.choice)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lbl_version = QtWidgets.QLabel(self.main)
        self.lbl_version.setMaximumSize(QtCore.QSize(16777215, 10))
        self.lbl_version.setStyleSheet("color: #898a8c;\n"
                                       "font-size: 6pt;\n"
                                       "font-weight: bold;")
        self.lbl_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.lbl_version.setObjectName("lbl_version")
        self.verticalLayout_3.addWidget(self.lbl_version)
        self.verticalLayout.addWidget(self.main)

        dialog_window = Dialog()

        self.retranslateUi()

        self.btn_close.clicked.connect(QtWidgets.qApp.exit)  # type: ignore
        self.btn_hide.clicked.connect(lambda: self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized))  # type: ignore
        self.btn_settings.clicked.connect(self.open_settings_menu)  # type: ignore
        self.pushButton.clicked.connect(self.open_settings_menu)  # type: ignore
        self.btn_shutdown.clicked.connect(lambda: dialog_window.show())  # type: ignore
        self.btn_news.clicked.connect(lambda: open("https://vk.com/alexanderkochetov"))  # type: ignore
        self.btn_discord.clicked.connect(lambda: open("https://discord.gg/ezVDWXmgx"))  # type: ignore
        self.btn_play.clicked.connect(self.open_bind)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.btn_news.setText(_translate("self", "Новости"))
        self.btn_news.setShortcut(_translate("self", "Ctrl+N"))
        self.btn_settings.setText(_translate("self", "Настройки"))
        self.btn_settings.setShortcut(_translate("self", "Ctrl+S"))
        self.btn_discord.setText(_translate("self", "Discord"))
        self.btn_discord.setShortcut(_translate("self", "Ctrl+D"))
        self.btn_shutdown.setText(_translate("self", "Shutdown"))
        self.btn_shutdown.setShortcut(_translate("self", "Ctrl+Q"))
        self.btn_play.setText(_translate("self", "Играть"))
        self.lbl_count.setText(_translate("self", f"{self.game_list.count()}"))
        self.pushButton.setText(_translate("self", "На главную страницу"))
        self.label.setText(_translate("self", "Сворачивать лаунчер после запуска бинда"))
        self.label_2.setText(_translate("self", "Запускать лаунчер после запуска компьютера"))
        __sortingEnabled = self.game_list.isSortingEnabled()
        self.game_list.setSortingEnabled(False)
        item = self.game_list.item(0)
        item.setText(_translate("self", "1"))
        item = self.game_list.item(1)
        item.setText(_translate("self", "2"))
        item = self.game_list.item(2)
        item.setText(_translate("self", "3"))
        item = self.game_list.item(3)
        item.setText(_translate("self", "1"))
        item = self.game_list.item(4)
        item.setText(_translate("self", "2"))
        item = self.game_list.item(5)
        item.setText(_translate("self", "3"))
        item = self.game_list.item(6)
        item.setText(_translate("self", "1"))
        item = self.game_list.item(7)
        item.setText(_translate("self", "2"))
        item = self.game_list.item(8)
        item.setText(_translate("self", "3"))
        item = self.game_list.item(9)
        item.setText(_translate("self", "1"))
        item = self.game_list.item(10)
        item.setText(_translate("self", "2"))
        item = self.game_list.item(11)
        item.setText(_translate("self", "3"))
        self.game_list.setSortingEnabled(__sortingEnabled)
        self.lbl_list.setText(_translate("self", "Список игр"))
        self.lbl_version.setText(_translate("self", "v0.0.1"))

    def saveBoxState_load(self):
        self.settings.beginGroup("Data")
        self.settings.setValue("State", self.checkBox_2.checkState())
        self.settings.endGroup()
        win.autoLaunch(bool(self.checkBox_2.checkState()))

    def saveBoxState_hide(self):
        self.settings.beginGroup("Data2")
        self.settings.setValue("State", self.checkBox.checkState())
        self.settings.endGroup()
        self.hideLauncherOnPlay = bool(self.checkBox.checkState())

    def open_settings_menu(self):
        if not self.widget.isVisible():
            self.widget.setVisible(True)
            self.btn_settings.setStyleSheet("QPushButton{\n"
                                            "font-family: Rubik;\n"
                                            "color: white;\n"
                                            "background-color: none;\n"
                                            "border: none;\n"
                                            "font-size: 9pt;\n"
                                            "font-weight: bold;\n"
                                            "}\n")
        else:
            self.btn_settings.setStyleSheet("QPushButton{\n"
                                            "font-family: Rubik;\n"
                                            "color: #898a8c;\n"
                                            "background-color: none;\n"
                                            "border: none;\n"
                                            "font-size: 9pt;\n"
                                            "font-weight: bold;\n"
                                            "}\n")
            self.widget.setVisible(False)

    def open_bind(self):
        if self.hideLauncherOnPlay:
            self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.settings.beginGroup('Window')
        self.settings.setValue('Place', self.geometry())
        self.settings.endGroup()
