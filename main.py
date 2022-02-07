from customer import Customer
from employee import Employee
from checking import CheckingAccount
from savings import SavingsAccount
from insurance import Insurance
from utilities import new_cust_prompt, new_emp_prompt


# 1. create customer 2. create employee 3. employeelogin 4. customer login 5. open savings/checking/insurance
# 6. make debit purchase 8. file insurance claim 9. check balances


def bank_ui():
    step1 = input('Enter 1 to create a customer account, 2 to create employee account, 3 for customer login,'
                  '4 for employee login, or 5 to Exit: ')
    if step1 == '5':
        print('See you later')
        return False
    elif step1 == '1':
        print('Creating customer account')
        vals = new_cust_prompt()
        cust = Customer(vals[0], vals[1], vals[2], vals[3], vals[4])
        cust_id = cust.insert_customer()
        print(f'Successfully created customer with id: {cust_id}')
        return bank_ui()
    elif step1 == '2':
        print('Creating employee account')
        vals = new_emp_prompt()
        emp = Employee(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])
        emp_id = emp.insert_employee()
        print(f'Successfully created customer with id: {emp_id}')
        return bank_ui()
    elif step1 == '3':
        print('Customer login')
        return False
    elif step1 == '4':
        print('Employee login')
        return False
    else:
        print('Incorrect input')
        return bank_ui()


ui = True
while ui:
    ui = bank_ui()
