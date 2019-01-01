import os

from storage.list_file import ListFile

folder_name = ""

list_files = []

def set(name):
    global folder_name
    if not os.path.isdir(name):
        raise NotADirectoryError("Directory %s not found" % (name))
    folder_name = name
    
def gather_lists():
    global folder_name, list_files
    for file_ in os.listdir(folder_name):
        full_path = os.path.join(folder_name, os.path.basename(file_))
        if (os.path.isfile(full_path)):
            name, extension = os.path.splitext(file_)
            if extension == ".txt":
                list_file = ListFile(full_path)
                list_files.append(list_file)

def get_lines():

    lines = []

    for list_file in list_files:
        lines.extend(list_file.get_lines())
    return lines 
