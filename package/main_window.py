import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QAction, QIcon, QGuiApplication
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QToolBar,
    QStatusBar,
    QLabel,
    QFileDialog
)

from package.about_window import AboutWindow
from package.how_to_use_window import HowToUseWindow

WINDOW_SIZE = 255

class FilesOrganizerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()
        self._createMenu()
        self._createWidgets()
    
    def _initUI(self):
        self.setWindowTitle("Files Organizer")
        self.setGeometry(300, 300, 300, 300)
        
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
    
    def _createWidgets(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        button_source_dir = QPushButton("Select source directory")
        button_destination_dir = QPushButton("Select destination directory")
        button_source_dir.clicked.connect(self.source_directory)
        button_destination_dir.clicked.connect(self.destination_directory)
        
        self.label_source_dir = QLabel()
        #label_source_dir.setText(x)
        self.label_destination_dir = QLabel()
        #label_destination_dir.setText()
        
        layout.addWidget(button_source_dir)
        layout.addWidget(self.label_source_dir)
        layout.addWidget(button_destination_dir)
        layout.addWidget(self.label_destination_dir)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def source_directory(self):
        source_directory = QFileDialog.getExistingDirectory(self, "Source directory",
                                             self.label_source_dir.text())
        if source_directory:
            self.label_source_dir.setText(source_directory)
    
    def destination_directory(self):
        destination_directory = QFileDialog.getExistingDirectory(self, "Source directory",
                                             self.label_destination_dir.text())
        if destination_directory:
            self.label_destination_dir.setText(destination_directory)
        
    def _mainWindow(self):
        print("newWindow")
    
    def _howtouseWindow(self):
        self.howtouse = HowToUseWindow()
        self.howtouse.show()     
    
    def _aboutWindow(self):
        self.about = AboutWindow()
        self.about.show()
  