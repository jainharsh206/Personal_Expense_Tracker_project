from Connect import harshi_value
from datetime import datetime

database = harshi_value()
Expense_Tracker = database.Expense_Tracker


def adding_expense(amount, category, User_experience, date=None):
    if date is None:
        date = datetime.today()
    else:
        date = datetime.strptime(date, "%Y-%m-%d")
    
    Expense_Tracker.insert_one({
        "amount": amount,
        "category": category.lower(),
        "User_experience": User_experience,
        "date": date
    })
    print("Expense has added Successfully.")

def checking_Budget():
    # Get all expenses sorted by date in descending order (latest first)
    all_expenses = Expense_Tracker.find().sort("date", -1)

    print(" Date       |  Category     |  Amount |  Note")
    print("-" * 55)
    
    # Loop through each expense and print details
    for exp in all_expenses:
        date = exp["date"].strftime("%Y-%m-%d")  # format date as string
        category = exp["category"].title()       # capitalize category
        amount = exp["amount"]                   # expense amount
        note = exp.get("User_experience", "")    # get note (optional)

        print(f"{date} | {category:} | ₹{amount:} | {note}")

def delete_expense(amount, category, user_experience, date):
    query = {
        "amount": amount,
        "category": category.lower(),             # case-insensitive match
        "user_experience": user_experience,
        "date": date                              # make sure date is stored as datetime
    }

    result = Expense_Tracker.delete_one(query)

    if result.deleted_count > 0:
        print("🗑️ Expense deleted successfully.")
    else:
        print("❌ No matching expense found.")
























































# def checking_Budget():
#     for exp in Expense_Tracker.find().sort("date", -1):
#         print(f"{exp['date'].date()} | {exp['category'].title()} | ₹{exp['amount']} | {exp['User_experience']}")

## deleting function are pending 

