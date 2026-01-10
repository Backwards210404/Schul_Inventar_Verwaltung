import sys
from PyQt6.QtWidgets import *
from ui import UI
from uicontroller import UIController
from user import User
sys.path.append(".")
app = QApplication(sys.argv)
controller = UIController()

sys.exit(app.exec())
