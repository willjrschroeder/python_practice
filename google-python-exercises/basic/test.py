import sys
import re


def search_file(filename, pat): ## search function that opens a file and returns a list of all occurrences of pat
    f = open(filename, 'r')
    print (f.read())
    contents = f.read()
    found = re.findall(pat, f.read())
    f.close()
    return found


def main(): ## main function that calls the search function or throws an error if right number of arguments aren't passed
    if len(sys.argv) == 3:
        print(search_file(sys.argv[1], sys.argv[2]))
    else:
        print('Error: Correct usage -- test.py filename pat')

if __name__ == '__main__':
    main()
