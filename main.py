import sys
import math

from PySide2.QtWidgets import QStyle, QMainWindow, QApplication, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QPushButton
from PySide2.QtGui import QIcon, QGuiApplication
from PySide2.QtCore import Qt
from wallpaper_box import WallpaperBox
from settings_service import applicationSettings
from add_application_button import AddApplicationButton
from utils import clear_layout

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.central_widget_setup()
    self.default_vbox_setup()
    self.addApplicationButton = AddApplicationButton(self)
    self.mainLayout.addWidget(self.addApplicationButton, alignment = Qt.AlignCenter)
    self.application_boxes_setup()
    self.applicationGrid = QVBoxLayout()
    self.application_grid_setup()
    self.mainLayout.addLayout(self.applicationGrid)
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
    self.setWindowIcon(QIcon('assets/app_icon.png'))

  def central_widget_setup(self):
    self.centralWidget = QWidget()
    self.setCentralWidget(self.centralWidget)
    self.mainLayout = QVBoxLayout()
    self.mainLayout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    self.centralWidget.setLayout(self.mainLayout)

  def default_vbox_setup(self):
    self.defaultVBox = QHBoxLayout()
    self.defaultVBox.addWidget(WallpaperBox(0, True))
    self.defaultVBox.addWidget(WallpaperBox(1, True))
    self.mainLayout.addLayout(self.defaultVBox)

  def application_boxes_setup(self):
    self.applicationBoxes = list()
    for i in range(0, len(applicationSettings.list)):
      self.applicationBoxes.append(WallpaperBox(i))

  def application_grid_setup(self):
    for i in range(0, len(self.applicationBoxes)):
      r = math.floor((i) / 4)
      c = i % 4
      if c == 0:
        self.applicationGrid.addLayout(QHBoxLayout())
      layout = self.applicationGrid.itemAt(r).layout()
      layout.addWidget(self.applicationBoxes[i])
    
app = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
