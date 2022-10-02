from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверка добавления книг.
    def test_add_new_book_find_added_book(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        collector.add_new_book(book_name)

        assert book_name in collector.get_books_rating()


    # Нельзя добавить одну и ту же книгу дважды.
    def test_get_books_rating_only_one_book_with_the_same_name(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        assert len(collector.get_books_rating()) == 1

    # Нельзя выставить рейтинг книге, которой нет в списке.
    def test_get_books_with_specific_rating_book_not_added(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'
        rating = 10

        collector.set_book_rating(book_name, rating)

        assert not book_name in collector.get_books_with_specific_rating (rating)

    # Нельзя выставить рейтинг меньше 1.
    def test_set_book_rating_less_than_one(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'
        rating = 0

        collector.set_book_rating(book_name, rating)

        assert len(collector.get_books_with_specific_rating (rating)) == 0

    # Нельзя выставить рейтинг больше 10.
    def test_set_book_rating_more_than_ten(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'
        rating = 11

        collector.set_book_rating(book_name, rating)

        assert len(collector.get_books_with_specific_rating (rating)) == 0

    # У не добавленной книги нет рейтинга.
    def test_get_book_rating_for_no_added_book(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        assert collector.get_book_rating(book_name) is None

    # Добавление книги в избранное.
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
    def test_add_book_in_favorites_not_added_in_books_raiting(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        collector.add_book_in_favorites(book_name)

        assert not book_name in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного.
    def test_delete_book_from_favorite(self):
        collector = BooksCollector()
        book_name = 'Маша и медведь'

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(book_name)

        assert not book_name in collector.get_list_of_favorites_books()
