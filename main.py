import sys

from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon
from wallpaper_row import WallpaperRow
from settings_service import settingsList

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.window_setup()
    self.central_widget_setup()
    self.leftWallpaperRow = WallpaperRow(1, True)
    self.rightWallpaperRow = WallpaperRow(2, True)
    self.mainLayout.addLayout(self.leftWallpaperRow)
    self.mainLayout.addLayout(self.rightWallpaperRow)
    self.show()

  def window_setup(self):
    self.setGeometry(0, 0, 320, 160)
    desktopRectangle = self.frameGeometry()
    desktopCenter = QDesktopWidget().availableGeometry().center()
    desktopRectangle.moveCenter(desktopCenter)
    self.move(desktopRectangle.topLeft())
    self.setWindowTitle("Be Setting the Wallpapers")
    self.setWindowIcon(QIcon('app_icon.png'))

  def central_widget_setup(self):
    self.centralWidget = QWidget()
    self.setCentralWidget(self.centralWidget)
    self.mainLayout = QHBoxLayout()
    self.centralWidget.setLayout(self.mainLayout)


def run():
  app = QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())

run()
