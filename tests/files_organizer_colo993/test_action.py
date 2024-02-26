import os
import shutil
import tempfile

from files_organizer_colo993 import action

class TestFile:
    
    def test_copy(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
            files_list = ["test_file1.txt", "test_file2.txt", "test_file3.txt"]
            for file in files_list:
                with open(os.path.join(source_dir, file), "w") as f:
                    f.write("Test")
            
            file_object = action.File(files_list, source_dir, dest_dir)
            
            file_object.copy()
            
            copied_files_list = os.listdir(dest_dir)
            assert sorted(copied_files_list) == sorted(files_list)
    
    def test_move(self):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
            files_list = ["test_file1.txt", "test_file2.txt", "test_file3.txt"]
            for file in files_list:
                with open(os.path.join(source_dir, file), "w") as f:
                    f.write("Test")
            
            file_object = action.File(files_list, source_dir, dest_dir)
            
            file_object.move()
            
            moved_files_source = os.listdir(source_dir)
            moved_files_dest =os.listdir(dest_dir)
            assert len(moved_files_source) == 0
            assert sorted(moved_files_dest) == sorted(files_list)
