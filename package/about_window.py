import sys
from random import randint

from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QGuiApplication


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("About Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        