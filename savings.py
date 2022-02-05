from account import Account


class SavingsAccount(Account):
    """Creates a savings account object with limited number of withdrawls

    Attributes:
    """

    def __init__(self, balance, interest_rate, account_number, customer_id):
        super().__init__(balance, interest_rate, account_number, customer_id)
