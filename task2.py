BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """
    Документация на класс.
    Класс описывает книгу.
    """
    def __init__(self, id_: float, name: str, pages: float):
        """
        Инициализация класса
        :param id_: Индентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги для пользователей
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        """
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library
class Library:
    """
    Документация на класс.
    Класс описывает библиотеку книг.
    """
    def __init__(self, books=None):
        """
        Инициализация экземпляра класса библиотека книг
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        Если книг нет, возвращает 1.
        Если книги есть, возвращает id последней книги увеличенный 1.
        """
        if not self.books:
            return 1
        else:
            last_book = self.books[-1]
            return last_book.id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса
        Если книга существует, возвращает индекс из списка
        Если книги нет, то вызывается ошибка ValueError с сообщением: "Книги с запрашиваемым id не существует"
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
