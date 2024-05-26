import sys
from random import randint

from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication


class AboutWindow(QWidget):
    """About window with general information about current version
    of the applciation.
    """
    def __init__(self):
        """Initis About window with GUI."""
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("About Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        