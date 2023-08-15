# -*- coding: utf-8 -*-
import sys
import os
from winreg import *
from pathlib import Path

if sys.platform == 'win32':
    TEMP_DIR = os.path.join(os.getenv('TMP'), '_FL_TEMP')
else:
    TEMP_DIR = os.path.join(Path(__file__).resolve().parent.parent, r'temp')


def isWindows(func) -> object:
    def wrapper(*args, **kwargs):
        if sys.platform == 'win32':
            func(*args, **kwargs)
        else:
            return {"keyword": "error", "msg": "No working on no windows OS"}
    return wrapper


def createFolder() -> str:
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    return TEMP_DIR


@isWindows
def autoLaunch(onStart: bool) -> None:
    key_my = OpenKey(HKEY_CURRENT_USER,
                     r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                     0,
                     KEY_ALL_ACCESS)
    SetValueEx(key_my, 'FastLauncher', 0, REG_SZ, sys.argv[0] if onStart else '')
    CloseKey(key_my)
