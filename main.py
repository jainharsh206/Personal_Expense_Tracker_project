from expense import adding_expense, checking_Budget, delete_expense
from calculation import total_expense, category_report, monthly_report


def menu():
    while True:
        print("Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Deleted Expense")
        print("4. Total Expense")
        print("5. Category Report")
        print("6. Monthly Report")
        print("7. Exits")

        choice = input("Choose an option: ")

        if choice == '1':
            print("==== Add Expense ====")
            amount = float(input("Amount: "))
            category = input("Category: ")
            User_experience = input("User_experience: ")
            date = input("Date (YYYY-MM-DD): ") or None
            adding_expense(amount, category, User_experience, date)

        elif choice == '2':
            print("==== See all Expense ====")
            checking_Budget()

        elif choice  == '3':
             date = input("Enter date yyy-mm-dd")
             amount = input("Enter amount")
             category = input("Enter Category")
             User_experience = input("Enter User Experience: ")
             delete_expense(amount, category, User_experience, date)

        elif choice == '4':
            print("==== All overall total expense ====")
            total_expense()  

        elif choice == '5':
            category_report()  

        elif choice == '6':
            m = int(input("Enter month[1-12]: "))
            y = int(input("Enter year: "))
            monthly_report(m, y)   
        
        elif choice == '7':
            print(" Invalid option.")   
            break 


if __name__ == "__main__":
    menu()            