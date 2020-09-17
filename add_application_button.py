from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QIcon
from edit_wallpaper_dialog import EditWallpaperDialog
from settings_service import applicationSettings
from wallpaper_box import WallpaperBox

class AddApplicationButton(QPushButton):
  def __init__(self, parent):
    super(AddApplicationButton, self).__init__()
    self.parent = parent
    self.isDefaultSetting = False
    self.setText("Add Application")
    self.setIcon(QIcon("assets/add.svg"))
    self.clicked.connect(self.handle_add_application)
    self.setFixedWidth(300)
  
  def handle_add_application(self):
    self.path = ""
    self.application = ""
    self.process = ""
    self.editWallpaperDialog = EditWallpaperDialog(self)
    self.editWallpaperDialog.show()

  def handle_save(self, path, application, process):
    applicationSettings.list.append([application, path, process])
    applicationSettings.write()
    self.parent.applicationBoxes.append(WallpaperBox(len(applicationSettings.list) - 1))
    self.parent.application_grid_setup()
    self.close()
