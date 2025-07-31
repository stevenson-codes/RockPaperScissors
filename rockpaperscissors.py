import random

cpu = random.choice(['rock', 'paper', 'scissors'])
user = input('Rock, Paper or Scissors?\n').lower()
wins, ties, loses = 0, 0, 0

while user != 'exit':
    if cpu == user:
        print('TIE')
        ties += 1
    elif (cpu == 'rock' and user == 'paper' or
        cpu == 'paper' and user == 'scissors' or
        cpu == 'scissors' and user == 'rock'):
        wins += 1
        print('WIN')
    else:
        print('LOSE')
        loses += 1
    print('Wins:', wins, 'Loses:', loses, 'Ties:', ties, '\n')
    user = input('Rock, Paper or Scissors?\n').lower()