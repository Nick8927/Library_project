1. Создаём виртуальное окружение и активируем его.
   python -m venv venv
   venv\Scripts\activate

2. Выстраиваем первоначальный вид проекта.

library_project/
│
├── library/
│ ├── __init__.py
│ ├── book.py
│ ├── user.py
│ ├── library.py
│
├── tests/
│ ├── __init__.py
│ ├── test_library.py
│
├── venv/ # Виртуальное окружение (обычно добавляется в .gitignore)
├── main.py
├── requirements.txt # Зависимости проекта
├── README.md
└── .gitignore

3. Добавляем .gitignore
   Чтобы виртуальное окружение не попадало в репозиторий, создай файл .gitignore и добавь в него строку:
   venv/

4. Установим зависимости
   pip install pytest

5. Закрепи установленную библиотеку в проекте: Чтобы зафиксировать версию зависимости в файле requirements.txt,
   используй:
   pip freeze > requirements.txt

6. Реализуем класс Book:
class Book:
    # Конструктор класса Book, инициализирует свойства книги
    def __init__(self, title, author, year):
        self.title = title  # Название книги
        self.author = author  # Автор книги
        self.year = year  # Год издания
        self.is_available = True  # Флаг доступности книги (по умолчанию книга доступна)

    # Метод для представления объекта в виде строки
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
        # Возвращает строку в формате "Название книги by Автор (Год издания)"

