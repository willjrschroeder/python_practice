#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f = open(filename, 'r') #open file
  contents = f.read() # save read contents to a string

  match = re.search('Popularity in \d\d\d\d', contents) #searches for string containing the year

  year = match.group()[-4:] #isolates the year from the rest of the string

  names = re.findall('(<td>\w+</td>)(<td>\w+</td>)(<td>\w+</td>)', contents) # creates a list of tuples with each tuple containing the rank at index 0, the male name at index 1, and the female name at index 2

  i = 0
  while i < len(names): # while loop that takes in a list of tuples and removes the css around the rankings and names and returns a list of clean lists
    temp = names[i] #creates a temporary variable containing each tuple
    temp = list(temp) #converts the tuple into a mutable list

    j = 0
    while j < len(temp): #for each element in the list temp, loop through and remove the css tags
      temp[j] = temp[j][4:-5] #splice each string at [4:-5]
      j = j + 1

    names[i] = temp #replaces the index value with the cleaned index value
    i = i + 1


  names_dict = {}
  for n in reversed(names): # creates a dictionary with names as key, and their rankings as the value. Goes in reverse order to assign male and female duplicate names to the higher number of prevalance
    names_dict[n[1]] = n[0]
    names_dict[n[2]] = n[0]

  final_data = []
  final_data.append(year)

  for n in sorted(names_dict.keys()): # iterates through each name sorted in order and adds the name and frequency to the list
    final_data.append(n + " " + names_dict[n])

  f.close()

  return final_data


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  if summary: # if summary is true, write results to summary files
    j = 0
    while j < len(args): # While loop to perform operation on each file that is passed
        f = open(args[j] + '.summary', 'x') # create a file called filename.summary
        for n in extract_names(args[j]): # loop that writes each line of list to filename.summary
          f.write(n + '\n')
        j = j + 1

  else: # if summary is false, print results to the terminal
      j = 0
      while j < len(args): # while loop to perform operation on each file passed by the user
        for n in extract_names(args[j]):
          print(n)
        j = j + 1
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file




if __name__ == '__main__':
  main()
