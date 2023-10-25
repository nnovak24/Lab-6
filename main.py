password = 0
choice = 0
encoded = 0

def menu(choice):
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    print("Please enter an option:")
    choice = input()
    return choice

def encode(password):
    newPassword = ""
    print("Please enter your password to encode")
    password = input()
    for x in password:
        x = int(x) + 3
        newPassword = newPassword + str(x)
    return newPassword

choice = menu(choice)
encoded = encode(password)