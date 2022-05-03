# https://codechalleng.es/bites/138/
class Animal:

    animals = []
    start = 10000 + 1

    def __init__(self, name):
        self.name = name.capitalize()
        self.animals.append(self.name)

    def __str__(self):
        num = self.start + self.animals.index(self.name)
        return f"{num}. {self.name}"

    @classmethod
    def zoo(cls):
        result = []
        for i, animal in enumerate(cls.animals):
            result.append(f"{cls.start + i}. {animal}")
        return "\n".join(result)
