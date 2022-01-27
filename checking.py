from account import Account


class CheckingAccount(Account):
    """Checking account object

    Attributes:
        card_number: string of the user's debit card number.
        overdraft_fee: float of how much will be charged when user overdrafts account."""

    def __init__(self, card_number, overdraft_fee, balance, interest_rate, account_number, customer_id):
        super().__init__(balance, interest_rate, account_number, customer_id)
        self.card_number = card_number
        self.overdraft_fee = overdraft_fee

    def debit_purchase(self, amount):
        """Reduces balance by amount and checks for overdraft

        Args:
            amount: int/float to withdraw from balance

        Returns:
            True if the function finishes without error

        Raises:
            ValueError if amount arg is not a postive int or float
        """
        if self.check_num_pos(amount):
            self.withdraw(amount)
            self.check_overdraft()
            return True
        else:
            raise ValueError("Debit purchase amount must be a positive number")

    def check_overdraft(self):
        """Reduces balance by overdraft fee if balance is < 0

        Args:

        Returns:
            True if an overdraft fee is charged.
            False if the balance is positive"""

        if self.balance < 0:
            self.balance -= self.overdraft_fee
            return True
        else:
            return False
