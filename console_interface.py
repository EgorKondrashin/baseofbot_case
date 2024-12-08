from library_management import BookManager
from services import FileManager

library_manager = BookManager()


def display_menu():
    '''Меню с пунктами возможного функционала.'''
    print('Система управления библиотекой.')
    print('1. Добавление книги')
    print('2. Удаление книги')
    print('3. Поиск книги (по названию, автору или году написания)')
    print('4. Просмотр всех книг')
    print('5. Изменение статуса книги')
    print('6. Выход')


class InterfaceManager:

    @staticmethod
    def add_book_interface(file_manager: FileManager):
        '''Метод для добавления книги в библиотеку.'''
        title = ''
        while not title:
            title = input('Введите название книги (не может быть пустым): ')

        author = ''
        while not author or author.isdigit():
            author = input('Введите автора книги (не может быть пустым): ')

        year = ''
        while not year or not year.isdigit():
            year = input('Введите год издания книги (не может быть пустым): ')

        books = file_manager.load_books()
        books = library_manager.add_book(title=title, author=author, year=year, books=books)
        file_manager.save_books(books)
        print(f'Была добавлена книга: {books[-1]}')


    @staticmethod
    def delete_book_interface(file_manager: FileManager):
        '''Метод для удаления книги из библотеки.'''
        book_id = ''
        while not book_id or not book_id.isdigit():
            book_id = input('Введите id книги, которую необходимо удалить: ')
        books = file_manager.load_books()
        books = library_manager.delete_book(book_id=int(book_id), books=books)
        if books is None:
            return
        file_manager.save_books(books)
        print(f'Книга с id {book_id} была удалена!')

    @staticmethod
    def search_book_interface(file_manager: FileManager):
        '''Метод для поиска книг по title, author или year.'''
        choice_method_search = {
            '1': library_manager.search_book_for_title,
            '2': library_manager.search_book_for_author,
            '3': library_manager.search_book_for_year
        }

        choice_answer_user = {
            '1': 'Введите слово по которому будет производиться поиск: ',
            '2': 'Введите слово по которому будет производиться поиск: ',
            '3': 'Введите год по которому будет производиться поиск: '
        }
        choice = ''
        while not choice or not choice.isdigit() or not (choice == '1' or choice == '2' or choice == '3'):
            choice = input('По какому полю хотите осуществить поиск:\n1. title\n2. author\n3. year\nВведите цифру: ')

        method_search = choice_method_search.get(choice)

        keyword = ''
        while not keyword:
            keyword = input(choice_answer_user.get(choice))
        books = file_manager.load_books()
        books = method_search(keyword=keyword.lower().strip(), books=books)
        print(books)

    @staticmethod
    def view_all_books_interface(file_manager: FileManager):
        '''Метод для отображения всех книг.'''
        books = file_manager.load_books()
        print(books)

    @staticmethod
    def change_book_status_interface(file_manager: FileManager):
        '''Метод для изменения статуса книги.'''
        choice_status = {'1': 'в наличии', '2': 'выдана'}
        book_id = ''
        while not book_id or not book_id.isdigit():
            book_id = input('Введите id книги, статус которой необходимо изменить: ')
        choice = ''
        while not choice or not choice.isdigit() or not (choice == '1' or choice == '2'):
            choice = input('Какой статус хотите присвоить книге:\n1. в наличии\n2. выдана\nВведите цифру: ')
        status = choice_status.get(choice)
        books = file_manager.load_books()
        books = library_manager.change_status_book(book_id=int(book_id), status=status, books=books)
        if books:
            file_manager.save_books(books)
