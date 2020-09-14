import sys

from PySide2.QtWidgets import QStyle, QMainWindow, QDesktopWidget, QApplication, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout
from PySide2.QtGui import QIcon, QGuiApplication
from PySide2.QtCore import Qt
from wallpaper_box import WallpaperBox
from settings_service import settingsList

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.central_widget_setup()
    self.default_vbox_setup()
    self.application_grid_setup()
    self.window_setup()
    self.show()

  def window_setup(self):
    self.adjustSize()
    self.setGeometry(
      QStyle.alignedRect(
        Qt.LeftToRight,
        Qt.AlignCenter,
        self.size(),
        QGuiApplication.primaryScreen().availableGeometry(),
      )
    )
    self.setWindowTitle("Be Setting the Wallpapers")
    self.setWindowIcon(QIcon('app_icon.png'))

  def central_widget_setup(self):
    self.centralWidget = QWidget()
    self.setCentralWidget(self.centralWidget)
    self.mainLayout = QVBoxLayout()
    self.mainLayout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    self.centralWidget.setLayout(self.mainLayout)

  def default_vbox_setup(self):
    self.defaultVBox = QHBoxLayout()
    self.defaultVBox.addLayout(WallpaperBox(1, True))
    self.defaultVBox.addLayout(WallpaperBox(2, True))
    self.mainLayout.addLayout(self.defaultVBox)

  def application_grid_setup(self):
    self.applicationGrid = QGridLayout()
    for i in range(1, len(settingsList)):
      r = (i - 1) / 4
      c = (i - 1) % 4
      self.applicationGrid.addLayout(WallpaperBox(i), r, c)
    
    self.mainLayout.addLayout(self.applicationGrid)

def run():
  app = QApplication(sys.argv)
  mainWindow = MainWindow()
  sys.exit(app.exec_())

run()
