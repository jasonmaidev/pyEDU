import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "You win!"
    else:
      return "You lose!"
  elif player == "paper":
    if computer == "scissors":
      return "You lose!"
    else:
      return "You win!"
  elif player == "scissors":
    if computer == "paper":
      return "You win!"
    else:
      return "You lose!"

choices = get_choices()

p_choice = choices["player"]
c_choice = choices["computer"]

print (check_win(p_choice, c_choice))