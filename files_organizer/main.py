import os
import shutil

class File:
    """Copy or move selected files to destination folder"""
    def __init__(self, source_path, destination_path, index_of_extension):
        self.source_path = source_path
        self.destination_path = destination_path
        self.index_of_extension = index_of_extension

    def _get_extension(self) -> list(): #HOW TO SELECT EXTENSION?!
        """Select extension of a file to being moved or copied"""
        extensions_list = ['.jpeg', '.png', '.txt']
        return extensions_list
    
    def _get_file_name(self):
        pass
    
    def _get_date_creation(self):
        pass

    def _get_list_of_files(self) -> list():
        return [file for file in os.listdir(path=self.source_path) if 
                self.get_extension()[self.index_of_extension] in file.lower()]

    def copy(self) -> None:
        for file in self._get_list_of_files():
            try:
                shutil.copy(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")
            except IOError as error:
                os.umask(0)
                os.makedirs(os.path.dirname(self.destination_path))
                shutil.copy(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")

    def move(self) -> None:
        for file in self.get_list_of_files():
            try:
                shutil.move(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")
            except IOError as error:
                os.umask(0)
                os.makedirs(os.path.dirname(self.destination_path))
                shutil.move(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")   


if __name__ == "__main__":
    file = File('sandbox', 'files_test/', 2)
    print(file.get_extension())
    file.copy()
    