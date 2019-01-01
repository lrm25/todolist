import sys
from storage import folder
from bus import master_list

def main():
    if (len(sys.argv) is not 2):
        print("Format:  python application.py <list folder>")
        exit(0)
    try:
        folder.set(sys.argv[1])
        folder.gather_lists()
        master_list.parse_lines(folder.get_lines())
    except NotADirectoryError as e:
        print(e)
        exit(1)
        

if __name__ == "__main__":
    main()
