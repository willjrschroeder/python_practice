

def create_row(number_of_cols):

#
#
  hats = ' ---'
  middles = '|   |'
  bottoms = ' ---'

  for i in range(0, number_of_cols - 1): # loops through number_of_cols times and adds the correct number of hats to a list
    hats = hats + ' ---'
    middles = middles + '   |'
    bottoms = bottoms + ' ---'

  print(hats) # prints each line of the cell
  print(middles)
  print(bottoms)



def create_bottoms(number_of_cols):
    middles = '|   |'
    bottoms = ' ---'

    for i in range(0, number_of_cols - 1): # loops through number_of_cols times and adds the correct number of hats to a list
      middles = middles + '   |'
      bottoms = bottoms + ' ---'

    print(middles)
    print(bottoms)



def main():

  number_of_cols = int(input("Please enter the number of columns you would like in the gameboard: "))

  number_of_rows = int(input('Please enter the number of rows you would like in the gameboard: '))


  create_row(number_of_cols)
  for i in range(0, number_of_rows - 1):
      create_bottoms(number_of_cols)







#########
# wrapper for the main function that will check for value errors on converted inputs. Not tested yet, waiting to implement

''' keep_going = True

while keep_going == True
try:
  ...
except ValueError:
  keep_going = False '''

#########


if __name__ == main():
    main()
