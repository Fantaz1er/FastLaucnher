# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from bin.win import autoLaunch
from ui.fastlauncher import UiFastLauncher


def run():
    application = QApplication(sys.argv)
    window = UiFastLauncher()
    QFontDatabase.addApplicationFont(r':fonts\Rubik-Bold.ttf')
    QFontDatabase.addApplicationFont(r':fonts\Rubik-Regular.ttf')
    autoLaunch(window.launchOnStart)
    window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    run()
