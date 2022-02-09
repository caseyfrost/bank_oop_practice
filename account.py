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

    def withdraw(self, amount, table):
        """Reduces the account balance by amount.

        Args:
            amount: int or float to withdraw.

        Returns:
            bool True if completes successfully.

        Raises:
            ValueError if amount is not a positive number."""

        if self.check_num_pos(amount):
            self.balance -= amount
            """ insert a new account into the CheckingAccount table """
            sql = f"""INSERT INTO "{table}"(customer_id)
                    VALUES(%s) RETURNING id;"""
            conn = None
            customer_id = None
            try:
                # read database configuration
                params = config()
                # connect to the PostgreSQL database
                conn = psycopg2.connect(**params)
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (self.customer_id))
                # get the generated id back
                customer_id = cur.fetchone()[0]
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            self.customer_id = customer_id

            return self.customer_id
        else:
            raise ValueError('Withdrawal amount must be a positive number')

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


