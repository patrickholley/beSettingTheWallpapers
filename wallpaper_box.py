from PySide2.QtWidgets import QVBoxLayout, QPushButton, QLabel, QErrorMessage, QFileDialog, QHBoxLayout, QWidget
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt, QSize
from settings_service import applicationSettings, defaultSettings
from edit_wallpaper_dialog import EditWallpaperDialog, update_thumbnail
from utils import clear_layout

class WallpaperBox(QWidget):
  def __init__(self, parent, index, isDefaultSetting = False):
    super(WallpaperBox, self).__init__()
    self.parent = parent
    self.layout = QVBoxLayout()
    self.layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
    self.setLayout(self.layout)
    self.isDefaultSetting = isDefaultSetting
    self.settings = defaultSettings if self.isDefaultSetting else applicationSettings
    self.index = index
    self.row = self.settings.list[index]
    self.applicationColumn = 0
    self.application = self.row[self.applicationColumn]
    self.pathColumn = 1
    self.path = self.row[self.pathColumn]
    if not self.isDefaultSetting:
      self.processColumn = 2
      self.process = self.row[self.processColumn]
    self.thumbnail_setup()
    self.label_row_setup()
    self.setFixedSize(325, 250)

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(300, 169)
    self.thumbnail.setStyleSheet("background-color: black; border: 1px solid black;")
    self.thumbnail.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    update_thumbnail(self)
    self.layout.addWidget(self.thumbnail)
  
  def label_row_setup(self):
    self.labelRow = QHBoxLayout()
    self.label = QLabel(self.application)
    self.labelRow.addWidget(self.label)
    self.button_setup("assets/edit.svg", self.handle_edit)
    if not self.isDefaultSetting:
      self.button_setup("assets/delete.svg", self.handle_delete)
    labelRowWrapper = QWidget()
    labelRowWrapper.setLayout(self.labelRow)
    labelRowWrapper.setFixedWidth(300)
    self.layout.addWidget(labelRowWrapper)

  def button_setup(self, iconPath, handle_click):
    button = QPushButton("")
    button.setIcon(QIcon(iconPath))
    button.setFixedSize(30, 30)
    button.clicked.connect(handle_click)
    self.labelRow.addWidget(button)

  def handle_delete(self):
    self.settings.list.pop(self.index)
    self.settings.write()
    self.parent.applicationBoxes.pop(self.index)
    self.parent.application_grid_arrange()

  def handle_edit(self):
    self.editWallpaperDialog = EditWallpaperDialog(self)
    self.editWallpaperDialog.exec_()

  def handle_save(self, path, application = None, process = None):
    if not self.isDefaultSetting:
      self.application = application
      self.label.setText(self.application)
      self.settings.list[self.index][self.applicationColumn] = self.application
      self.process = process
      self.settings.list[self.index][self.processColumn] = self.process
    self.path = path
    update_thumbnail(self)
    self.settings.list[self.index][self.pathColumn] = self.path
    self.settings.write()

  def set_index(self, index):
    self.index = index
