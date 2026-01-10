import sys
from PyQt6.QtWidgets import *
from uicontroller import UIController
sys.path.append(".")
app = QApplication(sys.argv)
controller = UIController()

sys.exit(app.exec())
