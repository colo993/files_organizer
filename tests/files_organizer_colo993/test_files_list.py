import os
import re
from datetime import datetime, timedelta

import pytest

from files_organizer_colo993 import filters
from files_organizer_colo993 import action

# Mock extensions data for testing
def get_extensions_data():
    return {
        "jpg" : r"jp(.*)",
        "png" : r"png$",
        "bmp" : r"bmp$"
    }


class TestFilesList:
    @pytest.fixture
    def files_list_instance(self, tmpdir):
        tmpdir_path = str(tmpdir)
        files_list = filters.FilesList(tmpdir_path)
        file_names = ["basic_file1.jpg", "ExtEnded_file2.jpg", 
                      "basic_file3.png", "ExtEnded_file4.png", 
                      "basic_file5.bmp", "ExtEnded_file6.bmp"
        ]
        for i, file in enumerate(file_names, start=1):
            file_path = os.path.join(tmpdir_path, file)
            with open(file_path, "a") as f:
               f.write('Test')
            os.utime(file_path, (i, i))
            
        return files_list
    
    def test_filter_by_extension_jpg(self, files_list_instance):
        result = files_list_instance.filter_by_extension("jpg")
        assert len(result) == 2
        assert all(re.search(r"jp(.*)", file) for file in result)
    
    def test_filter_by_extension_invalid_input(self, files_list_instance):
        with pytest.raises(KeyError):
            files_list_instance.filter_by_extension("Invalid_input")
    
    def test_filter_by_name_basic(self, files_list_instance):
        result = files_list_instance.filter_by_name("basic")
        assert len(result) == 3
        assert all(re.search(r"basic", file) for file in result)
    
    def test_filter_by_name_invalid_input(self, files_list_instance):
        with pytest.raises(TypeError):
            files_list_instance.filter_by_name(1)
    
    def test_filter_by_date_creation(self, files_list_instance):
        from_time = datetime.fromtimestamp(1)
        print(from_time)
        to_time = datetime.fromtimestamp(2)
        print(to_time)
        result = files_list_instance.filter_by_date_creation(from_time, to_time)
        assert len(result) == 2
        assert ['basic_file1.jpg', 'ExtEnded_file2.jpg'] == result
    
    def test_filter_by_date_creation_invalid_input(self, files_list_instance):
        with pytest.raises(TypeError):
            files_list_instance.filter_by_date_creation("Invalid", 123)
            
    def test_get_intersection(self, files_list_instance):
        extension = files_list_instance.filter_by_extension('png')
        names = files_list_instance.filter_by_name('ExtEnded')
        dates = files_list_instance.filter_by_date_creation(
                                                    datetime.fromtimestamp(1), 
                                                    datetime.fromtimestamp(6))
        assert files_list_instance.get('intersection', 
                                       extension, 
                                       names, 
                                       dates) == ["ExtEnded_file4.png"]
    
    def test_get_union(self, files_list_instance):
        extension = files_list_instance.filter_by_extension('png')
        names = files_list_instance.filter_by_name('ExtEnded')
        dates = files_list_instance.filter_by_date_creation(
                                                    datetime.fromtimestamp(3), 
                                                    datetime.fromtimestamp(4))
        result = files_list_instance.get('union', extension, names, dates)
        result.sort()
        assert result == ['ExtEnded_file2.jpg', 'ExtEnded_file4.png', 
                          'ExtEnded_file6.bmp', 'basic_file3.png']
        