class Book:
    def __init__(self, title: str, author: str):
        """Initialize base Book class with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize EBook, inheriting from Book, with additional file_size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize PrintBook, inheriting from Book, with additional page_count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize Library with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)