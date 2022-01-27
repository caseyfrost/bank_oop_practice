from user import User


class Customer(User):
    """Represents a bank customer.

    So far there is only one type of customer. Customers have an ID used as key for services and accounts.

    Attributes:
        customer_id: a string of the customer's id
    """
    def __init__(self, customer_id, first_name, last_name, date_of_birth, email):
        super().__init__(first_name, last_name, date_of_birth, email)
        self.customer_id = customer_id
