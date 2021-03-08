# https://codechalleng.es/bites/199/
# see __mro__ output in Bite description


class Person:
    def __init__(self):
        self.identity = "person"

    def __str__(self):
        _str = f"I am a {self.identity}"
        return _str


class Mother(Person):
    def __init__(self):
        self.secondary_identity = "awesome mom"
        super().__init__()

    def __str__(self):
        _inherited = super().__str__()
        _str = _inherited + " and " + self.secondary_identity
        return _str


class Father(Person):
    def __init__(self):
        self.secondary_identity = "cool daddy"
        super().__init__()

    def __str__(self):
        _inherited = super().__str__()
        _str = _inherited + " and " + self.secondary_identity
        return _str


class Child(Father, Mother):
    def __init__(self):
        self.new_identity = "the coolest kid"
        super().__init__()

    def __str__(self):
        _str = f"I am {self.new_identity}"
        return _str


# person = Person()
# dad = Father()
# mom = Mother()
# child = Child()

# print(person)
# print(dad)
# print(mom)
# print(child)
# print(Child.__mro__)
