import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QGuiApplication
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QStatusBar,
    QLabel
)

from package.about_window import AboutWindow
from package.how_to_use_window import HowToUseWindow

WINDOW_SIZE = 255

class FilesOrganizerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()
        self._createMenu()
    
    def _initUI(self):
        self.setWindowTitle("Files Organizer")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
    
    def _createMenu(self):
        toolbar = QToolBar("My main toolbar.")
        self.addToolBar(toolbar)
        
        new_button = QAction("&New", self)
        new_button.triggered.connect(self._mainWindow)
        
        exit_button = QAction("&Exit", self)
        exit_button.triggered.connect(self.close)
        
        how_to_use_button = QAction("&How to use", self)
        how_to_use_button.triggered.connect(self._howtouseWindow)
        
        about_button = QAction("&About", self)
        about_button.triggered.connect(self._aboutWindow)
        
        file_menu = self.menuBar().addMenu("&File")
        file_menu.addAction(new_button)
        file_menu.addSeparator()
        file_menu.addAction(exit_button)
        
        help_menu = self.menuBar().addMenu("&Help")
        help_menu.addAction(how_to_use_button)
        help_menu.addSeparator()
        help_menu.addAction(about_button)
        
    def _mainWindow(self):
        print("newWindow")
    
    def _howtouseWindow(self):
        self.howtouse = HowToUseWindow()
        self.howtouse.show()
        self.howtouse.move(100, 100)
    
    def _aboutWindow(self):
        self.about = AboutWindow()
        self.about.show()
  