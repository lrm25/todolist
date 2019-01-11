#
# module representing a directory on the OS (mac OS X, should be good for
# any unix or linux system, though I haven't tested)
#

import os
from storage.list_file import ListFile

class Folder:

    # 
    # set folder name, and make sure it's a folder
    # 
    # params: folder name
    # 
    # throws:
    # NotADirectoryError:  folder doesn't exist
    #
    def __init__(self, name):

        self._list_files = []

        if name is None or name == "":
            raise ValueError("Empty folder name")
        if not os.path.isdir(name):
            raise NotADirectoryError("Directory %s not found" % (name))
        self._name = name
        
    # 
    # get list of *.txt files in folder specified in global "folder_name"
    # 
    # returns:  nothing
    #
    def gather_lists(self):

        for file_ in os.listdir(self._name):
            full_path = os.path.join(self._name, os.path.basename(file_))
            if (os.path.isfile(full_path)):
                name, extension = os.path.splitext(file_)
                if extension == ".txt":
                    list_file = ListFile(full_path)
                    self._list_files.append(list_file)

    #
    # get full list of lines from all files
    #
    def get_lines(self):

        lines = []

        for list_file in self._list_files:
            lines.extend(list_file.get_lines())
        return lines 
