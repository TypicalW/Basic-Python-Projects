import sys
import pyperclip

passwords = {}

def add_passwords():
    try:
        num_accounts = input("Enter the number of accounts you want to add or press enter to add none: ")
        if num_accounts == "":
            return
        num_accounts = int(num_accounts)
        for i in range(num_accounts):
            key = input("Enter Username: ")
            value = input("Enter Password: ")
            passwords[key] = value
        print("The Database: ", passwords)
    except ValueError:
        print("Invalid number entered. Please enter an integer.")

if len(sys.argv) < 2:
    print("Usage: python password.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print("There is no account named " + account)

add_passwords()
