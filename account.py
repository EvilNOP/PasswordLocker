import os, csv, pyperclip

class Account:
    """
    Account is compose of three properties: username, password and category
    """
    def __init__(self, username, password, category):
        self.username = username
        self.password = password
        self.category = category

class PasswordManager:
    """
    PasswordManager managers account with the given csv file along with the "path"
    """
    def __init__(self, filepath, dialect=csv.excel):
        self.filepath = filepath
        self.dialect = dialect
        self.fieldnames = ['username', 'password', 'category']

    def createAccount(self, account):
        with open(self.filepath, 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.fieldnames, dialect=self.dialect)

            # Writer header if the csv file is newly created
            if os.path.getsize(self.filepath) == 0:
                writer.writeheader()

            writer.writerow({'username': account.username, 'password': account.password, 'category': account.category})

            print 'Account ' + account.username + ' created'

    def retrieveAccountPassword(self, username):
        with open(self.filepath) as csvFile:
            reader = csv.DictReader(csvFile, dialect=self.dialect)

            # Iterate over `reader` to copy the right password if the account name exists
            for row in reader:
                if row['username'] == username:
                    pyperclip.copy(row['password'])

                    print('Password for ' + username + ' copied to clipboard.')

                    break
            else:
                print('There is no account named ' + username)

    def updateAccount(self, account):
        # Read the CSV file in and update the account which matching the username of the given account
        with open(self.filepath, 'r') as csvFile:
            csvRows = []
            isUsernameFound = False

            reader = csv.DictReader(csvFile, dialect=self.dialect)

            for row in reader:
                if row['username'] == account.username:
                    isUsernameFound = True

                    # Update the account
                    row['username'] = account.username
                    row['password'] = account.password
                    row['category'] = account.category

                csvRows.append(row)

            if not isUsernameFound:
                print('There is no account named ' + account.username)

                return

        # Write the rows to the same csv file
        with open(self.filepath, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.fieldnames, dialect=self.dialect)

            writer.writeheader()
            writer.writerows(csvRows)

            print 'Account ' + account.username + ' updated'

    def deleteAccount(self, username):
        # Read the CSV file in (skipping the row matching the given username)
        with open(self.filepath, 'r') as csvFile:
            csvRows = []
            isUsernameFound = False

            reader = csv.DictReader(csvFile, dialect=self.dialect)

            for row in reader:
                if row['username'] == username:
                    isUsernameFound = True

                    continue

                csvRows.append(row)

            if not isUsernameFound:
                print('There is no account named ' + username)

                return

        # Write the rows to the same csv file
        with open(self.filepath, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=self.fieldnames, dialect=self.dialect)

            writer.writeheader()
            writer.writerows(csvRows)

            print 'Account ' + username + ' deleted'