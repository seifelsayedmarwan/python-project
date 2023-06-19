import sys
"""
It is a game that gives the user the advantage of choosing the type of questions,
 and it has several types, and each type has several levels, 
 perhaps one or more
"""
print("Welcome")
name = print("Hello,", input("What is your name? "))
print("Welcome to questions Game")

print("""There are three types of questions,which are 
      1- scientific questions,
      2- cultural questions,
      3- sports questions, """)
try:
  choose_number = int(input("Chose a number from one to three to specify the type of questions you will answer:"))
except ValueError:
    print("You did not choose a number")

if choose_number == "1":
    print("You chose scientific qustions")
    print("This part of the questions consists of one level")
    start = input("To get started, type start").lower()
    if start == "start":
       


if choose_number == "2":
    print("You chose cultural questions")

if choose_number == "3":
    print("You chose sports question")

else:
  print("You must choose from one to three only")

