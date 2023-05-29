import sys
#A simple calculator that performs four mathematical operations, 
# which are addition, subtraction, multiplication and division, 
# according to the user's choice. It works on two numbers only, according to the user's choice.
print("Hello")
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")

calc = input("What arithmetic operation do you want? ")

if calc == "plus":
    result = float(num_1) + float(num_2)
    print(result)
    sys.exit()

if calc == "minus":
    calc_type = input("Do you want to minus the first number from the second or the second from the first? ")
    if calc_type == "first from second":
        result = float(num_2) - float(num_1)
    else:
        result = float(num_1) - float(num_2)
    print(result)
    sys.exit()

if calc == "multiply":
    result = float(num_1) * float(num_2)
    print(result)
    sys.exit()

if calc == "divide":
    calc_type = input("Do you want to divide the first number / the second or the second / the first? ")
    if calc_type == "first \ sconed":
        result = float(num_1) / float(num_2)
    else:
        result = float(num_2) / float(num_1)
    print(result)
    sys.exit()

