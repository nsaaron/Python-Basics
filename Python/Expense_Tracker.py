print("Welcome to the Expense Tracker!")
user_options = ["Add a new expense", "View all expenses", "View total expenses", "View expenses by category", "Exit"]
class Expense:
    
    def __init__(self):
        self.description = "description"
        self.amount = 0.1
        self.category= "category" 
    
class ExpenseTracker:
    
    def __init__(self):
        self.expenseslist = []
        
    def add_expense(self):
        new_item = Expense()  # Create new item each time an expense is added
        new_item.description = input("Enter a Description of the expense: ")
        new_item.amount = float(input("Enter the amount:"))
        new_item.category = input("Enter the category:")
        self.expenseslist.append(new_item)
        
    def view_all_expenses(self):
        print("All Expenses:")
        for expense in self.expenseslist:
            print(f"Description: {expense.description}, {expense.amount} (Category: {expense.category})") 
        
    def view_total_expenses(self):
        total = sum(expense.amount for expense in self.expenseslist)  # Add the amount of each expense's amount in the list to the end total
        print(f"Expenses Total: ${total:.2f}")
       
    def view_expenses_by_category(self):
        catfilter = input("Enter the Category to filter by: ")
        print(f"Expenses in Category: {catfilter}")  
        for eachitem in self.expenseslist:  # Run through the list and print out the matching category entries
            if catfilter == eachitem.category:
                print(f"Description: {eachitem .description}, {eachitem.amount}")
        
##main  
if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    while True:
        print("What would you like to do?")
        counter = 1
        for options in user_options:
            print(f'{counter}- {options}')
            counter += 1
        user_selection = int(input("Enter your choice:"))
        
        if user_selection == 1:
            tracker.add_expense()
            
        elif user_selection == 2:
            tracker.view_all_expenses()
            
        elif user_selection == 3:
            tracker.view_total_expenses()
            
        elif user_selection == 4:
            tracker.view_expenses_by_category()
            
        elif user_selection == 5:
            break
    
