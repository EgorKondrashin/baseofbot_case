import pytest
from models import Book
from library_management import BookManager

@pytest.fixture
def book_manager():
    return BookManager()

@pytest.fixture
def books():
    return [
        Book(id=1, title='Book One', author='Author One', year='2001', status='в наличии'),
        Book(id=2, title='Book Two', author='Author Two', year='2002', status='выдана')
    ]

def test_add_book(book_manager, books):
    new_books = book_manager.add_book(title='Book Three', author='Author Three', year='2003', books=books)
    assert len(new_books) == 3
    assert new_books[-1].title == 'Book Three'
    assert new_books[-1].author == 'Author Three'
    assert new_books[-1].year == '2003'
    assert new_books[-1].status == 'в наличии'

def test_delete_book(book_manager, books):
    new_books = book_manager.delete_book(book_id=1, books=books)
    assert len(new_books) == 1
    assert new_books[0].id == 2

def test_delete_book_not_found(book_manager, books):
    new_books = book_manager.delete_book(book_id=999, books=books)
    assert new_books is None

def test_search_book_for_title(book_manager, books):
    found_books = book_manager.search_book_for_title(keyword='one', books=books)
    assert len(found_books) == 1
    assert found_books[0].title == 'Book One'

def test_search_book_for_author(book_manager, books):
    found_books = book_manager.search_book_for_author(keyword='two', books=books)
    assert len(found_books) == 1
    assert found_books[0].author == 'Author Two'

def test_search_book_for_year(book_manager, books):
    found_books = book_manager.search_book_for_year(keyword='2001', books=books)
    assert len(found_books) == 1
    assert found_books[0].year == '2001'

def test_change_status_book(book_manager, books):
    new_books = book_manager.change_status_book(book_id=1, status='выдана', books=books)
    assert new_books[0].status == 'выдана'

def test_change_status_book_not_found(book_manager, books):
    new_books = book_manager.change_status_book(book_id=999, status='выдана', books=books)
    assert new_books is None
