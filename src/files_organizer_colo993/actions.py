"""Copy or move selected files."""

import os
import shutil

class Files:
    """Copy or move selected files to destination folder."""
    def __init__(self, list_of_files, source_path, destination_path):
        self.list_of_files = list_of_files
        self.source_path = source_path
        self.destination_path = destination_path

    def copy(self) -> None:
        """Copy specified list of files."""
        for file in self.list_of_files:
            try:
                shutil.copy(f"{self.source_path}/{file}", 
                            f"{self.destination_path}/{file}")
            except PermissionError:
                print(f"Permission error copying {file} from \
                      {self.source_path} to {self.destination_path}")
            except IOError:
                os.umask(0) # set up 755 chmod permission on created directory
                os.makedirs(os.path.dirname(f"{self.destination_path}/{file}"), 
                            exist_ok=True)
                shutil.copy(f"{self.source_path}/{file}", 
                            f"{self.destination_path}/{file}")
            
    def move(self) -> None:
        """Move specified list of files."""
        for file in self.list_of_files:
            try:
                shutil.move(f"{self.source_path}/{file}", 
                            f"{self.destination_path}/{file}")
            except PermissionError:
                print(f"Permission error moving {file} from \
                      {self.source_path} to {self.destination_path}")
            except IOError:
                os.umask(0) # set up 755 chmod permission on created directory
                os.makedirs(os.path.dirname(f"{self.destination_path}/{file}"), 
                            exist_ok=True)       
                shutil.move(f"{self.source_path}/{file}", 
                            f"{self.destination_path}/{file}")   
