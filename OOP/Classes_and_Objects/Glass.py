class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0
        self.space_left = self.capacity

    def fill(self, ml):
        if self.space_left < ml:
            return f"Cannot add {ml} ml"

        self.space_left -= ml
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        self.space_left = self.capacity
        return "Glass is now empty"

    def info(self):
        return f"{self.space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
