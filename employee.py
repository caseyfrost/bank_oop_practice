from user import User


class Employee(User):
    """Represents an employee in our banking system application.

    Inherits from the user class, but also gives more information specific to employees. Some attributes aren't used
    at this time, but they are there for future enhancements to the system.

    Attributes:
        employee_id: a string of the employee's identification number.
        department: a string of the department the employee is in.
        salary: property, a positive number, defaults to zero."""

    def __init__(self, employee_id, department, first_name, last_name, date_of_birth, email, salary=0):
        super().__init__(first_name, last_name, date_of_birth, email)
        self.employee_id = employee_id
        self.department = department
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, slry):
        if isinstance(slry, (int, float)):
            if slry > 0:
                self._salary = slry
        else:
            raise ValueError('Salary must be a positive number')

    def give_raise(self, amount):
        """Increases the employee's salary.

        Args:
            amount: a positive int or float

        Returns:
            The boolean True if the raise is successful

        Raises:
            ValueError: the raise amount was not valid"""

        if self.check_num_pos(amount):
            self._salary += amount
            return True
        else:
            raise ValueError("Raise amount must be a positive number")
