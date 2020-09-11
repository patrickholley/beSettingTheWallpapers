from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class WallpaperRow(QHBoxLayout):
  def __init__(self, currentPath):
    super(WallpaperRow, self).__init__()
    self.currentPath = currentPath
    self.thumbnail_setup()
    self.path_edit_setup()
    self.browse_button_setup()
    self.save_button_setup()

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.pixmap = QPixmap(self.currentPath).scaledToWidth(300)
    self.thumbnail.setPixmap(self.pixmap)
    self.addWidget(self.thumbnail)

  def path_edit_setup(self):
    self.pathEdit = QLineEdit(self.currentPath)
    self.addWidget(self.pathEdit)

  def browse_button_setup(self):
    self.browseButton = QPushButton("Browse images . . .")
    self.addWidget(self.browseButton)
  
  def save_button_setup(self):
    self.saveButton = QPushButton("Save changes")
    self.addWidget(self.saveButton)