import os

#
# TODO get rid of this class
# class representing a *.txt list file
#
class ListFile:

    #
    # __init__
    #
    # params:
    # file_name:  full or relative path of list file
    #
    def __init__(self, file_name):

        if file_name is None or file_name == "":
            raise ValueError("Empty or no file name for list file")

        name, extension = os.path.splitext(file_name)
        if extension != ".txt":
            raise ValueError("File %s is not a .txt file" % file_name)

        if not os.path.isfile(file_name):
            raise IOError("File %s doesn't exist or is not a regular file" % 
                          file_name)

        self._file_name = file_name

    # 
    # return:  get this file's full or relative path
    # 
    def get_filename(self):
        return self._file_name

    # 
    # TODO move up to master_list
    # return:  get all lines from this file
    #
    def get_lines(self):
        lines = []
        basename = os.path.basename(self._file_name)
        with open(self._file_name) as f:
            for line_num, line in enumerate(f.readlines(), 1):
                stripped_line = line.rstrip()
                lines.append((basename, line_num, stripped_line))
        return lines
