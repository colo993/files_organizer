"""Filtered files by multiple conditions and return unified or 
intersectioned list of selected files
"""

import json
import os
import time
from datetime import datetime
import re

from files_organizer_colo993 import get_extensions_data

class FilesList:
    MISSING_SOURCE_PATH_INFO = "Source path was not provided."
    """Filter list files by different options."""
    def __init__(self, source_path):
        self.source_path = source_path
    
    def filter_by_name(self, file_name_to_search) -> list:
        """Find the files which matches the given word."""
        try:
            return [file for file in os.listdir(path=self.source_path) if 
                    file_name_to_search in file and file_name_to_search]
        except FileNotFoundError:
            print(self.MISSING_SOURCE_PATH_INFO)
    
    def filter_by_extension(self, type_of_extension) -> list: 
        """Select extension of a file"""   
        try:
            return [file for file in os.listdir(path=self.source_path) if 
                re.search(f"{get_extensions_data()[type_of_extension]}$",
                          file.lower())]
        except FileNotFoundError:
            print(self.MISSING_SOURCE_PATH_INFO)
    
    def filter_by_date_creation(self, from_time, to_time) -> list:
        """Find the files created in between the given datetime range."""
        files_in_datetime_range = []
        try:
            for file in os.listdir(path=self.source_path):
                time_in_epoch = os.path.getmtime(f"{self.source_path}/{file}")
                time_in_str =  time.ctime(time_in_epoch)
                datetime_creation = datetime.strptime(time_in_str, 
                                                    "%a %b %d %H:%M:%S %Y")
                if datetime_creation >= from_time and datetime_creation \
                    <= to_time:
                    files_in_datetime_range.append(file)  
            return files_in_datetime_range
        except FileNotFoundError:
            print(self.MISSING_SOURCE_PATH_INFO)

    def get(self, option, names=None, extensions=None, dates=None) -> list:
        """Return files present in all lists or files from all lists
        filtered by one or multiple conditions.
        """
        entry_list = [names, extensions, dates] 
        filtered_list = [x for x in entry_list if x is not None]
        try:
            if option == 'intersection':
                return list(set.intersection(*map(set,filtered_list)))
            elif option == 'union':
                return list(set.union(*map(set,filtered_list)))    
        except TypeError:
            print("No fitered options were provided.")
