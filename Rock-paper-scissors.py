import random
import termcolor
termcolor.cprint("Welcome", "blue")
char = ["rock", "paper", "scissors"]
          

computer = random.choice(char)

print("Just write the number of your choice where rock is number one, paper is number two, and scissors are number three")
user = str(input("What would you choose, rock, paper, or scissors? "))

if user == computer:
    print("The computer chose", computer)
    termcolor.cprint("Draw", "yellow")
elif user == "rock" and computer == "paper":
    print("The computer chose", computer)
    termcolor.cprint("Lose", "red")
elif user == "paper" and computer == "rock":
    print("The computer chose", computer)
    termcolor.cprint("Win", "green")
elif user == "scissors" and computer == "rock":
    print("The computer chose", computer)
    termcolor.cprint("Lose", "red")
elif user == "rock" and computer == "scissors":
    print("The computer chose", computer)
    termcolor.cprint("Win", "green")
elif user == "scissors" and computer == "paper":
    print("The computer chose", computer)
    termcolor.cprint("Win", "green")
elif user == "paper" and computer == "scissors":
    print("The computer chose", computer)
    termcolor.cprint("Lose", "red")
