import os
import shutil
from datetime import datetime
import time
import re
import json

class File:
    """Copy or move selected files to destination folder"""
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def _filter_by_extension(self, type_of_extension) -> list(): 
        """Select extension of a file"""
        with open('files_organizer/extensions_list.json', 'r') as file:
            extensions = json.load(file)
            
        return [file for file in os.listdir(path=self.source_path) if 
                re.search(extensions[type_of_extension], file.lower())]
    
    def _filter_by_name(self, file_name_to_search) -> list():
        """Find the files which matches the given word"""
        return [file for file in os.listdir(path=self.source_path) if 
                file_name_to_search in file]
    
    def _filter_by_date_creation(self, from_time, to_time) -> list():
        """Find the files created in between the given datetime range"""
        files_in_datetime_range = []
        for file in os.listdir(path=self.source_path):
            time_in_epoch = os.path.getmtime(f"{self.source_path}/{file}")
            time_in_str =  time.ctime(time_in_epoch)
            datetime_creation = datetime.strptime(time_in_str, "%a %b %d %H:%M:%S %Y")
            if datetime_creation >= from_time and datetime_creation <= to_time:
                files_in_datetime_range.append(file)
            
        return files_in_datetime_range

    def _get_list_of_files_intersection(self, extensions=None, names=None, dates=None) -> list():
        entry_list = [extensions, names, dates] 
        print(f"Entry_list: {entry_list}")
        filtered_list = [x for x in entry_list if x is not None]
        
        return list(set.intersection(*map(set,filtered_list)))
    
    def _get_list_of_files_union(self, extensions=None, names=None, dates=None) -> list():
        entry_list = [extensions, names, dates] 
        print(f"Entry_list: {entry_list}")
        filtered_list = [x for x in entry_list if x is not None]
        
        return list(set.union(*map(set,filtered_list)))

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
    file = File('/home/colo/files_organizer/sandbox', '/home/colo/files_organizer/files_test/')
    print(file._get_list_of_files_union(file._filter_by_extension('png'),
                                  file._filter_by_name('test'),
                                  file._filter_by_date_creation(datetime(2024, 2, 4, 00, 00, 00), 
                                                          datetime(2024, 2, 8, 12, 00, 00))))
    
    print(file._get_list_of_files_or(file._filter_by_extension('png'),
                                  file._filter_by_name('test'),
                                  file._filter_by_date_creation(datetime(2024, 2, 4, 00, 00, 00), 
                                                          datetime(2024, 2, 8, 12, 00, 00))))
    