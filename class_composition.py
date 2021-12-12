#counter part of inheritance
#inheritance means by this program- a bookself is a book
#composition is - 

class Bookself:
    def __init__(self, *books):
        self.books=books

        
    def __str__(self):
        return f"Bookself with {len(self.books)} books."
    
class Book:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f"Book {self.name}"
    
book=Book("Harry potter")
book2=Book("Python")
shelf=Bookself(book,book2)
print(shelf)