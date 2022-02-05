from user import User


class Customer(User):
    """Represents a bank customer.

    So far there is only one type of customer. Customers have an ID used as key for services and accounts.

    Attributes:
        customer_id: a string of the customer's id
    """
    def __init__(self, first_name, last_name, email, password, social, customer_id=''):
        super().__init__(first_name, last_name, email, password, social)
        self.customer_id = customer_id
