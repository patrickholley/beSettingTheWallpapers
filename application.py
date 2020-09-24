import os
import sys
from PySide2.QtWidgets import QApplication
from main_window import MainWindow
from system_tray import SystemTray

pidFilePath = f"{sys.argv[0]}/saharah.pid"

class Application(QApplication):
  def __init__(self, *args):
    super(Application, self).__init__(*args)
    self.stopped = False
    self.setQuitOnLastWindowClosed(False)
    self.systemTray = SystemTray(self)

  def open_main_window(self):
    self.mainWindow = MainWindow(self)

  def quit(self):
    self.stopped = True
    try:
      os.remove(pidFilePath)
    except OSError:
      pass
    super(Application, self).quit()
