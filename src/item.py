class Item:
    def __init__(self, name, description="A non-descript item", weight, cost):
        self.name = name
        self.description = description
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"{self.name} weights {self.weight} and costs {self.cost}"
