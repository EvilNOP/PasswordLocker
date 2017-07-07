# PasswordLocker

![Platform](https://img.shields.io/badge/platform-python-orange.svg?style=flat)
![Language](https://img.shields.io/badge/python27-compatible-4BC51D.svg?style=flat)

Password locker enables you copy any account password to the clipboard and paste it into the websites Password field.

- [Usage](#usage)

## Usage

```shell
    Usage: python pw.py
    -r --read                     - copy password to the clipboard for the given [username]
    -w --write                    - write an account(composed of [username] [password] [category]) into the csv file
    -f --file_path=your_file_path - the path to the csv file
    -u --username=your_username   - the username
    -p --password=your_password   - the password
    -c --category=your_category   - the category of the account(e.g. google gmail)

    Examples:
    python pw.py -f ~/Desktop/accounts.csv -u my_username
    python pw.py -r -f ~/Desktop/accounts.csv -u my_username
    python pw.py -w -f ~/Desktop/accounts.csv -u my_username -p my_password -c gmail
```
