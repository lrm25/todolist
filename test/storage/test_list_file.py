import os

from storage.list_file import ListFile

# 
# Init test function
# 
# params:
# val:  input value to list file init function
# exception:  expected exception text
# 
# return:  true if exception matches text (and is thrown), false if not
# 
def init(val, exception, exception_type):
    pass_test = False
    try:
        list_file = ListFile(val)
    except exception_type as err:
        pass_test = True if str(err) == exception else False
    return pass_test
    
#
# Various ListFile init function tests
# 
def test_init():
    # empty filename
    assert init(None, "Empty or no file name for list file", ValueError) is True
    assert init("", "Empty or no file name for list file", ValueError) is True

    # file does not have a txt extension
    with open("test.txtt", 'a'):
        assert init("test.txtt", 
                    "File test.txtt is not a .txt file", ValueError) is True
    os.remove("test.txtt")

    # file doesn't exist (and make sure it's not laying around for the sake
    # of the test)
    if os.path.isfile("test.txt"):
        os.remove("test.txt")
    assert init("test.txt", 
                "File test.txt doesn't exist or is not a regular file",
                IOError) is True
    
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
