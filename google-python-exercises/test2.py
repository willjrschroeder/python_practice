#add up two variables
#output that sum
#make a variable for #1
#make a variable for #2
#Ask the user for the variables
#add the variables up
#return the answer to the user

import sys

def main():

    x = 0 #create variable x and set it to 0
    y = 0 #create variable y and set it to 0
                                                 ## Debug print print('x type at start' , type(x))
    sum = 0 #create variable sum and set it to 0
    if len(sys.argv) == 3:##check if the length of sys.args is 2 #output the correct usage message if the arguments passed by the user are incorrect
      x = int(sys.argv[1]) #ask the user to input x and assign input to x
      y = int(sys.argv[2]) #ask the user to input y and assign input to x
    else:
      print('argument error. Correct usage: filename x y') ##else print out 'argument error. Correct usage: filename, x, y'
      sys.exit() ##exit the program
                                                ## print('x type before sum' , type(x))
    sum = x + y #add x to y and assign answer to sum
                                                 ## print('x type after sum' , type(x))
    print(sum)  #return the sum to the user

if __name__ == '__main__':
  main()
