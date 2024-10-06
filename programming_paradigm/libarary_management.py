# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def _init_(self, title, author):
        self.title = title          # Public attribute for the book's title
        self.author = author        # Public attribute for the book's author
        self._is_checked_out = False # Private attribute to track if the book is checked out

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""
    
    def _init_(self):
        self._books = []  # Private list to store book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.check_out():
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book.return_book():
                return True
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")


# Note: The main function for testing the library will be in the provided main.py file.