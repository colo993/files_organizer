import sys

from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout


class HowToUseWindow(QWidget):
    """HowToUse window with manual and information about features 
    of the application.
    """
    def __init__(self):
        """Initis HowToUse window with GUI."""
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("How To Use Window")
        layout.addWidget(self.label)
        self.setLayout(layout)