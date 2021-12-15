# In this program, print out a gameboard and ask the user where they want to
# place their move.
# Print out the updated gameboard and ask for the next move
# Do not allow a player to place a move on a square that is already occupied


def print_gameboard(number_of_cols, gameboard):
# Creates the each row of the gameboard
# Uses pipes as walls, each cell shares a pipe
# Checks the cells of the passed gameboard list and prints out the appropriate cell
  

  hats = ' --- --- ---' # establishes the top row of the cell
  bottoms = ' --- --- ---' # establishes the bottom row of the cell
  middles = '' # establishes an empty variable for the middle rows of the cell : It is filled in the if / elif block below

  middlesWhitespace = '   |' # variables that are used to add cells onto the board
  middlesX = ' X |'
  middlesO = ' O |'

  print (hats) # prints out the top slice of the first row

  for j in range(0,3):
# loops through 3 times and prints each row of the gameboard

    if gameboard[j][0] == 0: # if / elif block to decide what the first square of the board should be : Sets the middles variable accordingly
      middles = '|   |'
    elif gameboard[j][0] == 1:
        middles = '| X |'
    elif gameboard[j][0] == 2:
        middles = '| O |'


    for i in range(0, 2): 
  # Loops twice and adds the the correct cells onto the middle variable 
  # depending on the status of the passed gameboard list

      if gameboard[j][i + 1] == 0: # if / elif block to check which middle to add to the board
        middles = middles + middlesWhitespace
      elif gameboard[j][i + 1] == 1:
        middles = middles + middlesX
      elif gameboard[j][i + 1] == 2:
        middles = middles + middlesO

    
    print(middles) # prints out the bottom two structures of the row # Don't need more hats because the rows share hats and bottoms
    print(bottoms)


def player1_move(gameboard):
# Asks for player 1's move and places it into the gameboard list. Returns the passed list plus the next move. 
# Checks that the player did not place a move where one already exists
# # BUG: Does not make sure user is inputting in the right format

  keep_going = True

  while keep_going == True: # loops through until the player enters a valid move
    player1Row = input('Player 1, please enter your move (use the format (column, row)): ') # asks for player 1 input
    player1List = player1Row.split(',') # splits the user input at the comma: '1, 3' > [1, 3]
    player1Col = int(player1List[0].strip()) # cleans the whitespace leftover: [1, 3] > 1
    player1Row = int(player1List[1].strip()) # cleans the whitespace leftover: [1, 3] > 3

    if gameboard[player1Row - 1][player1Col - 1] == 0: # checks to make sure that the specified cell is empty
      gameboard[player1Row - 1][player1Col - 1] = 1 # sets the cell to player 1's move
      keep_going = False
    else:
      print('Invalid Move! There is already a piece in that spot')
    
  return gameboard

def player2_move(gameboard):
# Same code as above, but for player 2  
# Asks for player 2's move and places it in the gameboard list. Returns the passed list plus the next move.  
# Checks that the player did not place a move where one already exists
# # BUG: Does not make sure user is inputting in the right format

  keep_going = True

  while keep_going == True: # loops through until the player enters a valid move
    player2Row = input('Player 2, please enter your move (use the format (column, row)): ') # asks for player 2 input
    player2List = player2Row.split(',') # splits the input at the comma
    player2Col = int(player2List[0].strip())  # cleans the input from whitespace leftover
    player2Row = int(player2List[1].strip())

    if gameboard[player2Row - 1][player2Col - 1] == 0:
      gameboard[player2Row - 1][player2Col - 1] = 2
      keep_going = False
    else:
      print('Invalid Move! There is already a piece in that spot')
    
  return gameboard


def check_gameboard(gameboard):
# Checks to see if the game is over 
# Looks for 3 of the same move in a row horizontally, diagonally, and vertically
# Returns 0 for the game is not over, returns 1 for player 1 wins, returns 2 for player 2 wins, and returns 3 for tie game

  for i in gameboard: # loop through the rows of the board
      if i[0] == i[1] == i[2]: # check if player has won horizontally
          if i[0] != 0: # make sure the row isn't made of zeroes
              return i[0] # returns winning identity

  if gameboard[0][0] == gameboard[1][0] == gameboard[2][0]: # check if player has won vertically
      if gameboard[0][0] != 0:
          return gameboard[0][0] # returns winning identity  
  if gameboard[0][1] == gameboard[1][1] == gameboard[2][1]: # check if player has won vertically
      if gameboard[0][1] != 0:
          return gameboard[0][1] # returns winning identity
  if gameboard[0][2] == gameboard[1][2] == gameboard[2][2]: # check if player has won vertically
      if gameboard[0][2] != 0:
          return gameboard[0][2] # returns winning identity

  if gameboard[0][0] == gameboard[1][1] == gameboard[2][2]: # check if player has won diagonally
      if gameboard[0][0] != 0:
          return gameboard[0][0] # returns winning identity

  if gameboard[0][2] == gameboard[1][1] == gameboard[2][0]: # check if player has won diagonally
      if gameboard[0][2] != 0:
          return gameboard[0][2] # returns winning identity

  for i in gameboard: # if a winner was not found above, check each row for empty spaces. If an empty space is found, return 0 and keep playing
    if 0 in i:
      return 0

  return 3 # if all of the above checks do not return, all the cells are full with no winner, returns tie



def main():
# Intializes the empty gameboard and displays it in the output
# Loops through the game, asking each player for their moves
# Checks if a player has won or if the game is tied and prints the result, terminates the game
  # If neither condition is true, the game continues
    # Want to implement: ASCII art for other win conditions


  gameboard = [[0, 0, 0], # initializes the empty gameboard variable
               [0, 0, 0],
               [0, 0 ,0]]

  print_gameboard(3, gameboard) # prints the empty gameboard out

  playing = True
  while playing == True: # loops through asking for moves from the players until the game is over

    gameboard = player1_move(gameboard) # asks player 1 for their move and updates the gameboard
    print_gameboard(3, gameboard) # prints the current gameboard out
    gamestatus = check_gameboard(gameboard)
    if gamestatus == 3: # checks to see if the game is tied
      print('''
                                                    
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
                     .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
      ''')
      print('Cat\'s game!')
      playing = False
      break
    elif gamestatus == 1: # checks to see if player 1 won
      print('Player 1 wins!')
      playing = False
      break
    
  
    gameboard = player2_move(gameboard) # asks player 2 for their move and updates the gameboard
    print_gameboard(3, gameboard) # prints the current gameboard out
    gamestatus = check_gameboard(gameboard)
    if gamestatus == 3: # checks to see if the game is tied
      print('''
                            _                        
                      \`*-.                    
                       )  _`-.                 
                      .  : `. .                
                      : _   '  \               
                      ; *` _.   `*-._          
                      `-.-'          `-.       
                        ;       `       `.     
                        :.       .        \    
                        . \  .   :   .-'   .   
                        '  `+.;  ;  '      :   
                        :  '  |    ;       ;-. 
                        ; '   : :`-:     _.`* ;
               [bug] .*' /  .*' ; .*`- +'  `*' 
                     `*-*   `*-*  `*-*'        
      ''')
      print('Cat\s game!')
      playing = False
      break
    elif gamestatus == 2: # checks to see if player 2 won
      print('Player 2 wins!')
      playing = False
      break



if __name__ == '__main__':
  main()
