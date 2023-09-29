import random
options = ["rock", "paper", "scissors"]
computer = random.choice(options)
user_input = input("choose rock, paper, or scissors")
if user_input != "rock" or "paper" or "scissors":
    print("invalid input. Choose between rock, paper, or scissors")
elif user_input == computer:
    print("Tie")
elif user_input == "rock" and computer == "scissors":
    print("You Win! Rock beats Scissors")
elif user_input == "scissors" and computer == "rock":
    print("Computer Wins! Rock beats Scissors")
elif user_input == "rock" and computer == "paper":
    print("Computer Wins! Paper beats Rock.")
elif user_input == "paper" and computer == "rock":
    print("You Win! Paper beats Rock.")
elif user_input == "paper" and computer == "scissors":
    print("You Win! Scissors beats Paper.")
elif user_input == "scissors" and computer == "paper":
    print("Computer Wins! Scissors beats Paper.")