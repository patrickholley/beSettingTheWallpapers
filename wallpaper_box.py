from PySide2.QtWidgets import QVBoxLayout, QPushButton, QLabel, QErrorMessage, QFileDialog, QHBoxLayout, QWidget
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt, QSize
from settings_service import settingsList
from edit_wallpaper_dialog import EditWallpaperDialog, update_thumbnail

class WallpaperBox(QVBoxLayout):
  def __init__(self, row, isDefaultSetting = False):
    super(WallpaperBox, self).__init__()
    self.setAlignment(Qt.AlignTop)
    baseColumn = 3 if isDefaultSetting else 0
    self.applicationColumn = baseColumn
    self.pathColumn = baseColumn + 1
    self.processColumn = baseColumn + 2
    self.row = row
    self.isDefaultSetting = isDefaultSetting
    self.thumbnail_setup()
    self.label_row_setup()
    self.editWallpaperDialog = EditWallpaperDialog(row, self)

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(300, 169)
    self.thumbnail.setStyleSheet("background-color: black; border: 1px solid black;")
    self.thumbnail.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    update_thumbnail(self, self.row, self.pathColumn)
    self.addWidget(self.thumbnail)
  
  def label_row_setup(self):
    self.labelRow = QHBoxLayout()
    self.label = QLabel(settingsList[self.row][self.applicationColumn])
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
    self.editWallpaperDialog.exec_()
