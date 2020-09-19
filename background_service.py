import datetime
import time

def write_log(self):
  print(self)
  while not self.stopped:
    print(self.stopped)
    logPath = "log.txt"
    logFile = open(logPath, "w")
    logFile.write(str(datetime.datetime.now()))
    logFile.close()
    time.sleep(5)
  