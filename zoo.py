class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен(а) в зоопарк")

    def add_staff(self, employee):
        self.staff.append(employee)
        print(f"{employee.name} добавлен(а) как сотрудник")

    def show_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        for person in self.staff:
            print(f"Сотрудник: {person.name}, Должность: {person.role}")
