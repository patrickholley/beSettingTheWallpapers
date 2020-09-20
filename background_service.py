import datetime
import time

def write_log(self):
  throttle = 0
  while not self.stopped:
    throttle += 1
    if throttle == 5:
      throttle = 0
      print("ran background task")
    time.sleep(1)
  