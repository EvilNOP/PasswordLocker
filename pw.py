#! python
# pw.py - An insecure password locker program.
import sys, pyperclip

# Passwords example .
PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog' : 'VmALvQyKAxiVH5G8v01if1MLZF3sdt'
}

# Exit the program if the sys.argv list has fewer than two values in it(means miss the account).
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')

    sys.exit()

# First command line argv is the account name.
account = sys.argv[1]

# Copy the right password if the account name exists.
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])

    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)