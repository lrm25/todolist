# 
# main module
#

import sys
from storage import folder
from bus import master_list

#
# main function
# 
# params:
# text file (todolist file) directory location
# 
# returns:
# 0 if program runs successfully or no, or too many locations are provided
# 1 if there is a fatal program error
#
def main():
    if (len(sys.argv) is not 2):
        print("Format:  python application.py <list folder>")
        exit(0)
    try:
        # TODO remove direct connection to storage layer
        folder.set(sys.argv[1])
        folder.gather_lists()
        master_list.parse_lines(folder.get_lines())
    except NotADirectoryError as e:
        print(e)
        exit(1)
        

if __name__ == "__main__":
    main()
