class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal):
        if len(Vet.animals) >= self.space:
            return "Not enough space"

        Vet.animals.append(animal)
        self.animals.append(animal)
        return f"{animal} registered in the clinic"

    def unregister_animal(self, animal):
        if animal in Vet.animals:
            Vet.animals.remove(animal)
            self.animals.remove(animal)
            return f"{animal} unregistered successfully"

        return f"{animal} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {self.space - len(Vet.animals)} space left in clinic"

