def find_max_element(array):
    """Знаходимо максимальний елемент масиву"""
    return max(array)

def calculate_sum_before_last_positive(array):
    """Обчислюємо суму елементів масиву перед останнім додатним елементом"""
    last_positive_index = -1

    for i, element in enumerate(array):
        if element > 0:
            last_positive_index = i

    if last_positive_index == -1:
        return 0

    sum_before_last_positive = sum(array[:last_positive_index])

    return sum_before_last_positive

def process_array():
    file_name = input("Введіть назву файлу з масивом: ")  # Запит на введення назви файлу з масивом

    try:
        with open(file_name, "r") as file:  # Відкриття файлу для зчитування
            line = file.readline()
            array = [float(num) for num in line.split()]  # Розбиваємо рядок на числа та перетворюємо їх на числа з плаваючою точкою
    except FileNotFoundError:
        print("Файл не знайдено.")  # Повідомлення про помилку - файл не знайдено
        return
    except ValueError:
        print("Невірний формат даних у файлі.")  # Повідомлення про помилку - невірний формат даних у файлі
        return

    max_element = find_max_element(array)  # Знаходимо максимальний елемент масиву
    sum_before_last_positive = calculate_sum_before_last_positive(array)  # Обчислюємо суму елементів перед останнім додатнім елементом

    print("Максимальний елемент масиву:", max_element)  # Виведення максимального елемента масиву
    print("Сума елементів перед останнім додатним елементом:", sum_before_last_positive)  # Виведення суми елементів перед останнім додатнім елементом

if __name__ == "__main__":
    process_array()  # Виклик функції для обробки масиву