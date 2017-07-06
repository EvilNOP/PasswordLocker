#! python
# pw.py - An insecure password locker program.
import csv, sys, pyperclip

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

if __name__ == '__main__':
    # Exit the program if the sys.argv list has fewer than three values in it.
    if len(sys.argv) < 3:
        print('Usage: python pw.py [path of csv file] [account] - copy account password')

        sys.exit()

    # First command line argv is the path of csv file.
    path = sys.argv[1]

    # Second command line argv is the account name.
    account = sys.argv[2]

    passwordReader(path, account)
