# Test case

Этот проект представляет собой "Систему управления библиотекой". Был создан в целях тестового задания компании BaseOfBot

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Функционал](#функционал)

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/EgorKondrashin/baseofbot_case.git
    cd baseofbot_case
    ```

2. Создайте и активируйте виртуальное окружение.

3. Установите зависимости:

    ```bash
    pip install -U pytest
    ```
   
## Использование

1. Для запуска системы используйте команду:
   
   ```bash
    python main.py
    ```

2. Для заупска тестов используйте команду:
   
   ```bash
    pytest tests.py
    ```

## Функционал

1. При запуске системы в консоль приходят сообщения с пунктами возможного функционала:
   - Добавление книги
   - Удаление книги
   - Поиск книги (по названию, автору или году написания)
   - Просмотр всех книг
   - Изменение статуса книги
   - Выход

2. Добавление книги:
   - При выборе пункта с добавлением книги, программа будет запрашивать название книги (title),
   автора (author) и год издания (year). После чего добавляет новую книгу с уникальным
   идентификатором и статусом 'в наличии' в файл.

3. Удаление книги:
   - При выборе пункта с удалением книги, программа будет запрашивать уникальный идентификатор (id) книги,
   которую вы хотите удалить. После чего обновляет файл с книгами, удаляя необходимую книгу.

4. Поиск книги (по названию, автору или году написания):
   - При выборе пункта с поиском книги, программа будет запрашивать вариант поиска (1. title, 2. author, 3. year),
   необходимо ввести цифру с нужным вариантом. Далее программа будет запрашивать ключевое слово/год,
   по которому будет производится поиск и выведет список книг удовлетворяющие запросу.

5. Просмотр всех книг:
   - При выборе пункта с просмотром всех книг, программа выводит список всех книг.

6. Изменение статуса книги:
   - При выборе пункта с изменением статуса книги, программа будет запрашивать уникальный идентификатор (id) книги и 
   предложит выбрать статус для книги 'Введите цифру, где (1. в наличии, 2. выдана)',
   необходимо ввести цифру с нужным вариантом. После чего программа заменит статус указанной книги,
   и сохранит изменения в файл.

7. Выход:
   - При выборе пункта 'Выход', программа попращается, и завершит работу.
