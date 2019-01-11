import os, pytest

import helper
from storage.list_file import ListFile

#
# Fixture to make sure test files aren't left on system
# (in the case of assertion errors)
#
@pytest.fixture(autouse=True)
def remove_junk():
    yield
    remove_file("test.txtt")
    remove_file("test.txt")

# 
# See if a junk file is left on the system, and if so, remove it
#
# params:
# file_name:  name of junk file
# 
def remove_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

#
# Various ListFile init function tests
# 
def test_init():
    # empty filename
    assert helper.init(None, "Empty or no file name for list file", 
                       ValueError, ListFile) is True
    assert helper.init("", "Empty or no file name for list file", 
                       ValueError, ListFile) is True

    # file does not have a txt extension
    with open("test.txtt", 'a'):
        assert helper.init("test.txtt", 
                           "File test.txtt is not a .txt file", 
                           ValueError, ListFile) is True
    os.remove("test.txtt")

    # file doesn't exist (and make sure it's not laying around for the sake
    # of the test)
    remove_file("test.txt")
    assert helper.init("test.txt", 
                       "File test.txt doesn't exist or is not a regular file",
                       IOError, ListFile) is True
    
    # success
    with open("test.txt", 'a'):
        pass_test = True
        try:
            list_file = ListFile("test.txt")
        except Exception as err:
            pass_test = False
        assert(pass_test)
    os.remove("test.txt")

#
# get_filename test
# 
def test_get_filename():

    with open("test.txt", 'a'):
        list_file = ListFile("test.txt")
        assert(list_file.get_filename() == "test.txt")
    os.remove("test.txt")

#
# get_lines test
#
def test_get_lines():
    
    # empty file
    filename = os.path.join(os.getcwd(), "test.txt")
    with open(filename, 'a') as f:
        list_file = ListFile(filename)
        assert(len(list_file.get_lines()) == 0)
    os.remove(filename)

    # three lines
    with open(filename, 'w') as f:
        f.write("abc" + os.linesep)
        f.write("def" + os.linesep)
        f.write("ghi")
    list_file = ListFile(filename)
    lines = list_file.get_lines()
    assert(len(lines) == 3)
    assert(lines == [
        ("test.txt", 1, "abc"),
        ("test.txt", 2, "def"),
        ("test.txt", 3, "ghi")
    ])
