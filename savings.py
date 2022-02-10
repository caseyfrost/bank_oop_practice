from account import Account
import psycopg2
from config import config


class SavingsAccount(Account):
    """Creates a savings account object with limited number of withdrawls

    Attributes:
    """

    def __init__(self, customer_id, balance=0, interest_rate=0, account_number=0):
        super().__init__(balance, interest_rate, account_number, customer_id)
        self.customer_id = customer_id
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_number = account_number

    def insert_account(self):
        """ insert a new account into the CheckingAccount table """
        sql = f"""INSERT INTO "SavingsAccount"(customer_id)
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
            sql = """UPDATE "SavingsAccount"
                  SET balance = balance + %s
                  WHERE customer_id = %s
                  AND account_number = %s;
                  SELECT balance
                  FROM "SavingsAccount"
                  WHERE customer_id = %s
                  AND account_number = %s;"""
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

    def get_balance(self):
        """Set the objects balance property by querying the database.

        Args:
        Returns:
            bool True if method finishes successfully.
        Raises:
            ValueError if amount is not a positive number."""

        sql = """SELECT balance
              FROM "SavingsAccount"
              WHERE customer_id = %s
              AND account_number = %s;"""
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
            cur.execute(sql, (self.customer_id, self.account_number))
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
        print(f'Set balance to: {balance}')
        self.balance = balance

        return self.balance

    def make_withdrawal(self, amount):
        """Makes an 'amount' sized decrease to account balance.

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
            sql = """UPDATE "SavingsAccount"
                  SET balance = balance + %s
                  WHERE customer_id = %s
                  AND account_number = %s;
                  SELECT balance
                  FROM "SavingsAccount"
                  WHERE customer_id = %s
                  AND account_number = %s;"""
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
