import sys

from datetime import datetime
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
    QFileDialog,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QCalendarWidget
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
        self.setGeometry(800, 800, 500, 600)
        
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
        self.widget = QWidget()
        main_layout = QVBoxLayout()
        self.checkbox_layout_name = QVBoxLayout() 
        self.checkbox_layout_extension = QVBoxLayout() 
        self.checkbox_layout_date = QVBoxLayout()
        
        button_source_dir = QPushButton("Select source directory")
        button_destination_dir = QPushButton("Select destination directory")
        button_source_dir.clicked.connect(self.source_directory)
        button_destination_dir.clicked.connect(self.destination_directory)
        
        self.label_source_dir = QLabel()
        self.label_destination_dir = QLabel()
        
        self.filter_by_name_checkbox = QCheckBox("Filter by name", self)
        self.filter_by_name_checkbox.toggled.connect(self.filter_by_name)
        self.filter_by_extension_checkbox = QCheckBox("Filter by extension", self)
        self.filter_by_extension_checkbox.toggled.connect(self.filter_by_extension)
        self.filter_by_date_checkbox = QCheckBox("Filter by date range", self)
        self.filter_by_date_checkbox.toggled.connect(self.filter_by_date)
        
        main_layout.addWidget(button_source_dir)
        main_layout.addWidget(self.label_source_dir)
        main_layout.addWidget(button_destination_dir)
        main_layout.addWidget(self.label_destination_dir)
        
        main_layout.addLayout(self.checkbox_layout_name)
        self.checkbox_layout_name.addWidget(self.filter_by_name_checkbox)
        
        main_layout.addLayout(self.checkbox_layout_extension)
        self.checkbox_layout_extension.addWidget(self.filter_by_extension_checkbox)
        
        main_layout.addLayout(self.checkbox_layout_date)
        self.checkbox_layout_date.addWidget(self.filter_by_date_checkbox)
        
        main_layout.addStretch()
        main_layout.setContentsMargins(10, 10, 20, 30)
        self.widget.setLayout(main_layout)
        self.setCentralWidget(self.widget)
        
    def source_directory(self):
        source_directory = QFileDialog.getExistingDirectory(
                                            self, 
                                            "Source directory",
                                            self.label_source_dir.text())
        if source_directory:
            self.label_source_dir.setText(source_directory)
    
    def destination_directory(self):
        destination_directory = QFileDialog.getExistingDirectory(
                                            self, 
                                            "Destination directory",
                                            self.label_destination_dir.text())
        if destination_directory:
            self.label_destination_dir.setText(destination_directory)
    
    def filter_by_name(self):
        if self.filter_by_name_checkbox.isChecked():
            self.filter_by_name = QLineEdit()
            self.checkbox_layout_name.addWidget(self.filter_by_name)
        else:
            i = self.checkbox_layout_name.indexOf(self.filter_by_name)
            self.checkbox_layout_name.takeAt(i)
            self.filter_by_name.deleteLater()
    
    def filter_by_extension(self):
        if self.filter_by_extension_checkbox.isChecked():
            self.filter_by_extension = QComboBox()
            self.filter_by_extension.addItems(["jpg", "png", "bmp"])
            self.checkbox_layout_extension.addWidget(self.filter_by_extension)
        else:
            i = self.checkbox_layout_extension.indexOf(self.filter_by_extension)
            self.checkbox_layout_extension.takeAt(i)
            self.filter_by_extension.deleteLater()

    def filter_by_date(self):
        if self.filter_by_date_checkbox.isChecked():
            self.to_date_label = QLabel()
            self.to_date_label.setText("From date time:")
            self.filter_by_to_date = QDateTimeEdit(calendarPopup=True, 
                                                   dateTime=datetime.now())
            self.from_date_label = QLabel()
            self.from_date_label.setText("To date time:")
            self.filter_by_from_date = QDateTimeEdit(calendarPopup=True,
                                                     dateTime=datetime.now())
            self.checkbox_layout_date.addWidget(self.to_date_label)
            self.checkbox_layout_date.addWidget(self.filter_by_to_date)
            self.checkbox_layout_date.addWidget(self.from_date_label)
            self.checkbox_layout_date.addWidget(self.filter_by_from_date)
            
        else:
            widgets = [self.filter_by_to_date, self.filter_by_from_date, 
                       self.to_date_label, self.from_date_label]
            
            for widget in widgets:
                widget_index = self.checkbox_layout_date.indexOf(widget)
                self.checkbox_layout_date.takeAt(widget_index)
                widget.deleteLater()
        
    def _mainWindow(self):
        print("newWindow")
    
    def _howtouseWindow(self):
        self.howtouse = HowToUseWindow()
        self.howtouse.show()     
    
    def _aboutWindow(self):
        self.about = AboutWindow()
        self.about.show()
  