import sys

from datetime import datetime
from PyQt6 import QtCore
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
    QCalendarWidget,
    QRadioButton,
    QButtonGroup 
)

from package.about_window import AboutWindow
from package.how_to_use_window import HowToUseWindow
from files_organizer_colo993 import actions, filters

WINDOW_SIZE = 255

class FilesOrganizerWindow(QMainWindow):
    """Files organizer main window with widgets to copy or move files."""
    def __init__(self):
        """Initis FilesOrganizer window with GUI."""
        super().__init__()
        self._init_ui()
        self._create_menu()
        self._create_widgets()
    
    def _init_ui(self):
        """Set window title and size."""
        self.setWindowTitle("Files Organizer")
        self.setGeometry(800, 800, 500, 600)
        
    def _create_menu(self):
        """Add menu bar."""
        self._toolbar = QToolBar("My main toolbar.")
        self.addToolBar(self._toolbar)
        
        self._reset_to_default_button = QAction("&New", self)
        self._reset_to_default_button.triggered.connect(
                                                    self._restartMainWindow)
        
        self._exit_button = QAction("&Exit", self)
        self._exit_button.triggered.connect(self.close)
        
        self._how_to_use_button = QAction("&How to use", self)
        self._how_to_use_button.triggered.connect(self._howtouseWindow)
        
        self._about_button = QAction("&About", self)
        self._about_button.triggered.connect(self._aboutWindow)
        
        self._file_menu = self.menuBar().addMenu("&File")
        self._file_menu.addAction(self._reset_to_default_button)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._exit_button)
        
        self._help_menu = self.menuBar().addMenu("&Help")
        self._help_menu.addAction(self._how_to_use_button)
        self._help_menu.addSeparator()
        self._help_menu.addAction(self._about_button)
    
    def _create_widgets(self):
        """Add widgets."""
        widget = QWidget()
        main_layout = QVBoxLayout()
        self._checkbox_layout_name = QVBoxLayout() 
        self._checkbox_layout_extension = QVBoxLayout() 
        self._checkbox_layout_date = QVBoxLayout()
        radiobutton_layout = QGridLayout()
        summary_layout = QVBoxLayout()
        
        button_source_dir = QPushButton("Select source directory")
        button_destination_dir = QPushButton("Select destination directory")
        button_source_dir.clicked.connect(self._get_source_directory)
        button_destination_dir.clicked.connect(self._get_destination_directory)
        
        self._label_source_dir = QLabel()
        self._label_destination_dir = QLabel()
        
        self._filter_by_name_checkbox = QCheckBox("Filter by name", self)
        self._filter_by_name_checkbox.toggled.connect(self._get_file_name)
        self._filter_by_extension_checkbox = QCheckBox("Filter by extension", 
                                                       self)
        self._filter_by_extension_checkbox.toggled.connect(self._get_extension)
        self._filter_by_date_checkbox = QCheckBox("Filter by date range", self)
        self._filter_by_date_checkbox.toggled.connect(self._get_dates)
        
        merged_group = QButtonGroup(widget)
        radiobutton_union = QRadioButton("Union")
        merged_group.addButton(radiobutton_union, 0)
        radiobutton_union.toggled.connect(self._get_merged_type)
        radiobutton_intersection = QRadioButton("Intersection")
        merged_group.addButton(radiobutton_intersection, 1)
        radiobutton_intersection.toggled.connect(self._get_merged_type)
        
        action_group = QButtonGroup(widget)
        radiobutton_copy = QRadioButton("Copy")
        action_group.addButton(radiobutton_copy, 2)
        radiobutton_copy.toggled.connect(self._get_action_type)
        radiobutton_move = QRadioButton("Move")
        action_group.addButton(radiobutton_move, 3)
        radiobutton_move.toggled.connect(self._get_action_type)
        
        summary_label = QLabel()
        summary_label.setText("Files to be copied or moved:")
        files_list_label = QLabel()
        files_list_label.setText(self._get_list_of_files())
        run_action_button = QPushButton("RUN")
        run_action_button.clicked.connect(self._start_process)
        
        main_layout.addWidget(button_source_dir)
        main_layout.addWidget(self._label_source_dir)
        main_layout.addWidget(button_destination_dir)
        main_layout.addWidget(self._label_destination_dir)
        
        main_layout.addLayout(self._checkbox_layout_name)
        self._checkbox_layout_name.addWidget(self._filter_by_name_checkbox)
        
        main_layout.addLayout(self._checkbox_layout_extension)
        self._checkbox_layout_extension.addWidget(
                                            self._filter_by_extension_checkbox)
        
        main_layout.addLayout(self._checkbox_layout_date)
        self._checkbox_layout_date.addWidget(self._filter_by_date_checkbox)
        
        main_layout.addLayout(radiobutton_layout)
        radiobutton_layout.addWidget(radiobutton_union, 0, 0)
        radiobutton_layout.addWidget(radiobutton_intersection, 0, 1)
        radiobutton_layout.addWidget(radiobutton_copy, 1, 0)
        radiobutton_layout.addWidget(radiobutton_move, 1, 1)
        
        main_layout.addLayout(summary_layout)
        summary_layout.addWidget(summary_label)
        summary_layout.addWidget(files_list_label)
        summary_layout.addWidget(run_action_button)
        
        main_layout.addStretch()
        main_layout.setContentsMargins(10, 10, 20, 30)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    def _get_source_directory(self):
        """Obtain source directory path and print it out on the screen."""
        source_directory = QFileDialog.getExistingDirectory(
                                            self, 
                                            "Source directory",
                                            self._label_source_dir.text())
        if source_directory:
            self._label_source_dir.setText(source_directory)
    def _get_destination_directory(self):
        """Obtain destination directory path and print it out on the screen."""
        destination_directory = QFileDialog.getExistingDirectory(
                                            self, 
                                            "Destination directory",
                                            self._label_destination_dir.text())
        if destination_directory:
            self._label_destination_dir.setText(destination_directory)
        
    
    def _get_file_name(self):
        """Activate line editor when Checkbox filter_by_name_widget is checked
        to type file name for filtering.
        """
        if self._filter_by_name_checkbox.isChecked():
            self._filter_by_name_widget = QLineEdit()
            self._checkbox_layout_name.addWidget(self._filter_by_name_widget)
        else:
            i = self._checkbox_layout_name.indexOf(self._filter_by_name_widget)
            self._checkbox_layout_name.takeAt(i)
            self._filter_by_name_widget.deleteLater()
    
    def _get_extension(self):
        """Activate combobox with list of extensions when Checkbox 
        filter_by_extension is checked to chose type of extension 
        for filtering.
        """
        if self._filter_by_extension_checkbox.isChecked():
            self._filter_by_extension_widget = QComboBox()
            self._filter_by_extension_widget.addItems(["jpg", "png", "bmp"])
            self._checkbox_layout_extension.addWidget(
                                            self._filter_by_extension_widget)
        else:
            i = self._checkbox_layout_extension.indexOf(
                                            self._filter_by_extension_widget)
            self._checkbox_layout_extension.takeAt(i)
            self._filter_by_extension_widget.deleteLater()

    def _get_dates(self):
        """Activate datetime widget when Checkbox filter_by_date is 
        checked to chose datetime range for filtering.
        """
        if self._filter_by_date_checkbox.isChecked():
            self._from_date_label = QLabel()
            self._from_date_label.setText("From date time:")    
            self._filter_from_date_widget = QDateTimeEdit(calendarPopup=True,
                                                     dateTime=datetime.now())
            self._to_date_label = QLabel()
            self._to_date_label.setText("To date time:")  
            self._filter_to_date_widget = QDateTimeEdit(calendarPopup=True, 
                                                   dateTime=datetime.now()) 
            self._checkbox_layout_date.addWidget(self._from_date_label)
            self._checkbox_layout_date.addWidget(self._filter_from_date_widget)
            self._checkbox_layout_date.addWidget(self._to_date_label)
            self._checkbox_layout_date.addWidget(self._filter_to_date_widget)
        else:
            list_of_date_widgets = [self._filter_to_date_widget, 
                                    self._filter_from_date_widget, 
                                    self._to_date_label, 
                                    self._from_date_label]
            for date_widget in list_of_date_widgets:
                widget_index = self._checkbox_layout_date.indexOf(date_widget)
                self._checkbox_layout_date.takeAt(widget_index)
                date_widget.deleteLater()
    
    def _get_merged_type(self):
        """Obtain value of radio buttons Union or Intersection."""
        self._merged_type = self.sender()
        
    def _get_action_type(self):
        """Obtain value of radio buttons Copy or Move."""
        self._action_type = self.sender()
    
    def _get_list_of_files(self):
        """Return list of files to be copied or moved according to
        chosen option by the user.
        """
        #TODO
        return "List of files here!!!"
    
    def _start_process(self):
        """Copy or move selected files after clicking the button."""
        try:
            files_list = filters.FilesList(self._label_source_dir.text())

            if self._filter_by_name_checkbox.isChecked():
                filtered_by_name = files_list.filter_by_name(
                                                self._filter_by_name_widget.text()) 
            else:
                filtered_by_name = None
                
            if self._filter_by_extension_checkbox.isChecked():
                filtered_by_extension = files_list.filter_by_extension(
                                    self._filter_by_extension_widget.currentText())
            else:
                filtered_by_extension = None
                
            if self._filter_by_date_checkbox.isChecked():
                from_date = str(self._filter_from_date_widget.dateTime().
                                            toPyDateTime().replace(microsecond=0))
                to_date = str(self._filter_to_date_widget.dateTime().
                                            toPyDateTime().replace(microsecond=0))
                
                from_date_converted = datetime.strptime(from_date, 
                                                        "%Y-%m-%d %H:%M:%S")
                to_date_converted = datetime.strptime(to_date, 
                                                        "%Y-%m-%d %H:%M:%S")
    
                filtered_by_date = files_list.filter_by_date_creation(
                                            from_date_converted, to_date_converted)
            else:
                filtered_by_date = None

            all_files = files_list.get(self._merged_type.text().lower(), 
                                    filtered_by_name, 
                                    filtered_by_extension, 
                                    filtered_by_date)
            
            file = actions.Files(all_files, 
                                 self._label_source_dir.text(),
                                 self._label_destination_dir.text())
    
            if self._action_type.text() == 'Copy':
                file.copy()
            elif self._action_type.text() == 'Move':
                file.move()

            print(f'Merge type: {self._merged_type.text().lower()}')
            print(f'list of files: {all_files}')
        except AttributeError:
            print('AttributeError')
        
        
        
    def _restartMainWindow(self):
        """Reset FilesOrganizer main window to initial stage."""
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)
    
    def _howtouseWindow(self):
        """Open HowToUse window."""
        self.howtouse = HowToUseWindow()
        self.howtouse.show()     
    
    def _aboutWindow(self):
        """Open About window."""
        self.about = AboutWindow()
        self.about.show()
  