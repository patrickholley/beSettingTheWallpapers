import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QFileDialog, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon

class Window(QMainWindow):
  def __init__(self):
    super(Window, self).__init__()
    self.setGeometry(200, 200, 200, 50)
    self.setWindowTitle("Be Setting the Wallpapers")
    self.setWindowIcon(QIcon('beSettingTheWallpaper.png'))
    self.hbox = QVBoxLayout() 
    self.create_filedialog_button()
    self.label = QLabel(self)
    self.label.adjustSize()
    self.hbox.addChildWidget(self.label)
    self.show()

  def create_filedialog_button(self):
    btn = QPushButton("Select Image", self)
    btn.clicked.connect(self.show_file_dialog)
    btn.move(25, 10)
    btn.resize(150, 30)
  
  def show_file_dialog(self):
    dlg = QFileDialog(self)
    dlg.setFixedSize(320, 500)
    dlg.setFileMode(QFileDialog.ExistingFile)
    dlg.setNameFilter("Images (*.png *.xpm *.jpg)")
    dlg.setDirectory("/hdd/Wallpapers")
    dlg.setWindowTitle("Select an Image")
    if dlg.exec():
      self.show_image(dlg.selectedFiles()[0])

  def show_image(self, imagePath):
    pixmap = QPixmap(imagePath).scaledToWidth(1000)
    self.label.setPixmap(pixmap)
    self.label.resize(pixmap.size().width(), pixmap.size().height())
    self.resize(pixmap.size().width(), pixmap.size().height())

def run():
  app = QApplication(sys.argv)
  MainWindow = Window()
  sys.exit(app.exec_())

run()
