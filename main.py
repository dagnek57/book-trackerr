import json
import os
from datetime import datetime

BOOKS_FILE = "books.json"

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def show_menu():
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            pass  # позже добавим вызов add_book()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
