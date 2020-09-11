from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QLabel, QErrorMessage, QFileDialog
from PyQt5.QtGui import QPixmap

class WallpaperRow(QHBoxLayout):
  def __init__(self, currentPath):
    super(WallpaperRow, self).__init__()
    self.currentPath = currentPath
    self.thumbnail_setup()
    self.path_edit_setup()
    self.browse_button_setup()
    self.save_button_setup()
    self.update_thumbnail()

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedWidth(300)
    self.addWidget(self.thumbnail)

  def path_edit_setup(self):
    self.pathEdit = QLineEdit(self.currentPath)
    self.addWidget(self.pathEdit)

  def browse_button_setup(self):
    self.browseButton = QPushButton("Browse images...")
    self.browseButton.clicked.connect(self.handle_browse)
    self.addWidget(self.browseButton)
  
  def save_button_setup(self):
    self.saveButton = QPushButton("Save changes")
    self.saveButton.clicked.connect(self.handle_save)
    self.addWidget(self.saveButton)

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
        scaledPixmap = pixmap.scaledToWidth(300)
      else:
        scaledPixmap = pixmap.scaledToHeight(200)
      self.thumbnail.setPixmap(scaledPixmap)