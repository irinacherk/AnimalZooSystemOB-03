class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, role="Смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, role="Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")
