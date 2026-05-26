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

def show_all_books(books):
    if not books:
        print("Список книг пуст.")
        return
    print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} - {book['title']} (оценка: {book['rating']}, прочитана: {book['date_read']})")

def average_rating(books):
    if not books:
        print("Нет книг для расчёта средней оценки.")
        return
    avg = sum(book['rating'] for book in books) / len(books)
    print(f"\nСредняя оценка: {avg:.2f}")

def author_stats(books):
    if not books:
        print("Нет книг для статистики.")
        return
    stats = {}
    for book in books:
        author = book['author']
        stats[author] = stats.get(author, 0) + 1
    print("\nСтатистика по авторам:")
    for author, count in stats.items():
        print(f"{author}: {count} книг(а)")

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
            elif choice == "2":
            books = load_books()
            show_all_books(books)
        elif choice == "3":
            elif choice == "3":
            books = load_books()
            average_rating(books)
        elif choice == "4":
            elif choice == "4":
            books = load_books()
            author_stats(books)
        elif choice == "5":
            pass
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
