from PySide2.QtWidgets import QVBoxLayout, QPushButton, QLabel, QErrorMessage, QFileDialog, QHBoxLayout, QWidget
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt, QSize
from settings_service import settingsList, save_settings
from edit_wallpaper_dialog import EditWallpaperDialog, update_thumbnail

class WallpaperBox(QVBoxLayout):
  def __init__(self, rowIndex, isDefaultSetting = False):
    super(WallpaperBox, self).__init__()
    self.setAlignment(Qt.AlignTop)
    baseColumn = 3 if isDefaultSetting else 0
    self.isDefaultSetting = isDefaultSetting
    self.rowIndex = rowIndex
    self.row = settingsList[rowIndex]
    self.pathColumn = baseColumn + 1
    self.path = self.row[self.pathColumn]
    self.applicationColumn = baseColumn
    self.application = self.row[self.applicationColumn]
    if not self.isDefaultSetting:
      self.processColumn = baseColumn + 2
      self.process = self.row[self.processColumn]
    self.thumbnail_setup()
    self.label_row_setup()

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(300, 169)
    self.thumbnail.setStyleSheet("background-color: black; border: 1px solid black;")
    self.thumbnail.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    update_thumbnail(self)
    self.addWidget(self.thumbnail)
  
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
    self.addWidget(labelRowWrapper)

  def button_setup(self, iconPath, handle_click):
    button = QPushButton("")
    button.setIcon(QIcon(iconPath))
    button.setFixedSize(30, 30)
    button.clicked.connect(handle_click)
    self.labelRow.addWidget(button)

  def handle_delete(self):
    print("Will delete")

  def handle_edit(self):
    self.editWallpaperDialog = EditWallpaperDialog(self)
    self.editWallpaperDialog.exec_()

  def handle_save(self, path, application = None, process = None):
    if not self.isDefaultSetting:
      self.application = application
      self.label.setText(self.application)
      settingsList[self.rowIndex][self.applicationColumn] = self.application
      self.process = process
      settingsList[self.rowIndex][self.processColumn] = self.process
    self.path = path
    update_thumbnail(self)
    settingsList[self.rowIndex][self.pathColumn] = self.path
    save_settings()
