#! python
# pw.py - An insecure password locker program.
import csv, sys, pyperclip

# Exit the program if the sys.argv list has fewer than three values in it.
if len(sys.argv) < 3:
    print('Usage: python pw.py [path of csv file] [account] - copy account password')

    sys.exit()

# First command line argv is the path of csv file.
csvFilePath = sys.argv[1]

# Second command line argv is the account name.
account = sys.argv[2]

with open(csvFilePath) as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate over `reader` to copy the right password if the account name exists.
    for row in reader:
        if row['username'] == account:
            pyperclip.copy(row['password'])

            print('Password for ' + account + ' copied to clipboard.')

            break
    else:
        print('There is no account named ' + account)
