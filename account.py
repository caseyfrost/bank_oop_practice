class Account:
    """Parent for any future type of bank account.

    Stores all the common attributes and methods shared by every type of bank account. Currently there are only two
    subclasses: checking, and savings.

    Attributes:
        balance: a float of the account balance.
        interest_rate: a float of the account's interest rate.
        account_number: a string of the account number.
        customer_id: a string of the customer's id
    """

    def __init__(self, balance, interest_rate, account_number, customer_id):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_number = account_number
        self.customer_id = customer_id

    def make_deposit(self, amount):
        """Makse an 'amount' sized deposit in the account.

        Args:
            amount: int or float """
