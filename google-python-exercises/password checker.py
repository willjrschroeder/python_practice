def main():

  keep_going = True
  password = 'poggers'
  tries = 0

  while keep_going == True:
    tries = tries + 1
    print('Try #' + str(tries))
    answer = input('What is the password? ')
    if answer == password:
      print('Congratulations! Access granted')
      keep_going = False

    if tries >= 3:
      print('Incorrect! No more tries remaining')
      keep_going = False

if __name__ == '__main__':
  main()
