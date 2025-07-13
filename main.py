import pickle
from address_book import AddressBook, Record


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    # Завантаження адресної книги
    book = load_data()

    # Додаємо контакт (тільки якщо його ще немає)
    if not book.find("Ivan"):
        record = Record("Ivan")
        record.add_phone("0501234567")
        book.add_record(record)
        print("Додано нового контакта: Ivan")
    else:
        print("Контакт Ivan вже існує.")

    # Виводимо всі контакти
    for name, record in book.data.items():
        print(record)

    # Зберігаємо адресну книгу
    save_data(book)
    print("Адресна книга збережена.")


if __name__ == '__main__':
    main()

