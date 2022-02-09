from account import Account
import psycopg2
from config import config


class CheckingAccount(Account):
    """Checking account object

    Attributes:
        card_number: string of the user's debit card number.
        overdraft_fee: float of how much will be charged when user overdrafts account."""

    def __init__(self, customer_id, balance=0, interest_rate=0, account_number=0, card_number=0, overdraft_fee=0):
        super().__init__(balance, interest_rate, customer_id, account_number)
        self.card_number = card_number
        self.overdraft_fee = overdraft_fee
        self.customer_id = customer_id

    def debit_purchase(self, amount):
        """Reduces balance by amount and checks for overdraft

        Args:
            amount: int/float to withdraw from balance

        Returns:
            True if the function finishes without error

        Raises:
            ValueError if amount arg is not a positive int or float
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
            False if the balance is positive
        """

        if self.balance < 0:
            self.balance -= self.overdraft_fee
            return True
        else:
            return False

    def insert_account(self):
        """ insert a new account into the CheckingAccount table """
        sql = f"""INSERT INTO "CheckingAccount"(customer_id)
                VALUES(%s) RETURNING id;"""
        conn = None
        account_number = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, str(self.customer_id))
            # get the generated id back
            account_number = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        self.account_number = account_number

        return self.account_number

    def make_deposit(self, amount):
        """Makes an 'amount' sized increase to account balance.

        Args:
            amount: int or float of the deposit amount.
        Returns:
            bool True if method finishes successfully.
        Raises:
            ValueError if amount is not a positive number."""

        amount = int(amount)
        if self.check_num_pos(amount):
            self.balance += amount
            """ Update the balance for the customer id in the CheckingAccount table """
            sql = """UPDATE "CheckingAccount"
                  SET balance = balance + %s
                  WHERE customer_id = %s
                  AND account_number = %s;
                  SELECT balance
                  FROM "CheckingAccount"
                  WHERE customer_id = %s
                  AND id = %s;"""
            conn = None
            balance = None
            try:
                # read database configuration
                params = config()
                # connect to the PostgreSQL database
                conn = psycopg2.connect(**params)
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (str(amount), self.customer_id, self.account_number, self.customer_id,
                                  self.account_number))
                # get the generated id back
                balance = cur.fetchone()[0]
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            self.balance = balance

            return self.balance
        else:
            return False
