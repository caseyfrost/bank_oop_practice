import psycopg2
from config import config
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

    def insert_customer(self):
        """ insert a new customer into the Customer table """
        sql = """INSERT INTO "Customer"(first_name, last_name, email, password, social)
                VALUES(%s, %s, %s, %s, %s) RETURNING id;"""
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
            cur.execute(sql, (self.first_name, self.last_name, self.email, self.password, self.social))
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
