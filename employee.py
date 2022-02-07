import psycopg2
from config import config
from user import User


class Employee(User):
    """Represents an employee in our banking system application.

    Inherits from the user class, but also gives more information specific to employees. Some attributes aren't used
    at this time, but they are there for future enhancements to the system.

    Attributes:
        employee_id: a string of the employee's identification number.
        department: a string of the department the employee is in.
        salary: property, a positive number, defaults to zero."""

    def __init__(self, first_name, last_name, email, password, department, salary=0, social='', employee_id=''):
        super().__init__(first_name, last_name, password, email, social)
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

    def insert_employee(self):
        """ insert a new employee into the Employee table """
        sql = """INSERT INTO "Employee"(first_name, last_name, email, password, department, salary, social)
                VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id;"""
        conn = None
        employee_id = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (self.first_name, self.last_name, self.email, self.password, self.department,
                        self.salary, self.social))
            # get the generated id back
            employee_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        self.employee_id = employee_id

        return self.employee_id
