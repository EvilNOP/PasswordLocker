#! python
# pw.py - An insecure password locker program.
import os, csv, sys, getopt, account, pyperclip

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
    print '-r --read                     - copy password to the clipboard for the given [username]'
    print '-w --write                    - write an account to the csv file'
    print '-d --delete                   - delete an account from the csv file'
    print '-f --filepath=filepath        - the path to the csv file'
    print '-a --account=your_account     - the username of account'
    print '-p --password=your_password   - the password'
    print '-c --category=your_category   - the category of the account(e.g. google gmail)'
    print
    print
    print 'Examples: '
    print 'python pw.py -f ~/Desktop/accounts.csv -u my_username'
    print 'python pw.py -r -f ~/Desktop/accounts.csv -u my_username'
    print 'python pw.py -w -f ~/Desktop/accounts.csv -u my_username -p my_password -c gmail'
    print 'python pw.py -d -f ~/Desktop/accounts.csv -u my_username'

    sys.exit(0)

def passwordReader(path, username, dialect=csv.excel):
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile, dialect=dialect)

        # Iterate over `reader` to copy the right password if the account name exists.
        for row in reader:
            if row['username'] == username:
                pyperclip.copy(row['password'])

                print('Password for ' + username + ' copied to clipboard.')

                break
        else:
            print('There is no account named ' + username)

def accountWriter(path, account, dialect=csv.excel):
    global fieldnames

    with open(path, 'a') as csvFile:

        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        # Writer header if the csv file is newly created
        if os.path.getsize(path) == 0:
            writer.writeheader()

        writer.writerow({'username': account.username, 'password': account.password, 'category': account.category})

        print 'Account ' + account.username + ' was written to the file successfully'

def deleteAccount(path, username, dialect=csv.excel):
    global fieldnames

    # Read the CSV file in (skipping the row matching the given username)
    with open(path, 'r') as csvFile:
        csvRows = []
        isUsernameFound = False

        reader = csv.DictReader(csvFile, dialect=dialect)

        for row in reader:
            if row['username'] == username:
                isUsernameFound = True

                continue

            csvRows.append(row)

        if not isUsernameFound:
            print('There is no account named ' + username)

            return

    # Write the rows to the same csv file
    with open(path, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames, dialect=dialect)

        writer.writeheader()
        writer.writerows(csvRows)

        print 'Account ' + username + ' removed successfully'

def updateAccount(path, account, dialect=csv.excel):
    global fieldnames

    # Read the CSV file in and update the account which matching the username of the given account
    with open(path, 'r') as csvFile:
        csvRows = []
        isUsernameFound = False

        reader = csv.DictReader(csvFile, dialect=dialect)

        for row in reader:
            if row['username'] == account.username:
                isUsernameFound = True

                # Update the account
                row['username'] = account.username
                row['password'] = account.password
                row['category'] = account.category

            csvRows.append(row)

        if not isUsernameFound:
            print('There is no account named ' + username)

            return

    # Write the rows to the same csv file
    with open(path, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames, dialect=dialect)

        writer.writeheader()
        writer.writerows(csvRows)

        print 'Account ' + account.username + ' updated successfully'

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
            'hrwdf:a:p:c:',
            ['help', 'read', 'write', 'delete', 'filepath=', 'account=', 'password=', 'category=']
        )

        for o, a in opts:
            if o in ('-h', '--help'):
                usage()
            elif o in ('-r', '--read'):
                mode = 'r'
            elif o in ('-w', '--write'):
                mode = 'w'
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

        if mode == 'w':
            acc = account.Account(username, password, category)

            accountWriter(csvFilePath, acc)
        elif mode == 'd':
            deleteAccount(csvFilePath, username)
        else:
            passwordReader(csvFilePath, username)
    except getopt.GetoptError as err:
        print str(err)

        usage()

if __name__ == '__main__':
    main()
