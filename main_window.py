import math
import sys
from PySide2.QtWidgets import QStyle, QMainWindow, QMenu, QWidget, QHBoxLayout, QVBoxLayout, QScrollArea
from PySide2.QtGui import QIcon, QGuiApplication
from PySide2.QtCore import Qt
from wallpaper_box import WallpaperBox
from settings_service import applicationSettings
from add_application_button import AddApplicationButton
from primary_monitor_select import PrimaryMonitorSelect
from utils import clear_layout

class MainWindow(QMainWindow):
  def __init__(self, app):
    super(MainWindow, self).__init__()
    self.app = app
    self.central_widget_setup()
    self.default_vbox_setup()
    self.layout.addWidget(PrimaryMonitorSelect(self))
    self.add_application_button_setup()
    self.application_boxes_setup()
    self.application_grid_setup()
    self.application_scroll_setup()
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
    self.setWindowIcon(QIcon(f"{sys.argv[0]}/assets/app_icon.png"))

  def central_widget_setup(self):
    self.centralWidget = QWidget()
    self.setCentralWidget(self.centralWidget)
    self.layout = QVBoxLayout()
    self.layout.setAlignment(Qt.AlignCenter | Qt.AlignTop)
    self.centralWidget.setLayout(self.layout)

  def default_vbox_setup(self):
    self.defaultVBox = QHBoxLayout()
    self.defaultVBox.addWidget(WallpaperBox(self, 0, True))
    self.defaultVBox.addWidget(WallpaperBox(self, 1, True))
    self.layout.addLayout(self.defaultVBox)

  def add_application_button_setup(self):
    self.addApplicationButton = AddApplicationButton(self)
    self.layout.addWidget(self.addApplicationButton, alignment = Qt.AlignCenter)

  def application_boxes_setup(self):
    self.applicationBoxes = list()
    for i in range(0, len(applicationSettings.list)):
      self.applicationBoxes.append(WallpaperBox(self, i))

  def application_grid_setup(self):
    self.applicationGrid = QVBoxLayout()
    self.applicationGridContainer = QWidget()
    self.applicationGridContainer.setLayout(self.applicationGrid)
    self.applicationGridContainer.setFixedWidth(1340)
    self.application_grid_arrange()

  def application_grid_arrange(self):
    for i in reversed(range(0, self.applicationGrid.count())):
      layout = self.applicationGrid.takeAt(i).layout()
      for j in reversed(range(0, layout.count())):
        widget = layout.takeAt(j).widget()
        widget.hide()
    for i in range(0, len(self.applicationBoxes)):
      r = math.floor((i) / 4)
      c = i % 4
      if c == 0:
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.applicationGrid.addLayout(layout)
      layout = self.applicationGrid.itemAt(r).layout()
      applicationBox = self.applicationBoxes[i]
      applicationBox.set_index(i)
      applicationBox.show()
      layout.addWidget(applicationBox)
    self.applicationGridContainer.setFixedHeight(self.applicationGrid.count() * 250)

  def application_scroll_setup(self):
    self.applicationScroll = QScrollArea()
    self.applicationScroll.setWidget(self.applicationGridContainer)
    self.applicationScroll.setFixedSize(1370, 510)
    self.layout.addWidget(self.applicationScroll)

  def closeEvent(self, event):
    self.app.mainWindow = None
    event.accept()
    