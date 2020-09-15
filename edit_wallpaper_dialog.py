from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QHBoxLayout, QMessageBox
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt
from settings_service import settingsList, save_settings

def update_thumbnail(self, row, pathColumn):
  pixmap = QPixmap(settingsList[row][pathColumn])
  if pixmap.isNull():
    errorDialog = QErrorMessage()
    errorDialog.showMessage(f"Image at path {settingsList[row][pathColumn]} could not be found.")
    errorDialog.exec_()
  else:
    aspectRatio = pixmap.size().width() / pixmap.size().height()
    if aspectRatio > 1.78:
      scaledPixmap = pixmap.scaledToWidth(self.thumbnail.size().width())
    else:
      scaledPixmap = pixmap.scaledToHeight(self.thumbnail.size().height())
    self.thumbnail.setPixmap(scaledPixmap)

class EditWallpaperDialog(QDialog):
  def __init__(self, row, parent):
    super(EditWallpaperDialog, self).__init__()
    self.setWindowTitle("Edit Wallpaper")
    self.isSaved = False
    self.parent = parent
    self.layout = QVBoxLayout()
    self.settingsList = settingsList.copy()
    self.setLayout(self.layout)
    self.thumbnail_setup()
    self.application_edit_setup()
    if not self.parent.isDefaultSetting:
      self.process_edit_setup()
    self.select_image_button_setup()
    self.save_button_setup()
    self.adjustSize()
    self.setFixedSize(self.size())

  def closeEvent(self, event):
    if self.isSaved:
      event.accept()
    else:
      messageBox = QMessageBox()
      confirmClose = messageBox.question(
        self,
        "Confirm Cancel",
        "Any changes made will not be saved. Cancel anyways?",
        messageBox.No,
        messageBox.Yes
      )

      if confirmClose == messageBox.Yes:
        event.accept()
      else:
        event.ignore()

    self.isSaved = False

  def application_edit_setup(self):
    self.applicationLayout = QHBoxLayout()
    self.application = QLabel("Application:")
    self.applicationLayout.addWidget(self.application)
    if not self.parent.isDefaultSetting:
      self.applicationEdit = QLineEdit()
      self.applicationEdit.setText(settingsList[self.parent.row][self.parent.applicationColumn])
      self.applicationEdit.setFixedWidth(350)
      self.applicationLayout.addWidget(self.applicationEdit)
    self.layout.addLayout(self.applicationLayout)

  def process_edit_setup(self):
    self.processLayout = QHBoxLayout()
    self.processLabel = QLabel("Process Name:")
    self.processLayout.addWidget(self.processLabel)
    self.processEdit = QLineEdit()
    self.processEdit.setText(settingsList[self.parent.row][self.parent.processColumn])
    self.processEdit.setFixedWidth(350)
    self.processLayout.addWidget(self.processEdit)
    self.layout.addLayout(self.processLayout)

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(500, 282)
    self.thumbnail.setStyleSheet("background-color: black; border: 1px solid black;")
    self.thumbnail.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    update_thumbnail(self, self.parent.row, self.parent.pathColumn)
    self.layout.addWidget(self.thumbnail)
  
  def select_image_button_setup(self):
    self.selectButton = QPushButton("Select Image...")
    self.selectButton.clicked.connect(self.handle_select)
    self.layout.addWidget(self.selectButton)

  def save_button_setup(self):
    self.saveButton = QPushButton("Save Changes")
    self.saveButton.clicked.connect(self.handle_save)
    self.layout.addWidget(self.saveButton)

  def handle_select(self):
    fileDialog = QFileDialog()
    fileDialog.setFileMode(QFileDialog.ExistingFile)
    fileDialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg)")
    fileDialog.setDirectory("/hdd/Wallpapers")
    fileDialog.setWindowTitle("Select an Image")
    if fileDialog.exec():
      self.settingsList[self.parent.row][self.parent.pathColumn] = (fileDialog.selectedFiles()[0])
      update_thumbnail(self, self.parent.row, self.parent.pathColumn)

  def handle_save(self):
    save_settings(self.settingsList)
    self.isSaved = True
    self.close()
