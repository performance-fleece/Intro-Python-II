class Item:
    def __init__(self, name, weight=1, cost=1):
        self.name = name
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return f"A {self.name} lies in the dirt"

    # def take(self, item):
    #     player.items.append()
