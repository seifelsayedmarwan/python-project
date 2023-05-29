import random

def create_password(length):
    password = ""
    char = "01234567890123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$&@#$&abcdefghijklmnopqrstuvwxyz@#$&"
    for _ in range(length):
        password += random.choice(char)
    return password

while True:
    pass_length = int(input("Enter password length: "))
    print(create_password(pass_length))
    go_back = input("Type back to back first or press enter to exit: ")
    if go_back.lower() == "back":
     continue
    else:
        break 


    