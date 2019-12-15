#! python 3
# Utilizing strings methods in an unsecure password program

# Create dictionary PASSWORDS to store passwords to different accounts
PASSWORDS = {'email' : 'superduper', 'blog' : 'dogkibble',
              'luggage' : '12345'}

import sys
import pyperclip
# if the user prompt receives less than two messages display message
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)
