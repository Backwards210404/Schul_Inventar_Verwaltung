import sys
from PyQt6.QtWidgets import *

from ui import UI
from user import User
sys.path.append(".")
app = QApplication(sys.argv)
ui = UI()
ui.showLoginPage()
sys.exit(app.exec())
