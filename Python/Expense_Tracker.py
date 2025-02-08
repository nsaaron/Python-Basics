print("Welcome to the Expense Tracker!")
user_options = ["Add a new expense", "View all expenses", "View total expenses", "View expenses by category", "Exit"]
class Expense:
    
    def __init__(self):
        self.amount = 50.0
        self.description = ""
        self.category= "" 
    
class ExpenseTracker:
    
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, expense):
        item.description = input("Enter a Description of the expense: ")
        item.amount = float(input("Enter the amount:"))
        item.category = input("Enter the category:")
        tracker.expenses.append(item)
        
    def view_all_expenses(self):
        print("PLACEHOLDER")
        
    def view_total_expenses():
        print("Test")
        
    def View_expenses_by_category(category):
        print("Test")
        
        
##main  
if __name__ == "__main__":
    tracker = ExpenseTracker()
    item = Expense()
    
    while True:
        print("What would you like to do?")
        counter = 1
        for options in user_options:
            print(f'{counter}- {options}')
            counter += 1
        user_selection = int(input("Enter your choice:"))
        
        if user_selection == 1:
            tracker.add_expense(item)
            
        elif user_selection == 2:
            tracker.view_all_expenses()
            
        elif user_selection == 3:
            print("placeholder")
            
        elif user_selection == 4:
            print("placeholder")
            
        elif user_selection == 5:
            break
    
