import random

cpu = random.choice(['rock', 'paper', 'scissors'])
user = input('Rock, Paper or Scissors?\n').lower()

if cpu == user:
    print('TIE')
elif cpu == 'rock' and user == 'paper':
    print('WIN')
elif cpu == 'paper' and user == 'scissors':
    print('WIN')
elif cpu == 'scissors' and user == 'rock':
    print('WIN')
else:
    print('LOSE')