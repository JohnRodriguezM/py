import random

choices_list = ["rock", "paper", "scissors"]


#new function
def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  computer_choice = random.choice(choices_list)

  choices = {
    "player": player_choice,
    "computer": computer_choice,
  }

  return check_win(player_choice, computer_choice)


#new function
def check_win(player_choice, computer_choice):
  outcomes = {
    'rock': {
      'rock': 'tie',
      'paper': 'computer',
      'scissors': 'player'
    },
    'paper': {
      'rock': 'player',
      'paper': 'tie',
      'scissors': 'computer'
    },
    'scissors': {
      'rock': 'computer',
      'paper': 'player',
      'scissors': 'tie'
    }
  }
  return outcomes[player_choice][computer_choice]


# I store the function execution inside a variable for then print the result in the console
response = get_choices()

print('The winner is:', response)