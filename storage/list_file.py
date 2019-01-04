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
        self._file_name = file_name

    # 
    # return:  get this file's full or relative path
    # 
    def get_filename(self):
        return self._file_name

    # 
    # TODO move to main
    # return:  get all lines from this file
    #
    def get_lines(self):
        lines = []
        line_num = 1
        basename = os.path.basename(self._file_name)
        with open(self._file_name) as f:
            for line in f.readlines():
                stripped_line = line.rstrip()
                lines.append((basename, line_num, stripped_line))
                line_num = line_num + 1
        return lines
