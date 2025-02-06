class library:
    
    def __init__(self):
        self.available_books = ["Python Basics", "Data Structures", "Artificial Intelligence", "Machine Learning"]
        self.borrowed_books = []
    
    def displaybooks(self):
        print("Available Books:")
        for books in self.available_books:
            print(f"- {books}")
        
    def lend_book(self, book_name):
        print("Test")
        
    def return_book(book_name):
        print("Test")
    
class User:
    
    def borrow_book(self):
        print("Test")
        
    def return_book(self):
        print("Test")
     
     
##main     
while True:        
    libclass = library()
    userclass = User()
    #testclass.displaybook()
    #print(testclass.available_books)
    #testuser.borrow_book()
    
    print("Welcome to the Library!")
    print("Available Books:")
    for eachbook in libclass.available_books:
        print("- %s" % eachbook)
    print(
        """
        Which would you like to do?
        1. View availale Books
        2. Borrow a Book
        3. Return a Book
        4. Exit
        """
        )
        
    usel = int(input("Enter your choice:"))
    
    if usel == 1:
        libclass.displaybooks()
