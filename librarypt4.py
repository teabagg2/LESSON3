class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")
            
        else:
            print(f"Sorry, '{self.title}' by {self.author} is already borrowed.")
            

book1 = Book("things fall apart", "Chinua Achebe")
book2 = Book("the alchemist", "Paulo Coelho")
book3 = Book("animal farm", "George Orwell")

book1.borrow()
book2.borrow()
book3.borrow()

