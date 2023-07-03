from pathlib import Path
from subprocess import call

from winapps import search_installed

BASE_DIR = Path(__file__).cwd().parent


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
    except ValueError:
        return {'error': 'not found the game'}
    else:
        return {"name": npp.name, "modify_path": npp.modify_path}
