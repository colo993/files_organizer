import sys

from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout


class HowToUseWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("How To Use Window")
        layout.addWidget(self.label)
        self.setLayout(layout)