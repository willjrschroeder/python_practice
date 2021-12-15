# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac
# Toe game board, tell me whether anyone has won, and tell me which player won,
# if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a
# diagonal. Don’t worry about the case where TWO people have won - assume that
# in every board there will only be one winner.



game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1]]



def check_gameboard(game):
    for i in game: # loop through the rows of the board
        if i[0] == i[1] == i[2]: # check if player has won horizontally
            if i[0] != 0: # make sure the row isn't made of zeroes
                print('Player', i[0], 'wins!')

    if game[0][0] == game[1][0] == game[2][0]: # check if player has won vertically
        if game[0][0] != 0:
            print('Player', game[0][0], 'wins!')
    if game[0][1] == game[1][1] == game[2][1]: # check if player has won vertically
        if game[0][1] != 0:
            print('Player', game[0][1], 'wins!')
    if game[0][2] == game[1][2] == game[2][2]: # check if player has won vertically
        if game[0][2] != 0:
            print('Player', game[0][2], 'wins!')

    if game[0][0] == game[1][1] == game[2][2]: # check if player has won diagonally
        if game[0][0] != 0:
            print('Player', game[0][0], 'wins!')

    if game[0][2] == game[1][1] == game[2][0]: # check if player has won diagonally
        if game[0][2] != 0:
            print('Player', game[0][2], 'wins!')

check_gameboard(game)
