class Account:
    """
    Account is compose of three properties: username, password and category
    """
    def __init__(self, username, password, category):
        self.username = username
        self.password = password
        self.category = category
