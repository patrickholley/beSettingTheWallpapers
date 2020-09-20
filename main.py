import os
import fcntl
import sys
import threading
from background_service import write_log
from application import Application, pidFilePath

def write_pid():
  pidFile = open(pidFilePath, "w")
  print(os.getpid())
  pidFile.write(str(os.getpid()))
  pidFile.close()

def is_already_running():
  try:
    pidFile = open(pidFilePath, "r+")
    fcntl.lockf(pidFile, fcntl.LOCK_EX)
    pid = int(pidFile.read())
    pidFile.close()
    return True if os.kill(pid, 0) is None else False
  except Exception as e:
    return False

def main():
  write_pid()
  app = Application(sys.argv)
  backgroundThread = threading.Thread(target = write_log, args=([app]))
  backgroundThread.start()
  sys.exit(app.exec_())

if __name__ == "__main__":
  if is_already_running():
    print("already active")
  else:
    main()
