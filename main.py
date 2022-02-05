from customer import Customer
from employee import Employee
from checking import CheckingAccount
from savings import SavingsAccount
from insurance import Insurance
from sql_functions import insert_customer


# 1. create customer 2. create employee 3. user login 4. customer login 5. open savings/checking/insurance
# 6. make debit purchase 7. transfer from checking to savings 8. file insurance claim


def bank_ui():
    step1 = input('Enter 1 to create account, 2 to create employee account, 3 for customer login, 4 for employee '
                  'login, or 5 to Exit: ')
    if step1 == '5':
        print('See you later')
        return False
    elif step1 == '1':
        print('Creating account')
        id = insert_customer('test', 'test', 'test@gmail.com', 'test', 'test')
        print(id)
        return False
    elif step1 == '2':
        print('Create employee account')
        return False
    elif step1 == '3':
        print('Customer login')
        return False
    elif step1 == '4':
        print('Employee login')
        return False
    else:
        print('Incorrect input')
        return bank_ui()


def create_account(f_name, l_name, bday, soc, email, pnum, pwrd):
    
    pass


ui = True
while ui:
    ui = bank_ui()
