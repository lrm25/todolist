import os

class ListFile:

    def __init__(self, file_name):
        self._file_name = file_name

    def get_filename(self):
        return self._file_name

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
