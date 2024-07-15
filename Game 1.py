import random

while True:
    user_action = input("Enter the choise  rock , paper, scissors")

    possible_action = ['rock', 'paper', 'scissors']

    computer_action = random.choice(possible_action)

    print(f'\n your choise {user_action} , computer choise {computer_action} \n')

    if user_action == computer_action:
        print('it is a tie')
    elif user_action == 'rock':
        if computer_action == 'paper':
            print('Paper covers the Rock and YOU LOSE!!!!')
        else:
            print('Rock smashes the scissors and YOU WIN!!!!')
    elif user_action == 'paper':
        if computer_action == 'scissors':
            print('Scissors will Cut the Paper and YOU LOSE!!!!')
        else:
            print('Paper covers the Rock and YOU WIN!!!!')
    elif user_action == 'scissors':
        if computer_action == 'rock':
            print('Rock smashes the scissors and YOU LOSE!!!!')
        else:
            print('Scissors will Cut the Paper and YOU WIN!!!!')
    else:
        print("enter valid choise")
    a = input('Do you want to play again (y/n)')
    if a == 'n':
        break
