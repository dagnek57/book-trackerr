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

def add_book(books):
    print("\nДобавление новой книги")
    author = input("Автор: ").strip()
    title = input("Название: ").strip()

    # Проверка на дубликат (пока простая, потом усилим)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Такая книга уже есть в списке!")
            return books

    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите целое число")

    date_str = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Используйте ГГГГ-ММ-ДД")
        return books

    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_str
    }
    books.append(book)
    save_books(books)
    print("Книга добавлена!")
    return books

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
            books = load_books()
            books = add_book(books)  # позже добавим вызов add_book()
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
