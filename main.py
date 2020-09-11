import sys

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from wallpaper_row import WallpaperRow


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.window_setup()
    self.central_widget_setup()
    self.primaryWallpaperRow = WallpaperRow("/hdd/Wallpapers/1.jpg")
    self.mainLayout.addLayout(self.primaryWallpaperRow)
    self.show()

  def window_setup(self):
    self.setGeometry(0, 0, 1000, 750)
    desktopRectangle = self.frameGeometry()
    desktopCenter = QDesktopWidget().availableGeometry().center()
    desktopRectangle.moveCenter(desktopCenter)
    self.move(desktopRectangle.topLeft())
    self.setWindowTitle("Be Setting the Wallpapers")
    self.setWindowIcon(QIcon('app_icon.png'))

  def central_widget_setup(self):
    self.centralWidget = QWidget()
    self.setCentralWidget(self.centralWidget)
    self.mainLayout = QVBoxLayout()
    self.centralWidget.setLayout(self.mainLayout)


def run():
  app = QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())

run()