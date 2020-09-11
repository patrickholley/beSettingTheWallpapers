from PyQt5.QtWidgets import QLineEdit, QGridLayout, QPushButton, QLabel, QErrorMessage, QFileDialog, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class WallpaperRow(QGridLayout):
  def __init__(self, currentPath):
    super(WallpaperRow, self).__init__()
    self.currentPath = currentPath
    self.thumbnail_setup()
    self.path_edit_setup()
    self.browse_button_setup()
    self.save_button_setup()
    self.setAlignment(Qt.AlignLeft)
    self.update_thumbnail()

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(180, 120)
    self.addWidget(self.thumbnail, 0, 0, 3, 1)

  def path_edit_setup(self):
    self.pathEdit = QLineEdit(self.currentPath)
    self.pathEdit.setMaximumWidth(270)
    self.addWidget(self.pathEdit, 0, 1)

  def browse_button_setup(self):
    self.browseButton = QPushButton("Browse images...")
    self.browseButton.clicked.connect(self.handle_browse)
    self.addWidget(self.browseButton, 1, 1)
  
  def save_button_setup(self):
    self.saveButton = QPushButton("Save changes")
    self.saveButton.clicked.connect(self.handle_save)
    self.addWidget(self.saveButton, 2, 1)

  def handle_browse(self):
    fileDialog = QFileDialog()
    fileDialog.setFileMode(QFileDialog.ExistingFile)
    fileDialog.setNameFilter("Images (*.png *.xpm *.jpg)")
    fileDialog.setDirectory("/hdd/Wallpapers")
    fileDialog.setWindowTitle("Select an Image")
    if fileDialog.exec():
      self.currentPath = (fileDialog.selectedFiles()[0])
      self.update_thumbnail()

  def handle_save(self):
    self.currentPath = self.pathEdit.text()
    self.update_thumbnail()
    

  def update_thumbnail(self):
    self.pathEdit.setText(self.currentPath)
    pixmap = QPixmap(self.currentPath)
    if pixmap.isNull():
      errorDialog = QErrorMessage()
      errorDialog.showMessage(f"Image at path {self.currentPath} could not be found.")
      errorDialog.exec_()
    else:
      aspectRatio = pixmap.size().width() / pixmap.size().height()
      if aspectRatio > 1.5:
        scaledPixmap = pixmap.scaledToWidth(self.thumbnail.size().width())
      else:
        scaledPixmap = pixmap.scaledToHeight(self.thumbnail.size().height())
      self.thumbnail.setPixmap(scaledPixmap)
