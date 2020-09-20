import sys
import threading
from PySide2.QtWidgets import QApplication
from system_tray import SystemTray
from main_window import MainWindow
from background_service import write_log

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
    super(Application, self).quit()

def main():
  app = Application(sys.argv)
  backgroundThread = threading.Thread(target = write_log, args=([app]))
  backgroundThread.start()
  sys.exit(app.exec_())

if __name__ == "__main__":main()
