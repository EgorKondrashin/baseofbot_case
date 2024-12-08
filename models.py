'''Файл с моделью книги.'''

from dataclasses import dataclass

@dataclass
class Book:
    '''Модель книги'''
    id: int
    title: str
    author: str
    year: str
    status: str = 'в наличии'
