#An insecure python password locker
passwords = {}

def add_passwords():
    num_accounts = int(input("enter the number of accounts you wanna add or press nothing to add nothing: "))
    if num_accounts == "":
        break
        for i in range(num_accounts):
            key = input("Enter Username: ")
            value = input("Enter password: ")
            passwords[key] = value

    print("The Database: ", passwords)

import sys
import pyperclip

if len(sys.argv) < 2:
    print("Usage: python password.py [account] - copy account password")
    sys.exit()
account =  sys.argv[1] 

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print("there is no account named " + account)

add_passwords()
