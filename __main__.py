import os
import fcntl
import sys
import threading
import faulthandler
import subprocess
from background_service import run_background_service, run_subprocess_command
from application import Application, pidFilePath

faulthandler.enable()

def set_is_running():
    pidFile = open(pidFilePath, "w")
    pidFile.write(str(os.getpid()))
    pidFile.close()


def is_running():
    try:
        pidFile = open(pidFilePath, "r+")
        fcntl.lockf(pidFile, fcntl.LOCK_EX)
        pid = int(pidFile.read())
        pidFile.close()
        return "saharah" in run_subprocess_command(f"ps -o cmd= {pid}")
    except Exception:
        return False


def main():
    set_is_running()
    app = Application(sys.argv)
    backgroundThread = threading.Thread(target=run_background_service, args=([app]))
    backgroundThread.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    if is_running():
        print("already active")
    else:
        main()
