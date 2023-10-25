def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    print("Please enter an option:")
    choice = input()
    return choice

def encode():
    newPassword = ""
    print("Please enter your password to encode")
    password = input()
    for x in password:
        x = int(x) + 3
        newPassword = newPassword + str(x)
    return newPassword

def decode(password):
    pw = ""
    for x in password:
        x = int(x) - 3
        pw += str(x)
    return pw

def main():
    password = ""
    while True:
        choice = menu()

        if choice == '1':
            password = encode()
            print('Your password has been encoded and stored!\n')
        elif choice == '2':
            print(f'The encoded password is {password}, and the original password is {decode(password)}.\n')
        elif choice == '3':
            quit()

if __name__ == '__main__':
    main()
