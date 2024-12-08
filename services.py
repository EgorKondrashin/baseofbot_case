'''Файл для работы с файловой системой.'''
import json
from dataclasses import asdict
from typing import List

from models import Book


class FileManager:
    '''Класс для работы с файлом.'''
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_books(self) -> List[Book]:
        '''Метод для загрузки всех книг из файла.'''
        try:
            with open(self.file_path, encoding='utf-8') as file:
                books_data = json.load(file)
                return [Book(**book_data) for book_data in books_data]
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []

    def save_books(self, books: List[Book]):
        '''Метод для записи книг в файл.

        :params books: Список книг.
        '''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            books = [asdict(book) for book in books]
            json.dump(books, file, indent=4, ensure_ascii=False)
