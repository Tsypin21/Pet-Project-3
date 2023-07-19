import matrix_functions
import array_functions

def show_menu():
    print("Меню:")
    print("1. Обробка матриці")  # Опція для обробки матриці
    print("2. Вивід результатів обробки матриці")  # Опція для виводу результатів обробки матриці
    print("3. Обробка масиву")  # Опція для обробки масиву
    print("0. Вихід")  # Опція для виходу з програми

def process_choice(choice):
    if choice == "1":
        matrix_functions.process_matrix()  # Виклик функції для обробки матриці
    elif choice == "2":
        matrix_functions.print_matrix_data()  # Виклик функції для виводу результатів обробки матриці
    elif choice == "3":
        array_functions.process_array()  # Виклик функції для обробки масиву
    elif choice == "0":
        return False
    else:
        print("Невірний вибір. Спробуйте ще раз.")  # Повідомлення про невірний вибір

    return True

if __name__ == "__main__":
    running = True

    while running:
        show_menu()  # Виведення меню
        choice = input("Ваш вибір: ")  # Запит вибору користувача
        running = process_choice(choice)  # Обробка вибору користувача
