import string

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def hello(self):
        return 'inside person classs'

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self, major):
        self.major = major
        x = super().hello()
        print(x)

    def get_major(self):
        return self.major

person = Person('niklas', 26)
niklas = Student('niklas', 26, 'cs')
print(niklas)
print(niklas.change_major('yo'))

    # alphabet_lowers = string.ascii_lowercase
    # alphabet_uppers = string.ascii_uppercase
    # map_letters = {}
    # i = 0
    #     #Loop over lower and uppercase characters, upper_or_lower becomes a string with
    # for upper_or_lower in (alphabet_lowers, alphabet_uppers):


