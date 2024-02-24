import os
import re

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
        for file in file_names:
            open(os.path.join(tmpdir_path, file), "a").close()
        return files_list
    
    def test_filter_by_extension_jpg(self, files_list_instance):
        result = files_list_instance.filter_by_extension("jpg")
        assert len(result) == 2
        assert all(re.search(r"jp(.*)", file) for file in result)
    
    def test_filter_by_extension_png(self, files_list_instance):
        result = files_list_instance.filter_by_extension("png")
        assert len(result) == 2
        assert all(re.search(r"\.png$", file) for file in result)
    
    def test_filter_by_extension_bmp(self, files_list_instance):
        result = files_list_instance.filter_by_extension("bmp")
        assert len(result) == 2
        assert all(re.search(r"\.bmp$", file) for file in result)
    
    def test_filter_by_extension_invalid_input(self, files_list_instance):
        with pytest.raises(KeyError):
            files_list_instance.filter_by_extension("Invalid_input")
    
    def test_filter_by_name_basic(self, files_list_instance):
        result = files_list_instance.filter_by_name("basic")
        assert len(result) == 3
        assert all(re.search(r"basic", file) for file in result)
    
    def test_filter_by_name_extended(self, files_list_instance):
        result = files_list_instance.filter_by_name("ExtEnded")
        assert len(result) == 3
        assert all(re.search(r"ExtEnded", file) for file in result)
    
    def test_filter_by_name_invalid_input(self, files_list_instance):
        with pytest.raises(TypeError):
            files_list_instance.filter_by_name(1)
    