import subprocess
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).cwd().parent


def shutdownComputer(time: int = int(os.getenv("TIME"))) -> None:
    subprocess.call(f"shutdown -s -t {time}")


def shutdownComputerOff() -> None:
    subprocess.call("shutdown -a")


if __name__ == '__main__':
    # shutdownComputer()  # success
    pass
