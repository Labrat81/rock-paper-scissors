import random


def get_choices():  # function declaration - must include :
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices  # must be indented the same

#choices = get_choices() - these were just for the sake of checking what was printed
#print(choices)

def check_win(player, computer):
    print(f'You chose {player}, computer chose {computer}')
    if player == computer:                                  #if statements need a : after the condition
        return "It's a tie"                                 #if returns need to have a further indent 
    elif player == 'rock' and computer == 'scissors':       #elif is else...if for python
        return 'Rock smashes scissors! You win!'
    elif player == 'rock' and computer == 'paper':          #conditional and is the word, not &&
        return 'Paper covers rock! You lose!'
    
#switch to the nested version to continue - I want to keep this to remind me how the basic elif chain works <--------- 

check_win('rock', 'paper')