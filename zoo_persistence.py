import pickle

# Функция для сохранения данных
def save_zoo(zoo, filename='zoo_data.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

# Функция для загрузки данных
def load_zoo(filename='zoo_data.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None
