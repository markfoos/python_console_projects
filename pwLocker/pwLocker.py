#! python3
# pw.py -- AN insecure pawword locker program by Mark Foos
# inspired by Autonmate the Boring Stuff with Python by AL Sweitgart

PASSWORDS = {'email': 'pw_for_eamil', 'facebook':'pw_for_fb', 'google' : 'pw_for_google'}

import sys, pyperclip
if len(sys.argv) > 2:
    print("Usage: python-pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] #first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There is no account named " + account)
