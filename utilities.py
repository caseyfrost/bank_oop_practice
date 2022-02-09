import psycopg2
from config import config
from checking import CheckingAccount
from savings import SavingsAccount


def new_cust_prompt():
    f_name = input('Enter first name: ')
    l_name = input('Enter last name: ')
    email = input('Enter email address: ')
    password = input('Enter password: ')
    social = input('Enter social: ')
    return (f_name, l_name, email, password, social)


def new_emp_prompt():
    f_name = input('Enter first name: ')
    l_name = input('Enter last name: ')
    email = input('Enter email address: ')
    password = input('Enter password: ')
    department = input('Enter department: ')
    salary = input('Enter salary: ')
    social = input('Enter social: ')
    return (f_name, l_name, email, password, department, salary, social)


def login_prompt():
    email = input('Enter email: ')
    password = input('Enter password: ')
    return (email, password)


def login(email, password, table):
    sql = f"""SELECT first_name, last_name, email, password, social, id
            FROM "{table}"
            WHERE email = (%s) and password = (%s)"""
    conn = None
    customer_vals = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (email, password))
        # get the generated id back
        customer_vals = cur.fetchone()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return customer_vals


def check_type(type):
    if int(type) == 1:
        return 'SavingsAccount', 
    elif int(type) == 2:
        return 'CheckingAccount'
    elif int(type) == 3:
        return 'Exit'
    return False
    