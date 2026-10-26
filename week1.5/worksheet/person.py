# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        if name == "" or birth <= 0:
            raise ValueError("Width and height must be greater than zero")
        if not isinstance(name, str) or not isinstance(birth, int):
            raise TypeError("Width and height must be integers")
        self.name=name
        self.birth=birth
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        result=""
        spart=self.name.split()
        for i in spart:
            result += i[0]
        return result
    def is_birthday(self):
        return self.birth == date.today().month

print(Person("Jan Malty",2).initials())