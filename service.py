class Service:
    """Parent class for all bank services

    Attributes:
        account_number: str of account number
        customer_id: str of account owner's customer id
    """

    def __init__(self, account_number, customer_id):
        self.account_number = account_number
        self.customer_id = customer_id

    def bill_customer(self, amount):
        """After db is set up a query will be run to reduce the customer's balance by the amount"""

