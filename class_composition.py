class Bookshelf:

    def __init__(self, *books):
        self.books = books
        print(type(self.books))

    def __str__(self):
        return f"There are {len(self.books)} books in the bookshelf"



class Book:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book's name is  {self.name}"

book1 = Book("one")
book2 = Book("two")

shelf_1 = Bookshelf(book1, book2)

print(shelf_1)
