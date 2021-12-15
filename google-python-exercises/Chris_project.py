#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Beep Boop

Define the beep_boop() function below and change main()
to call it.

The beep_boop funciton takes no arguments, returns nothing, and must do the following:

- Prints all integers from 1 to 100, each on its own line,
- But there are the following expections
- If the number is divisible by 3, print "beep" instead
- If the number is divisible by 5, print "boop" instead
- If the number is divisible by both 3 and 5, print "beep_boop" instead


"""

def beep_boop():
  """
  - Prints all integers from 1 to 100, each on its own line,
  - But there are the following expections
  - If the number is divisible by 3, print "beep" instead
  - If the number is divisible by 5, print "boop" instead
  - If the number is divisible by both 3 and 5, print "beep_boop" instead
  """
  i = 1
  while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
      print('beep_boop')
    elif i % 3 == 0:
      print('beep')
    elif i % 5 == 0:
      print('boop')
    else:
      print (i)
    i = i + 1





def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  beep_boop()



if __name__ == '__main__':
  main()
