import csv
from faker import Faker
import random

genres = ["Fantasy", "Mystery", "Romance", "Historical", "Thriller"]


class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.genre}', '{self.publication_date}')"


class Shelf:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.genre not in self.books:
            self.books[book.genre] = []
        self.books[book.genre].append(book)

    def sorted_books(self):
        for genre in self.books:
            self.books[genre] = sorted(self.books[genre], key=lambda book: book.title)

    def print_books(self):
        for genre, books in self.books.items():
            print("-" * 20)
            print(f"Genre: {genre}")
            print("-" * 20)
            for book in books:
                print(f"{book.title} by {book.author} ({book.publication_date})")


def create_books():
    fake = Faker()
    books = set()

    for _ in range(20):
        publication_date = fake.date_between(start_date='-100y', end_date='today')
        book = Book(
            title=fake.sentence(),
            author=fake.name(),
            genre=random.choice(genres),
            publication_date=publication_date.strftime("%Y-%m-%d")
        )
        books.add(book)  # add set

    return books


def save_books_csv(books, filename="books_database.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Author", "Title", "Genre", "PublicationDate"])
        for book in books:
            writer.writerow([book.author, book.title, book.genre, book.publication_date])


books = create_books()

save_books_csv(books)

shelf = Shelf()
for book in books:
    shelf.add_book(book)

shelf.sorted_books()

shelf.print_books()
