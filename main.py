# Rock Paper Scissors Game

import random as rand

choices = ['rock', 'paper', 'scissors']
player = None
computer = rand.choice(choices)

while player not in choices:
    player = input('Rock, Paper, Scissors?').lower().strip()

if player == computer:
    print("It's a tie!")

elif player == 'Rock'.lower():
    if computer == 'Paper'.lower():
        print('You lose!')
    elif computer == 'Scissors'.lower():
        print('You win!')

elif player == 'Paper'.lower():
    if computer == 'Scissors'.lower():
        print('You lose!')
    elif computer == 'Rock'.lower():
        print('You win!')

elif player == 'Scissors'.lower():
    if computer == 'Paper'.lower():
        print('You win!')
    elif computer == 'Rock'.lower():
        print('You lose!')

print('Computer: ' + computer.capitalize() + ' \nPlayer: ' + player.capitalize())




