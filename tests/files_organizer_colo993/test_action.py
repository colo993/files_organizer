import os
import shutil
import tempfile

import pytest

from files_organizer_colo993 import action


class TestFile:
    @pytest.fixture
    def mock_files(self, tmpdir):
        """Create mock files for testing."""
        files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in files:
            path = tmpdir.join(file)
            path.write("")
        return tmpdir

    @pytest.fixture
    def file_instance(self, tmpdir):
        """Initialize File object for testing."""
        source_path = str(tmpdir)
        destination_path = str(tmpdir.join("destination"))
        os.makedirs(destination_path)  # Create a destination directory
        list_of_files = ["file1.txt", "file2.txt"]
        for file in list_of_files:
            file_path = os.path.join(source_path, file)
            with open(file_path, "w") as f:
                f.write("Test content")
        return action.File(list_of_files, source_path, destination_path)

    def test_copy(self, file_instance):
        """Test copy method."""
        file_instance.copy()
        destination_files = os.listdir(file_instance.destination_path)
        assert len(destination_files) == 2
        assert all(file in destination_files for file in file_instance.list_of_files)

    def test_copy_no_permissions(self, file_instance):
        """Test copy method when user has no permissions in destination folder."""
        os.chmod(file_instance.destination_path, 0o400)

        with pytest.raises(IOError):
            file_instance.copy()

    def test_move(self, file_instance):
        """Test move method."""
        file_instance.move()
        destination_files = os.listdir(file_instance.destination_path)
        assert len(destination_files) == 2
        assert all(file in destination_files for file in file_instance.list_of_files)

        source_files = os.listdir(file_instance.source_path)
        assert len(source_files) == 1

    def test_move_no_permissions(self, file_instance):
        """Test move method when user has no permissions in destination folder."""
        os.chmod(file_instance.destination_path, 0o400)

        with pytest.raises(IOError):
            file_instance.move()
