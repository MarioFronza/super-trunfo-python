class Card:
    def __init__(
        self, name: str, age: float, size: float, height: float, weight: float
    ):
        self.name = name
        self.age = age
        self.size = size
        self.height = height
        self.weight = weight

    def get_attr_by_number(self, number: int) -> float:
        if number == 1:
            return self.age
        if number == 2:
            return self.size
        if number == 3:
            return self.height
        if number == 4:
            return self.weight

    def __str__(self):
        return "name: {0}, age: {1}, size: {2}, height: {3}, weight: {4}".format(
            self.name, self.age, self.size, self.height, self.weight
        )
