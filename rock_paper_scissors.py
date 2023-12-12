import random

comp_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("What is your choice- rock, paper, scissors?\n")

if user_choice == comp_choice:
    print("TIE")
elif user_choice == "rock" and comp_choice == "scissors":
    print("WIN!!! Computer Choice is "+comp_choice)
elif user_choice == "paper" and comp_choice == "rock":
    print("WIN!!! Computer Choice is "+comp_choice)
elif user_choice == "scissors" and comp_choice == "paper":
    print("WIN!!! Computer Choice is "+comp_choice)
else:
    print("You Lose!!! Computer Choice is "+comp_choice)
