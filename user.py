class User:
    """Stores all attributes and methods shared by all user types.

    Part of the overall banking system application. There are currently two subclasses: employee, and customer.

    Attributes:
        first_name: a string of the user's first name.
        last_name: a string of the user's last name.
        date_of_birth: a string of the user's dob.
        email: a string of the user's email.
        social: property, a string of the last 4 digits of the user's social. Defaults to empty string.
    """

    def __init__(self, first_name, last_name, date_of_birth, address, email, social=''):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.email = email
        self._social = social

    @property
    def social(self):
        return self._social

    @social.setter
    def social(self, last_4):
        if self.check_num_pos(last_4):
            self._social = last_4
        else:
            self._social = ''
            raise ValueError('Social must be a 4 digit number')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def check_num_pos(num):
        """Checks if arg is a positive number

        Args:
            num: any type of python object

        Returns:
            Bool True if num is positive integer, or False if not"""
        if isinstance(num, (int, float)):
            if num > 0:
                return True

