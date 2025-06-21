class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return self.get_details()


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"{self.title} by {self.author} [EBook, {self.file_size}MB]"

    def __str__(self):
        return self.get_details()


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{self.title} by {self.author} [PrintBook, {self.page_count} pages]"

    def __str__(self):
        return self.get_details()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")

    def list_books(self):
        for book in self.books:
            print(book)  # Uses __str__ automatically
