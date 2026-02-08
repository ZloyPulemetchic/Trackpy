# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Any, Optional


class Book:
    def __init__(self, title: str, total_pages: int):
        """
        Модель книги для отслеживания прогресса чтения.

        :param title: Название книги.
        :param total_pages: Общее количество страниц.

        Примеры:
        >>> book = Book("Мастер и Маргарита", 400)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(total_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if total_pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self.total_pages = total_pages
        self.current_page = 0

    def read_pages(self, pages: int) -> int:
        """
        Метод для фиксации прочитанных страниц.

        :param pages: Количество прочитанных страниц.
        :return: Текущая страница после чтения.
        :raise ValueError: Если количество страниц отрицательное или превышает остаток в книге.

        Примеры:
        >>> book = Book("Мастер и Маргарита", 400)
        >>> book.read_pages(50)
        50
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        ...

    def get_reading_progress(self) -> float:
        """
        Рассчитывает процент прогресса чтения.

        :return: Процент прочитанного (от 0.0 до 100.0).

        Примеры:
        >>> book = Book("Тестовая книга", 100)
        >>> # Предположим, прочитано 20 страниц
        >>> book.get_reading_progress()
        20.0
        """
        ...


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        """
        Абстрактная модель банковского счета.

        :param owner: Имя владельца счета.
        :param balance: Начальный баланс.

        Примеры:
        >>> account = BankAccount("Иван Иванов", 1000.50)
        """
        if not isinstance(owner, str):
            raise TypeError("Имя владельца должно быть строкой")
        self.owner = owner

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным при открытии")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета.

        :param amount: Сумма пополнения.
        :raise ValueError: Если сумма пополнения не положительная.

        Примеры:
        >>> account = BankAccount("Петр Петров", 0)
        >>> account.deposit(500.0)
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        ...

    def withdraw(self, amount: float) -> float:
        """
        Снятие наличных со счета.

        :param amount: Сумма для снятия.
        :return: Сумма, которая была снята.
        :raise ValueError: Если на счету недостаточно средств.

        Примеры:
        >>> account = BankAccount("Петр Петров", 1000)
        >>> account.withdraw(300)
        300.0
        """
        ...


class DataStack:
    def __init__(self, max_size: int):
        """
        Модель структуры данных "Стек" (LIFO).

        :param max_size: Максимальный размер стека.

        Примеры:
        >>> stack = DataStack(max_size=5)
        """
        if not isinstance(max_size, int):
            raise TypeError("Размер стека должен быть целым числом")
        if max_size <= 0:
            raise ValueError("Размер стека должен быть положительным")

        self.max_size = max_size
        self.stack_list = []

    def push(self, item: Any) -> None:
        """
        Добавление элемента в стек.

        :param item: Объект для добавления.
        :raise OverflowError: Если стек уже заполнен.

        Примеры:
        >>> stack = DataStack(3)
        >>> stack.push("data_1")
        """
        ...

    def pop(self) -> Any:
        """
        Извлечение последнего элемента из стека.

        :return: Извлеченный элемент.
        :raise IndexError: Если попытка извлечь из пустого стека.

        Примеры:
        >>> stack = DataStack(5)
        >>> # Допустим, добавили элемент 'A'
        >>> stack.pop()
        'A'
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

