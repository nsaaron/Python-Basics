class Expense:
    
    def __init__(self):
        self.ammount = 50.0
        self.description = ""
        self.category= "" 
    
class ExpenseTracker:
    
    def __init__(self):
        self.expenses = []
        
    def add_expense(description, amount, category):
        print("Test")
        
    def view_all_expenses():
        print("Test")
        
    def view_total_expenses():
        print("Test")
        
    def View_expenses_by_category(category):
        print("Test")
        
        
##main  
if __name__ == "__main__":
    tracker = ExpenseTracker()
    expense = Expense()
    
    print("Welcome to the Expense Tracker!")