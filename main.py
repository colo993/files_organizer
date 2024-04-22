import sys

from PyQt6.QtWidgets import QApplication

from package import main_window


def main():
    """Files organizer main function"""
    files_organizer_app = QApplication([])
    files_organizer_window = main_window.FilesOrganizerWindow()
    files_organizer_window.show()
    sys.exit(files_organizer_app.exec())

if __name__ == "__main__":
    main()
