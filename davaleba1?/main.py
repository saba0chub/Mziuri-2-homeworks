class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self):
        return f"{self.title} ({self.year})"


    # @property ragacas afuwebs
    def is_classic(self):
        return (2026 - self.year) >= 50


class EBook(Book):
    def __init__(self, title, author, year, size_mb):
        super().__init__(title, author, year)
        self.size_mb = size_mb

    def __str__(self):
        return f"{self.title} by {self.author} [{self.size_mb}MB]"


class Library:
    pass

ebook = EBook("Dune", "Frank Herbert", 1965, 2.4)
book = Book("Dune", "Frank Herbert", 1999)

print(f"Is classic? {ebook.is_classic()}")