# -*- coding: utf-8 -*-
from subprocess import call

from winapps import search_installed


def shutdownComputer(time: int) -> None:
    call(f"shutdown -s -t {abs(int(time))}")


def shutdownComputerOff() -> None:
    call("shutdown -a")


def openBind(name: str) -> dict:
    try:
        [npp] = search_installed(name.lower().strip())
        if npp:
            if "steam" in npp.uninstall_string:
                call(str(npp.uninstall_string).replace('uninstall', 'run'))
            else:
                print(npp.uninstall_string)
    except ValueError:
        return {"error": "Name bind is invalid"}


def findBindOnRequest(name: str) -> dict:
    try:
        [npp] = search_installed(name.lower().strip())
        if npp:
            if "steam" in npp.uninstall_string:
                modify_path = str(npp.uninstall_string).replace('uninstall', 'run')
            else:
                modify_path = str(npp.uninstall_string)
        else:
            modify_path = None
    except ValueError:
        return {"keyword": "error", "modify_path": "Not found the game/bind/script/app"}
    else:
        return {"keyword": npp.name, "modify_path": modify_path}
