import os
import shutil

class File:
    """Copy or move selected files to destination folder"""
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
    
    def get_extension(self, index_of_extension): #HOW TO SELECT EXTENSION?!
        """Select extension of a file to being moved or copied"""
        extensions_list = ['.jpeg', '.png', '.txt']
        return extensions_list[index_of_extension]
            
    def get_list_of_files(self):
        return [file for file in os.listdir(path=self.source_path) if 
                self.get_extension(1) in file.lower()]
    
    def copy(self):
        for file in self.get_list_of_files():
            try:
                shutil.copy(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")
            except IOError as error:
                print(f"Error: {error}")
                os.makedirs(self.destination_path)
                shutil.copy(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")
    
    def move(self):
        for file in self.get_list_of_files():
            try:
                shutil.move(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")
            except IOError as error:
                print(f"Error: {error}")
                os.makedirs(self.destination_path)
                shutil.move(f"{self.source_path}/{file}", f"{self.destination_path}/{file}")   
            

if __name__ == "__main__":
    file = File('sandbox', '/home/colo/photos_organizer/files_test')
    print(file.get_extension(1))
    file.copy()
    #os.makedirs(os.path.dirname('test'))
    
    


    