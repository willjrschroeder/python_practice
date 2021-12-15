#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def list_files(dir):

  files = os.listdir(dir) # creates a list of all the files inside of the passed directory

  for file in files[:]: # loop through a copy of a list of files and remove files from the original list that do not have the right format. Must loop through a copy because you cannot edit a list that is being looped through
    match = re.search('.+__\w+__.+', file)
    if match == None:
      files.remove(file)
  sorted_files = []
  for file in files: # loops through list of files and adds the absolute path of the file to a new list
    sorted_files.append((os.path.abspath(file)))
  return sorted_files

def todirect(todir, currentdir):
  sorted_files = list_files(currentdir) # calls the list_files function and gets the special files into tbe list sorted_files

  if os.path.exists(currentdir + '/' + todir):
    for file in sorted_files:
      shutil.copy(file, currentdir + '/' + todir)
  else:
    os.mkdir(currentdir + '/' + todir) # creates a new dir inside the current dir
    for file in sorted_files: # loop through the sorted_files and copy them to the new dir
      shutil.copy(file, currentdir + '/' + todir)




def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  # checks for presence of flags and runs the
  # corresponding function if flags are present
  # else, runs the default list_files function

  if todir != '':
    todirect(todir, args[0])
  elif tozip != '':
    print('tozip not coded yet')
  else:
    answer = list_files(args[0])
    for file in answer:
        print(file)

if __name__ == "__main__":
  main()
