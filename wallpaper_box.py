from PySide2.QtWidgets import QLineEdit, QVBoxLayout, QPushButton, QLabel, QErrorMessage, QFileDialog, QSpacerItem, QSizePolicy
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from settings_service import settingsList, save_settings

class WallpaperBox(QVBoxLayout):
  def __init__(self, row, isDefaultSetting = False):
    super(WallpaperBox, self).__init__()
    self.setAlignment(Qt.AlignTop)
    self.column = 3 if isDefaultSetting else 1
    self.row = row
    self.isDefaultSetting = isDefaultSetting
    self.thumbnail_setup()
    self.label_setup()
    self.browse_button_setup()
    self.update_thumbnail()

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(300, 169) # see if width can be applied to layout
    self.thumbnail.setStyleSheet("border: 1px solid black;")
    self.addWidget(self.thumbnail)
  
  def label_setup(self):
    self.label = QLabel(settingsList[self.row][self.column - 1])
    self.label.setAlignment(Qt.AlignCenter)
    self.label.setFixedWidth(300)
    self.addWidget(self.label)

  def browse_button_setup(self):
    self.browseButton = QPushButton("Browse images...")
    self.browseButton.clicked.connect(self.handle_browse)
    self.browseButton.setFixedWidth(300)
    self.addWidget(self.browseButton)

  def handle_browse(self):
    fileDialog = QFileDialog()
    fileDialog.setFileMode(QFileDialog.ExistingFile)
    fileDialog.setNameFilter("Images (*.png *.xpm *.jpg)")
    fileDialog.setDirectory("/hdd/Wallpapers")
    fileDialog.setWindowTitle("Select an Image")
    if fileDialog.exec():
      settingsList[self.row][self.column] = (fileDialog.selectedFiles()[0])
      self.update_thumbnail()
      save_settings()

  def update_thumbnail(self):
    pixmap = QPixmap(settingsList[self.row][self.column])
    if pixmap.isNull():
      errorDialog = QErrorMessage()
      errorDialog.showMessage(f"Image at path {settingsList[self.row][self.column]} could not be found.")
      errorDialog.exec_()
    else:
      aspectRatio = pixmap.size().width() / pixmap.size().height()
      if aspectRatio > 1.5:
        scaledPixmap = pixmap.scaledToWidth(self.thumbnail.size().width())
      else:
        scaledPixmap = pixmap.scaledToHeight(self.thumbnail.size().height())
      self.thumbnail.setPixmap(scaledPixmap)
