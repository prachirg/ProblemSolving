class Book:
    def __init__(self, bookName, author):
        self.bookName = bookName
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print("Book added:",book)

    # def display_books(self):
    #     print("Available books:", self.books)
    #
    # def borrow_book(self,remove_book):
    #     if remove_book in self.books:
    #         self.books.remove(remove_book)
    #         print("Book borrowed:", remove_book)
    #
    # def return_book(self,return_book):
    #     if return_book not in self.books:
    #         self.books.append(return_book)
    #     print("Book returned:",return_book)

lib = Library()
book = Book("Harry Potter 1", "JK Rowling")
lib.add_books(book)

# lib.add_books('Harry Potter 1')
# lib.add_books('Harry Potter 2')
# lib.add_books('Harry Potter 3')
# lib.add_books('Harry Potter 4')
# lib.add_books('Harry Potter 5')
# lib.display_books()
# lib.borrow_book("Harry Potter 6")
# lib.display_books()
# lib.return_book("Harry Potter 2")
# lib.display_books()




