import sys
from pathlib import Path
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QHBoxLayout, QMessageBox
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

def update_thumbnail(self):
  if self.path != "":
    pixmap = QPixmap(self.path)
    if pixmap.isNull():
      criticalMessageBox = QMessageBox()
      criticalMessageBox.critical(
        None,
        "Invalid Image",
        f"Image at path {self.path} could not be found.",
        criticalMessageBox.Close
      )
    else:
      aspectRatio = pixmap.size().width() / pixmap.size().height()
      if aspectRatio > 1.78:
        scaledPixmap = pixmap.scaledToWidth(self.thumbnail.size().width())
      else:
        scaledPixmap = pixmap.scaledToHeight(self.thumbnail.size().height())
      self.thumbnail.setPixmap(scaledPixmap)

class EditWallpaperDialog(QDialog):
  def __init__(self, parent):
    super(EditWallpaperDialog, self).__init__()
    self.setWindowTitle("Edit Wallpaper")
    self.isSaved = False
    self.parent = parent
    self.path = self.parent.path
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)
    self.thumbnail_setup()
    self.application_edit_setup()
    if not self.parent.isDefaultSetting:
      self.process_edit_setup()
    self.select_image_button_setup()
    self.save_and_cancel_buttons_setup()
    self.adjustSize()
    self.setFixedSize(self.size())

  def closeEvent(self, event):
    if self.isSaved:
      event.accept()
    else:
      confirmMessageBox = QMessageBox()
      confirmClose = confirmMessageBox.question(
        self,
        "Confirm Cancel",
        "Any changes made will not be saved. Cancel anyways?",
        confirmMessageBox.No,
        confirmMessageBox.Yes
      )

      if confirmClose == confirmMessageBox.Yes:
        event.accept()
      else:
        event.ignore()

  def application_edit_setup(self):
    applicationValue = self.parent.application
    self.applicationLayout = QHBoxLayout()
    self.applicationLayout.setAlignment(Qt.AlignCenter)
    self.application = QLabel(applicationValue if self.parent.isDefaultSetting else "Application:")
    self.applicationLayout.addWidget(self.application)
    if not self.parent.isDefaultSetting:
      self.applicationEdit = QLineEdit()
      self.applicationEdit.setText(applicationValue)
      self.applicationEdit.setFixedWidth(350)
      self.applicationLayout.addWidget(self.applicationEdit)
    self.layout.addLayout(self.applicationLayout)

  def process_edit_setup(self):
    self.processLayout = QHBoxLayout()
    self.processLabel = QLabel("Process Name:")
    self.processLayout.addWidget(self.processLabel)
    self.processEdit = QLineEdit()
    self.processEdit.setText(self.parent.process)
    self.processEdit.setFixedWidth(350)
    self.processLayout.addWidget(self.processEdit)
    self.layout.addLayout(self.processLayout)

  def thumbnail_setup(self):
    self.thumbnail = QLabel()
    self.thumbnail.setFixedSize(500, 282)
    self.thumbnail.setStyleSheet("background-color: black; border: 1px solid black;")
    self.thumbnail.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    update_thumbnail(self)
    self.layout.addWidget(self.thumbnail)
  
  def select_image_button_setup(self):
    self.selectButton = QPushButton("Select Image...")
    self.selectButton.setIcon(QIcon(f"{sys.argv[0]}/assets/image.svg"))
    self.selectButton.clicked.connect(self.handle_select)
    self.layout.addWidget(self.selectButton)

  def save_and_cancel_buttons_setup(self):
    buttonsLayout = QHBoxLayout()
    self.saveButton = QPushButton("Save Changes")
    self.saveButton.setIcon(QIcon(f"{sys.argv[0]}/assets/save.svg"))
    self.saveButton.clicked.connect(self.handle_save)
    buttonsLayout.addWidget(self.saveButton)
    self.cancelButton = QPushButton("Cancel")
    self.cancelButton.setIcon(QIcon(f"{sys.argv[0]}/assets/cancel.svg"))
    self.cancelButton.clicked.connect(self.close)
    buttonsLayout.addWidget(self.cancelButton)
    self.layout.addLayout(buttonsLayout)

  def handle_select(self):
    fileDialog = QFileDialog()
    fileDialog.setFileMode(QFileDialog.ExistingFile)
    fileDialog.setNameFilter("Images (*.png *.xpm *.jpg *.jpeg)")
    fileDialog.setDirectory(f"{str(Path.home())}/Pictures")
    fileDialog.setWindowTitle("Select an Image")
    if fileDialog.exec_():
      self.path = fileDialog.selectedFiles()[0]
      update_thumbnail(self)

  def handle_save(self):
    handleSaveArgs = [self.path]
    if not self.parent.isDefaultSetting:
      handleSaveArgs.extend([self.applicationEdit.text(), self.processEdit.text()])
    someArgIsInvalid = any(arg == "" for arg in handleSaveArgs)
    if someArgIsInvalid:
      errorDialog = QMessageBox.critical(
        self,
        "Empty Fields",
        "Cannot save with any field empty.",
        QMessageBox.StandardButton.Close
      )
    else:
      self.parent.handle_save(*handleSaveArgs)
      self.isSaved = True
      self.close()
