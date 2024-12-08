from console_interface import display_menu, InterfaceManager
from services import FileManager


def main():
    file_manager = FileManager('library/books.json')

    actions = {
        '1': InterfaceManager.add_book_interface,
        '2': InterfaceManager.delete_book_interface,
        '3': InterfaceManager.search_book_interface,
        '4': InterfaceManager.view_all_books_interface,
        '5': InterfaceManager.change_book_status_interface,
        '6': 'выход'
    }

    flag = True

    while flag:
        display_menu()

        choice = input('Выберите действие: ')

        action = actions.get(choice)

        if action == 'выход':
            flag = False
            print('До встречи!')
        elif action:
            function = action(file_manager)
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
