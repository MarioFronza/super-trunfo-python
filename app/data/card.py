class Card:
    def __init__(self, name: str, age: int, size: float, height: float, weight: float):
        self.name = name
        self.age = age
        self.size = size
        self.height = height
        self.weight = weight

    def __str__(self):
        return "name: {0}, age: {1}, size: {2}, height: {3}, weight: {4}".format(
            self.name, self.age, self.size, self.height, self.weight
        )

