#
# module representing a directory on the OS (mac OS X, should be good for
# any unix or linux system, though I haven't tested)
#

import os
from storage.list_file import ListFile

folder_name = ""

list_files = []

# 
# set folder name, and make sure it's a folder
# 
# params:
# folder name
#
# returns:  nothing
# 
# throws:
# NotADirectoryError:  folder doesn't exist
#
def set(name):
    global folder_name
    if not os.path.isdir(name):
        raise NotADirectoryError("Directory %s not found" % (name))
    folder_name = name
    
# 
# get list of *.txt files in folder specified in global "folder_name"
# 
# params:  none
# 
# returns:  list of *.txt files in folder, if any
#
def gather_lists():
    global folder_name, list_files
    for file_ in os.listdir(folder_name):
        full_path = os.path.join(folder_name, os.path.basename(file_))
        if (os.path.isfile(full_path)):
            name, extension = os.path.splitext(file_)
            if extension == ".txt":
                list_file = ListFile(full_path)
                list_files.append(list_file)

#
# TODO move to main
# get full list of lines from all files
# params:  none
#
# returns:  list of lines from all files
#
def get_lines():

    lines = []

    for list_file in list_files:
        lines.extend(list_file.get_lines())
    return lines 
