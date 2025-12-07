class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor that initializes book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor that prints deletion message."""
        print(f"Deleting {self.title}")