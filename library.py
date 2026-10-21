
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("Things Fall Apart", "Chinua Achebe")

# Display the books
print("LIBRARY BOOKS")
print(book1)
print(book2)
print(book3)

print("\nBORROWING BOOKS")
book1.borrow()
book2.borrow()

print("\nUPDATED BOOK STATUS")
print(book1)
print(book2)

print("\nRETURNING BOOKS")
book1.return_book()

print("\nFINAL BOOK STATUS")
print(book1)
print(book2)
print(book3)
