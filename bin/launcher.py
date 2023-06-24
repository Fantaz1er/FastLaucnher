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
        [npp] = search_installed(name.lower())
        if name.lower() == 'war thunder':
            call(str(npp.uninstall_string).replace('uninstall', 'run'))
        else:
            try:
                call(npp.install_location)
            except:
                return {'error': 'Operation not allowed'}
    except ValueError:
        return {"error": "Name bind is invalid"}
