import sys
from PySide2.QtWidgets import QSystemTrayIcon, QMenu
from PySide2.QtGui import QIcon


class SystemTray(QSystemTrayIcon):
    def __init__(self, app):
        super(SystemTray, self).__init__()
        self.app = app
        self.systemTray = QSystemTrayIcon(QIcon(f"{sys.argv[0]}/assets/app_icon.png"))
        self.trayMenu = QMenu()
        self.systemTray.setContextMenu(self.trayMenu)
        self.menu_title_setup()
        self.open_action_setup()
        self.exit_action_setup()
        self.systemTray.show()

    def menu_title_setup(self):
        self.trayMenu.menuTitle = self.trayMenu.addAction("Saharah Paper")
        self.trayMenu.menuTitle.setEnabled(False)
        self.trayMenu.addSeparator()

    def open_action_setup(self):
        self.trayMenu.openAction = self.trayMenu.addAction("Settings")
        self.trayMenu.openAction.triggered.connect(self.handle_open)

    def handle_open(self):
        self.app.mainWindow.show()

    def exit_action_setup(self):
        self.trayMenu.exitAction = self.trayMenu.addAction("Exit")
        self.trayMenu.exitAction.triggered.connect(self.app.quit)
