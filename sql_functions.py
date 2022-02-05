import psycopg2
from config import config

def insert_customer(first_name, last_name, email, password, social):
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
        cur.execute(sql, (first_name, last_name, email, password, social))
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

    return customer_id