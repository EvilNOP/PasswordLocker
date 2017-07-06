#! python
# pw.py - An insecure password locker program.
import os, csv, sys, pyperclip

def passwordReader(path, username, dialect=csv.excel, **kwargs):
    with open(path) as csvFile:
        reader = csv.DictReader(csvFile, dialect=dialect, **kwargs)

        # Iterate over `reader` to copy the right password if the account name exists.
        for row in reader:
            if row['username'] == username:
                pyperclip.copy(row['password'])

                print('Password for ' + username + ' copied to clipboard.')

                break
        else:
            print('There is no account named ' + username)

def accountWriter(path, account, dialect=csv.excel, **kwargs):
    with open(path, 'a') as csvFile:
        fieldnames = ['username', 'password', 'category']

        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

        # Writer header if the csv file is newly created
        if os.path.getsize(path) == 0:
            writer.writeheader()

        writer.writerow({'username': account.username, 'password': account.password, 'category': account.category})

if __name__ == '__main__':
    # Exit the program if the sys.argv list has fewer than three values in it.
    if len(sys.argv) < 3:
        print('Usage: python pw.py [path of csv file] [account] - copy account password')

        sys.exit()

    # First command line argv is the path of csv file.
    path = sys.argv[1]

    # Second command line argv is the username.
    username = sys.argv[2]

    passwordReader(path, username)
