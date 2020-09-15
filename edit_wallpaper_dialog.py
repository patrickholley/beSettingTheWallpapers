from PySide2.QtWidgets import QDialog

class EditWallpaperDialog(QDialog):
  def __init__(self, row, isDefaultSetting = False):
    super(EditWallpaperDialog, self).__init__()
    self.setWindowTitle("Edit Wallpaper")
    self.setFixedSize(self.size())
    

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
      settingsList[self.row][self.pathColumn] = (fileDialog.selectedFiles()[0])
      self.update_thumbnail()
      save_settings()
