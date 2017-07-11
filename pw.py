#! python
# pw.py - An insecure password locker program.
import sys, getopt, account

# Define global variables
# `mode` indicates either read password or write an account to csv file
mode        = None
csvFilePath = None
username    = None
password    = None
category    = None
fieldnames  = ['username', 'password', 'category']

def usage():
    print 'An insecure password locker program'
    print
    print 'Usage: python pw.py '
    print '-r --read                     - copy password to the clipboard for the given username'
    print '-w --write                    - write an account to the csv file'
    print '-d --delete                   - delete an account from the csv file'
    print '-u --update                   - update an account to the csv file'
    print '-f --filepath=filepath        - the [path] to the csv file'
    print '-a --account=your_account     - the [username] of account'
    print '-p --password=your_password   - the [password]'
    print '-c --category=your_category   - the [category] of the account(e.g. google)'
    print
    print
    print 'Examples: '
    print 'python pw.py -f ~/Desktop/accounts.csv -a my_username'
    print 'python pw.py -r -f ~/Desktop/accounts.csv -a my_username'
    print 'python pw.py -w -f ~/Desktop/accounts.csv -a my_username -p my_password -c google'
    print 'python pw.py -d -f ~/Desktop/accounts.csv -a my_username'
    print 'python pw.py -u -f ~/Desktop/accounts.csv -a my_username -p my_password -c google'

    sys.exit(0)

def main():
    global mode
    global csvFilePath
    global username
    global password
    global category

    # Display the usage if the sys.argv list has fewer than three values in it.
    if not len(sys.argv[1:]):
        usage()

    # Read the commandline options
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'hrwudf:a:p:c:',
            ['help', 'read', 'write', 'update', 'delete', 'filepath=', 'account=', 'password=', 'category=']
        )

        for o, a in opts:
            if o in ('-h', '--help'):
                usage()
            elif o in ('-r', '--read'):
                mode = 'r'
            elif o in ('-w', '--write'):
                mode = 'w'
            elif o in ('-u', '--update'):
                mode = 'u'
            elif o in ('-d', '--delete'):
                mode = 'd'
            elif o in ('-f', '--filepath'):
                csvFilePath = a
            elif o in ('-a', '--account'):
                username = a
            elif o in ('-p', '--password'):
                password = a
            elif o in ('-c', '--category'):
                category = a
            else:
                assert False, "Unhandled Option"

        manager = account.PasswordManager(csvFilePath)

        if mode in 'wu':
            acc = account.Account(username, password, category)

            if mode == 'w':
                manager.createAccount(acc)
            else:
                manager.updateAccount(acc)
        elif mode == 'd':
            manager.deleteAccount(username)
        else:
            manager.retrieveAccountPassword(username)
    except getopt.GetoptError as err:
        print str(err)

        usage()

if __name__ == '__main__':
    main()
