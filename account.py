import psycopg2
from config import config


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

    def __init__(self, customer_id, balance=0, interest_rate=0, account_number=0):
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_number = account_number
        self.customer_id = customer_id

    def print_balance(self):
        return f"The current account balance is: {self.balance}"

    @staticmethod
    def check_num_pos(num):
        """Checks if arg is a positive number

        Args:
            num: any type of python object

        Returns:
            Bool True if num is positive integer, or False if not"""
        if isinstance(num, (int, float)):
            if num > 0:
                return True


