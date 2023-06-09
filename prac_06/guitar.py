CURRENT_YEAR = 2023


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        age = CURRENT_YEAR - self.year
        self.age = age
        return self.age

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False
