# Rock Paper Scissors Game

import random as rand

while True:
    choices = ['rock', 'paper', 'scissors']
    player = None
    computer = rand.choice(choices)

    while player not in choices:
        player = input('Rock, Paper, Scissors?').lower().strip()

    if player == computer:
        print("It's a tie!")

    elif player == 'rock':
        if computer == 'paper':
            print('You lose!')
        elif computer == 'scissors':
            print('You win!')

    elif player == 'paper':
        if computer == 'scissors':
            print('You lose!')
        elif computer == 'rock':
            print('You win!')

    elif player == 'scissors':
        if computer == 'paper':
            print('You win!')
        elif computer == 'rock':
            print('You lose!')

    print('Computer: ' + computer.capitalize() + ' \nPlayer: ' + player.capitalize())

    play_again = input("Play again? (Yes/No): ").lower()

    if play_again != 'yes':
        break

print('Bye!')




