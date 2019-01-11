import os, pytest

from storage.folder import Folder

import helper

#
# Make sure test folder isn't left on system
#
@pytest.fixture(autouse=True)
def remove_junk():
    yield
    if os.path.isdir("test_dir"):
        os.rmdir("test_dir")
    elif os.path.isfile("test_dir"):
        os.remove("test_dir")

#
# Test Folder's init function
#
def test_init():

    # No or empty folder name
    assert helper.init(None, "Empty folder name", ValueError, Folder)
    assert helper.init("", "Empty folder name", ValueError, Folder)

    # Directory doesn't exist
    assert helper.init("test_dir", "Directory test_dir not found",
                       NotADirectoryError, Folder)

    # Not a directory
    with open("test_dir", 'a'):
        assert helper.init("test_dir", "Directory test_dir not found",
                           NotADirectoryError, Folder)
    os.remove("test_dir")

    # Success
    os.mkdir("test_dir")
    pass_test = True
    try:
        folder = Folder("test_dir")
    except Exception as err:
        pass_test = False
    assert(pass_test)
    os.rmdir("test_dir")
