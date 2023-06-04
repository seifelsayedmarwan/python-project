import random
import termcolor

termcolor.cprint("Welcome to guess game", "green")
#A game in which the computer chooses a random number from one to nine 
#you have to guess the number 
#you have three attempts
def random_num(length):
    num = ""
    char = "0123456789"
    for _ in range(length):
        num += random.choice(char)
    return num

length = 1 # تحديد طول العدد العشوائي
num = random_num(length)

count = 0
limit = 3
lose = False

while True:
    if count < limit:
        ask = input("Guess the number randomly chosen by the computer from zero to nine:\t")
        count += 1

        if ask == num:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Wrong guess. Try again.")
    else:
        lose = True
        break

if lose:
    print("You reached the maximum number of attempts. The correct number was:", num)