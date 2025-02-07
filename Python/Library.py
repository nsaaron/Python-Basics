
class library:
    
    def __init__(self):
        self.available_books = ["Python Basics", "Data Structures", "Artificial Intelligence", "Machine Learning"]
        self.borrowed_books = []
    
    def displaybooks(self):
        print("Available Books:")
        for books in self.available_books:
            print(f"- {books}")
        
    def lend_book(self, book_name):
        if book_name not in self.available_books:
            print(f"{book_name} is not in the Library.")
        if book_name in self.available_books:
            self.available_books.remove(book_name)
            self.borrowed_books.append(book_name)
            print(f"You borrowed '{book_name}'. Enjoy reading!")
        
    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            self.available_books.append(book_name)
            print(f"Thank you for returning '{book_name}'! ")
    
class User:
    def __init__(self, library):
        self.library = library
        
    def borrow_book(self):
        book_name = input("Which book would you like to borrow? ")
        self.library.lend_book(book_name)
        
    def return_book(self):
        book_name = input("Which book would you like to return? ")
        self.library.return_book(book_name)

##main  
if __name__ == "__main__":
    library = library()
    userclass = User(library) 
   
    while True:        
        print("Welcome to the Library!")
        library.displaybooks()
        usel = (input("Enter your choice:"))
        if not usel.strip():
            print("Enter a selection")
        else:
            try:
                usel = int(usel)
            except ValueError:
                print("Invalid Input, Enter a Number")
        
        if usel == 1:
            library.displaybooks()
        elif usel == 2:
            userclass.borrow_book()
        elif usel == 3:
            userclass.return_book()
        elif usel == 4:
            print("Goodbye!")
            break
