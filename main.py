from customer import Customer
from employee import Employee

test = Employee('test_id', 'test_department', 'test_firstname', 'test_lastname', '1/1/1111', 'test.email')
# test2 = Customer()
test.give_raise(1000)

print(test.salary)
test.give_raise(1000)

print(test.salary)
