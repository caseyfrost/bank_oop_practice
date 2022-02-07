import psycopg2
from config import config


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


def login_prompt()
    email = input('Enter email: ')
    password = input('Enter password: ')