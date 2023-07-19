import pickle

def calculate_row_sum(row):
    """Обчислюємо суму елементів у рядку"""
    return sum(row)

def find_max_element(matrix):
    """Знаходимо максимальний елемент матриці і повертаємо його координати"""
    max_element = matrix[0][0]
    max_row = 0
    max_column = 0

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element > max_element:
                max_element = element
                max_row = i
                max_column = j

    return max_row + 1, max_column + 1  # Додаємо 1 до номерів рядка і стовпчика

def process_matrix():
    file_name = input("Введіть назву файлу з матрицею: ")  # Запит на введення назви файлу з матрицею

    try:
        with open(file_name, "r") as file:  # Відкриття файлу для зчитування
            lines = file.readlines()

            matrix = []
            for line in lines:
                row = [int(num) for num in line.split()]  # Розбиваємо рядок на числа та перетворюємо їх на цілі числа
                matrix.append(row)
    except FileNotFoundError:
        print("Файл не знайдено.")  # Повідомлення про помилку - файл не знайдено
        return
    except ValueError:
        print("Невірний формат даних у файлі.")  # Повідомлення про помилку - невірний формат даних у файлі
        return

    row_sums = []
    negative_row_sums = []

    for row in matrix:
        row_sum = calculate_row_sum(row)  # Обчислюємо суму елементів у рядку
        row_sums.append(row_sum)

        if any(element < 0 for element in row):  # Перевіряємо, чи є в рядку від'ємні елементи
            negative_row_sums.append(row_sum)

    max_row, max_column = find_max_element(matrix)  # Знаходимо координати максимального елемента

    with open("matrix_data.bin", "wb") as file:  # Відкриття файлу для запису
        data = {
            "row_sums": row_sums,
            "negative_row_sums": negative_row_sums,
            "max_row": max_row,
            "max_column": max_column
        }
        pickle.dump(data, file)  # Запис даних у файл у бінарному форматі

    print("Матриця оброблена і дані записані до файлу.")  # Повідомлення про успішну обробку матриці

def print_matrix_data():
    with open("matrix_data.bin", "rb") as file:  # Відкриття файлу для зчитування
        data = pickle.load(file)  # Завантаження даних з файлу

    print("Суми елементів рядків:", data["row_sums"])  # Виведення сум елементів рядків
    print("Суми елементів рядків з від'ємними елементами:", data["negative_row_sums"])  # Виведення сум елементів рядків з від'ємними елементами
    print("Номер рядка максимального елемента:", data["max_row"])  # Виведення номера рядка максимального елемента
    print("Номер стовпчика максимального елемента:", data["max_column"])  # Виведення номера стовпчика максимального елемента

if __name__ == "__main__":
    process_matrix()  # Виклик функції для обробки матриці
    print_matrix_data()  # Виклик функції для виведення даних
