# PasswordLocker

![Platform](https://img.shields.io/badge/platform-python-orange.svg?style=flat)
![Language](https://img.shields.io/badge/python27-compatible-4BC51D.svg?style=flat)

Password locker enables you copy any account password to the clipboard and paste it to the websites Password field.

- [Usage](#usage)

## Usage

```bash
    Usage: python pw.py 
    -r --read                     - copy password to the clipboard for the given username
    -w --write                    - write an account to the csv file
    -d --delete                   - delete an account from the csv file
    -u --update                   - update an account from the csv file
    -f --filepath=filepath        - the [path] to the csv file
    -a --account=your_account     - the [username] of account
    -p --password=your_password   - the [password]
    -c --category=your_category   - the [category] of the account(e.g. google)
    
    Examples: 
    python pw.py -f ~/Desktop/accounts.csv -a my_username
    python pw.py -r -f ~/Desktop/accounts.csv -a my_username
    python pw.py -w -f ~/Desktop/accounts.csv -a my_username -p my_password -c google
    python pw.py -d -f ~/Desktop/accounts.csv -a my_username
    python pw.py -u -f ~/Desktop/accounts.csv -a my_username -p my_password -c google
```
