import sys
from PyQt5.QtWidgets import QApplication

from ui.fastlauncher import UiFastLauncher
from bin.win import autoLaunch


def run():
    application = QApplication(sys.argv)
    window = UiFastLauncher()
    autoLaunch(window.launchOnStart)
    window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    run()
