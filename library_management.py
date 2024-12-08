'''Файл для управления библиотекой.'''

import json
from typing import List

from models import Book


class BookManager:
    '''Модель управления книгами.'''

    def add_book(
            self,
            title: str,
            author: str,
            year: int,
            books: List[Book]
    ) -> List[Book]:
        '''Метод для добавления новой книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param books: Список книг.
        :return: Обновленный список книг с добавленной новой книгой.
        '''
        book = Book(
            id=(books[-1].id + 1 if books else 1),
            title=title,
            author=author,
            year=year,
            status='в наличии'
        )
        books.append(book)
        return books

    def delete_book(self, book_id: int, books: List[Book]) -> List[Book]:
        '''Метод для удаления книги по id.

        :param book_id: Идентификатор книги, которую нужно удалить.
        :param books: Список книг.
        :return: Обновленный список книг.
        '''
        try:
            book = self._find_book(book_id, books)
        except ValueError:
            print('Книга с таким id не найдена!')
            return
        books = [book for book in books if book.id != book_id]
        return books

    def search_book_for_title(self, keyword: str, books: List[Book]) -> List[Book]:
        '''Метод для поиска книги по title.

        :param keyword: Ключевое слово для поиска в названии книги.
        :param books: Список книг.
        :return: Список книг, содержащих ключевое слово в названии.
        '''
        books = [book for book in books if keyword in book.title.lower()]
        return books

    def search_book_for_author(self, keyword: str, books: List[Book]) -> List[Book]:
        '''Метод для поиска книги по author.

        :param keyword: Ключевое слово для поиска в авторе книги.
        :param books: Список книг.
        :return: Список книг, содержащих ключевое слово в авторе.
        '''
        books = [book for book in books if keyword in book.author.lower()]
        return books

    def search_book_for_year(self, keyword: str, books: List[Book]) -> List[Book]:
        '''Метод для поиска книги по year.

        :param keyword: Ключевое слово для поиска в годе издания книги.
        :param books: Список книг.
        :return: Список книг, содержащих ключевое слово в годе издания.
        '''
        books = [book for book in books if keyword in book.year]
        return books

    def change_status_book(self, book_id: int, status: str, books) -> List[Book]:
        '''Метод для изменения статуса книги.

        :param book_id: Идентификатор книги, статус которой нужно изменить.
        :param status: Новый статус книги.
        :param books: Список книг.
        :return: Обновленный список книг.
        '''
        try:
            book = self._find_book(book_id, books)
        except ValueError:
            print('Книга с таким id не найдена!')
            return
        book.status = status
        return books

    def _find_book(self, book_id: int, books: List[Book]) -> Book:
        '''Метод для поиска книги по id.

        :param book_id: Идентификатор книги, которую нужно найти.
        :param books: Список книг.
        :return: Найденная книга.
        :raises ValueError: Ошибка, если книга с указанным id не найдена.
        '''
        for book in books:
            if book.id == book_id:
                return book
        raise ValueError('Book not found')