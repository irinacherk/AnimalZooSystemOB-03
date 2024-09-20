from animal import Bird, Mammal, Reptile
from zoo import Zoo
from staff import ZooKeeper, Veterinarian
from zoo_persistence import save_zoo, load_zoo

# Функция для вывода звуков животных (демонстрация полиморфизма)
def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()

# Создаем зоопарк или загружаем его состояние
zoo = load_zoo('zoo_data.pkl')
if zoo is None:
    zoo = Zoo()

# Создаем несколько животных
bird = Bird(name="Попугай", age=2)
mammal = Mammal(name="Лев", age=4)
reptile = Reptile(name="Змея", age=3)

# Добавляем животных в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

# Создаем сотрудников
zookeeper = ZooKeeper(name="Иван")
vet = Veterinarian(name="Дмитрий")

# Добавляем сотрудников в зоопарк
zoo.add_staff(zookeeper)
zoo.add_staff(vet)

# Показываем всех животных
print("\nЖивотные в зоопарке:")
zoo.show_animals()

# Показываем всех сотрудников
print("\nСотрудники зоопарка:")
zoo.show_staff()

# Взаимодействие сотрудников с животными
print("\nВзаимодействие сотрудников с животными:")
zookeeper.feed_animal(mammal)  # Иван кормит Льва
vet.heal_animal(bird)          # Дмитрий лечит Попугая

# Демонстрация полиморфизма: выводим звуки животных
print("\nЗвуки животных:")
animals = [bird, mammal, reptile]
animal_sounds(animals)

# Сохраняем текущее состояние зоопарка
save_zoo(zoo, 'zoo_data.pkl')

print("\nСостояние зоопарка сохранено.")
