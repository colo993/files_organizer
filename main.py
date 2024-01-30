import os
import shutil

class File:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
    
    def copy(self):
        try:
            shutil.copy(self.source_path, self.destination_path)
        except IOError as error:
            os.makedirs(os.path.dirname(self.destination_path))
            shutil.copy(self.source_path, self.destination_path)
    
    def move(self):
        try:
            shutil.move(self.source_path, self.destination_path)
        except IOError as error:
            os.makedirs(os.path.dirname(self.destination_path))
            shutil.move(self.source_path, self.destination_path)   