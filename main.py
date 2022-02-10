from customer import Customer
from employee import Employee
from checking import CheckingAccount
from savings import SavingsAccount
from utilities import new_cust_prompt, new_emp_prompt, login_prompt, login, check_type, print_balances, act_typ_prmpt,\
    dep_type_prmpt, check_dep_type, act_num_prmpt


def step_1():
    """First step of the UI, 1. create customer 2. create employee 3. employee login 4. customer login

    Prompts the user to chose what they want to do from the above list of options

    Arguments:
    Returns:
        False: if the user selects 5 to exit
        Step_2(): if the user successfully logs in
        Step_1(): if the user successfully creates a customer or employee account
        Step_1(): if the user input is invalid"""

    step1 = input('Enter 1 to create a customer account, 2 to create employee account, 3 for customer login, '
                  '4 for employee login, or 5 to Exit: ')
    if step1 == '5':
        print('See you later')
        return False
    elif step1 == '1':
        vals = new_cust_prompt()
        cust = Customer(vals[0], vals[1], vals[2], vals[3], vals[4])
        cust_id = cust.insert_customer()
        print(f'Successfully created customer with id: {cust_id}')
        return step_1()
    elif step1 == '2':
        vals = new_emp_prompt()
        emp = Employee(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6])
        emp_id = emp.insert_employee()
        print(f'Successfully created employee with id: {emp_id}')
        return step_1()
    elif step1 == '3':
        creds = login_prompt()
        vals = login(creds[0], creds[1], 'Customer')
        if vals:
            cust = Customer(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])
            print(f'Successfully logged in with {cust.email}')
            return step_2(cust)
        else:
            print('Incorrect email & password')
            return step_1()
    elif step1 == '4':
        creds = login_prompt()
        vals = login(creds[0], creds[1], 'Employee')
        if vals:
            emp = Employee(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])
            print(f'Successfully logged in with {emp.email}')
            return step_2(emp)
        else:
            print('Incorrect email & password')
            return step_1()
    else:
        print('Incorrect input')
        return step_1()


# 5. open savings/checking/insurance 6. make debit purchase 8. file insurance claim 9. check balances
def step_2(account):
    step2 = input('Enter 1 to check your balances, 2 to open an account, 3 to make a deposit/withdrawal, '
                  '4 for insurance matters, 5 to return to the first menu, or 6 to exit: ')
    if step2 == '6':
        return False
    elif step2 == '5':
        return step_1()
    elif step2 == '1':
        act_type = act_typ_prmpt()
        act_type = check_type(act_type)
        if act_type == 'SavingsAccount':
            balances = account.check_savings_balance()
            print_balances(balances)
            return step_2(account)
        elif act_type == 'CheckingAccount':
            balances = account.check_checking_balance()
            print_balances(balances)
            return step_2(account)
        elif act_type == 'Exit':
            return step_2(account)
        else:
            print('Incorrect input')
            return step_2(account)
    elif step2 == '2':
        act_type = act_typ_prmpt()
        act_type = check_type(act_type)
        if act_type == 'Exit':
            return step_2(account)
        deposit = input('Enter initial deposit amount: ')
        if act_type == 'SavingsAccount':
            act = SavingsAccount(account.customer_id)
            act.insert_account()
            act.make_deposit(deposit)
            print(f'Successfully created savings account. Current balance: {act.balance}')
            return step_2(account)
        elif act_type == 'CheckingAccount':
            print(f'Creating checking for customer id: {account.customer_id}')
            act = CheckingAccount(account.customer_id)
            act.insert_account()
            act.make_deposit(deposit)
            print(f'Successfully created checking account. Current balance: {act.balance}')
            return step_2(account)
        else:
            print('Incorrect input')
            return step_2(account)
    elif step2 == '3':
        act_type = act_typ_prmpt()
        act_type = check_type(act_type)
        if act_type == 'Exit':
            return step_2(account)
        dep_type = dep_type_prmpt()
        dep_type = check_dep_type(dep_type)
        if dep_type == 'Exit':
            return step_2(account)
        act_num = act_num_prmpt()
        amt = input('Enter amount: ')
        if act_type == 'SavingsAccount' and dep_type == 'Deposit':
            act = SavingsAccount(customer_id=account.customer_id, account_number=act_num)
            print(f'Customer id: {act.customer_id} Account Number: {act.account_number}')
            act.make_deposit(amt)
            print(f'Successfully deposited {amt} into savings account {act.account_number}. Current balance: '
                  f'{act.balance}')
            return step_2(account)
        elif act_type == 'SavingsAccount' and dep_type == 'Withdrawal':
            pass
        elif act_type == 'CheckingAccount' and dep_type == 'Deposit':
            act = SavingsAccount(customer_id=account.customer_id, account_number=act_num)
            act.make_deposit(amt)
            print(f'Successfully deposited {amt} into checking account {act.account_number}. Current balance: '
                  f'{act.balance}')
            return step_2(account)
        elif act_type == 'CheckingAccount' and dep_type == 'Withdrawal':
            pass
        else:
            print('Incorrect input')
            return step_2(account)


def bank_ui():
    step_1()
    return False


ui = True
while ui:
    ui = bank_ui()
