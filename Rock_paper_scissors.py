#rock paper scissors game.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors] #list of game in order
#user enters their choice
user_choice = int(input('What did you choose? Type 0 for Rock, 1 for paper, 2 for Scissors:\n'))
#checking if the user enters an invalid number
if user_choice >= 3 or user_choice<0:
    print('You choose a wrong number. You lose!')
#continue the game
else:
    print(f'You choose\n{game[user_choice]}')

    computer_choice = random.randint(0,3) #random number chose by the computer
    print(f'Computer choose\n{game[computer_choice]}') 
    #rules for the games
    '''
    rock beats scissors, paper beats rock, scissors beats paper
    '''
    #checking for all conditions
    if user_choice ==  computer_choice: 
        print('It\'s a draw')
    elif user_choice == 0 and computer_choice == 1:
        print('You lose.')
    elif user_choice == 0 and computer_choice == 2:
        print('You won')
    elif user_choice == 1 and computer_choice == 0:
        print('You won')
    elif user_choice == 1 and computer_choice == 2:
        print('You lose')
    elif user_choice == 2 and computer_choice == 0:
        print('You lose')
    elif user_choice == 2 and computer_choice == 1:
        print(f'You choose:\n{scissors}\nComputer choose:\n{paper}')
        print('You won')
    else:
        print('Enter either 1 or 2')
