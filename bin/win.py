import sys
from winreg import *


def isWindows(func):
    def wrapper(*args, **kwargs):
        if sys.platform == 'win32':
            func(*args, **kwargs)
        else:
            return {"error": "No working on no windows OS"}
    return wrapper


@isWindows
def autoLaunch(onStart: bool) -> None:
    key_my = OpenKey(HKEY_CURRENT_USER,
                     r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                     0,
                     KEY_ALL_ACCESS)
    SetValueEx(key_my, 'FastLauncher', 0, REG_SZ, sys.argv[0] if onStart else '')
    CloseKey(key_my)
