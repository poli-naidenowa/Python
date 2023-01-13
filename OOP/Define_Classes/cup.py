class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.free_space = size - quantity

    def fill(self, milliliters):
        if milliliters <= self.free_space:
            self.free_space -= milliliters
            self.quantity += milliliters

    def status(self):
        return self.free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())