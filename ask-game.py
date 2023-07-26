import sys
#A simple questions game consisting of three stages, each stage consists of ten questions, 
# and for each question you answer correctly, you will be given a point, 
# and if you do not answer, it will tell you the correct answer, 
# and in the end it will tell you how many questions you answered correctly and how many points you collected
print("                                             Welcome to questions Game")
print("                                                     (login page)")

first = input("What is your first name? ")            
second = input("What is your second name? ")
age = int(input("What is your age? "))
if age > 10:
 print("You are welcome")

else:
     print("You are a child and this program is for those who are only ten years old")
     sys.exit()

print("                                                      (play page)")
score = 0
ask = ""
#1
answer = "cairo"
count = 0
limit = 3
lose = False
while answer != ask and not lose:
    if count < limit:
        ask = input("What is the capital  of Egypt? ").lower()
        count += 1
    else:
        lose = True

if lose:
    print("Right answer is: cairo")
    
else:
    print("Right answer")
    score += 1

#2
answer = "paris"
count = 0
limit = 3
lose = False
while answer != ask and not lose:
    if count < limit:
        ask = input("What is the capital of France? ").lower()
        count += 1
    else:
        lose = True

if lose:
    print("Right answer is: paris")
    
else:
    print("Right answer")
    score += 1

#3
answer = "mount everest"
count = 0
limit = 3
lose = False
while answer != ask and not lose:
    if count < limit:
        ask = input("What is the tallest mountain in the world? ").lower()
        count += 1
    else:
        lose = True

if lose:
    print("Right answer is: mount everest")

else:
    print('Right answer')
    score += 1

#4
answer = "mars"
count = 0
limit = 3
lose = False
while answer != ask and not lose:
    if count < limit:
        ask = input("Which planet is known as the \"Red Planet\"? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: mars")
    
else:
    print("Right answer")
    score += 1

#5
answer = "pacific ocean"
count = 0
limit = 3
lose = False
while answer != ask and not lose:
    if count < limit:
        ask = input("What is the largest ocean on Earth? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: pacific ocean")
    
else:
    print("Right answer")
    score += 1

#6
answer = "china"
count = 0
limit = 3
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which country is famous for the Great Wall? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: china")
    
else:
    print("Right answer")
    score += 1

#7
answer = "asia"
count = 0
limit = 3
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the largest continent by land area? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("ٌRight answer is: asia")
    
else:
    print("Right answer")
    score += 1

#8
answer = "new york"
count = 0
limit = 3
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which city is known as the \"Big Apple\"? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: new york")
    
else:
    print("Right answer")
    score += 1

#9
answer = "canberra"
count = 0
limit = 3
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the capital city of Australia? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: canberra")
    
else:
    print("Right answer")
    score += 1

#10
answer = "jupiter"
count = 0
limit = 3
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the largest planet in our solar system? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: jupiter")
    
else:
    print("Right answer")
    score += 1

#second level
print("        Welcome to the second level of the game questions")
#11
answer = "yen"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count <limit:
        ask = input("What is the currency of Japan? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: japanese yen")
    
else:
    print("Right answer")
    score += 1

#12
answer = "russia"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the largest country in the world by land area? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: russia")
    
else:
    print("Right answer")
    score += 1

#13
answer = "euro"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the currency of Germany? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: euro")
    
else:
    print("Right answer")
    score += 1

#14
answer = "brasilia"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the capital city of Brazil? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: brasilia")
    
else:
    print("Right answer")
    score += 1

#15
answer = "australia"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which country is home to the Great Barrier Reef? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: australia")
    
else:
    print("Right answer")
    score += 1

#16
answer = "ottawa"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the capital city of Canada? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: ottawa")
    
else:
    print("Right answer")
    score += 1

#17
answer = "brazil"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which country is known for producing the most coffee in the world? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: brazil")
    
else:
    print("Right answer")
    score += 1

#18

answer = "GBP"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the currency of the United Kingdom? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: GBP")
    
else:
    print("Right answer")
    score += 1

#19
answer = "pretoria"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the executive capital of South Africa? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: pretoria")
else:
    print("Right answer")
    score += 1

#20
answer = "madrid"
count = 0
limit = 2
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the capital city of Spain? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: madrid")
    
else:
    print("Right answer")
    score += 1

#third level
print("        Welcome to the third level of the questions game")



#21
answer = "AUD"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the currency of Australia? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: AUD")
    
else:
    print("Right answer")
    score += 1

#22
answer = "egypt"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which country is known for its pyramids? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: egypt")
    
else:
    print("Right answer")
    score += 1


#23
answer = "CAD"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the currency of Canada? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: CAD")
    
else:
    print("Right answer")
    score += 1

#24
answer = "german"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the official language of Germany? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: german")
    
else:
    print("Right answer")
    score += 1

#25
answer = "italy"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("Which country is known for its historical landmarks such as the Colosseum and the Vatican? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: italy")
    
else:
    print("Right answer")
    score += 1

#26
answer = "spanish"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the official language of Spain? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: spanish")
    
else:
    print("Right answer")
    score += 1

#27
answer = "titan" 
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the name of the largest moon of Saturn? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: titan")
else:
    print("Right answer")
    score += 1

#28
answer = "au"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the chemical symbol for the element gold? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: au")
    
else:
    print("Right answer")
    score += 1

#29
answer = "seoul"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the capital city of South Korea? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: seoul")
    
else:
    print("Right answer")
    score += 1

#30
answer = "ag"
count = 0
limit = 1
lose = False
while ask != answer and not lose:
    if count < limit:
        ask = input("What is the chemical symbol for the element silver? ").lower()
        count += 1
    else:
        lose = True
if lose:
    print("Right answer is: ag")
    
else:
    print("Right answer")
    score += 1

print("""You have finished the game and answered all the questions correctly, and this indicates that you are educated and know a lot of information""")
print("You answer", score ,"question from 30 questions")
print("Your score is:", score)
if score > 22:
    print("Your culture is excellent. Work on developing it")
else:
    print("You did not get the points required to succeed in the game")
print(input("If there is any problem, tell us or press Enter to exit: "))