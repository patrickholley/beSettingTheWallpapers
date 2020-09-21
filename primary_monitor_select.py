from PySide2.QtWidgets import QRadioButton, QHBoxLayout, QWidget, QLabel
from PySide2.QtCore import Qt
from settings_service import defaultSettings

class PrimaryMonitorSelect(QWidget):
  def __init__(self, parent):
    super(PrimaryMonitorSelect, self).__init__()
    self.parent = parent
    self.layout = QHBoxLayout()
    self.layout.setAlignment(Qt.AlignCenter)
    self.setLayout(self.layout)
    self.label = QLabel("Primary Monitor:")
    self.layout.addWidget(self.label)
    self.radio_buttons_setup()

  def radio_buttons_setup(self):
    self.leftRadioButton = QRadioButton("Left")
    self.leftRadioButton.toggled.connect(self.handle_toggled)
    self.rightRadioButton = QRadioButton("Right")
    self.rightRadioButton.toggled.connect(self.handle_toggled)
    if defaultSettings.list[2][1] == "True":
      self.leftRadioButton.setChecked(True)
    else:
      self.rightRadioButton.setChecked(True)
    self.layout.addWidget(self.leftRadioButton)
    self.layout.addWidget(self.rightRadioButton)

  def handle_toggled(self):
    defaultSettings.list[2][1] = str(self.leftRadioButton.isChecked())
    defaultSettings.write()
