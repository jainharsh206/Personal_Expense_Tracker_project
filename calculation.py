from Connect import harshi_value
from datetime import datetime

database = harshi_value()
Expense_Tracker = database.Expense_Tracker

def total_expense():
    total = 0  # Start with zero

    # Go through each expense in the collection
    for expense in Expense_Tracker.find():
        total += expense["amount"]  # Add the amount to total

    print(f" Total Kharcha ------------>  ₹{total}")


def category_report():
    all_expenses = Expense_Tracker.find()
    category_totals = {}

    for expense in all_expenses:
        category = expense["category"].lower() 
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    print("|  Category     |  Price ")
    print("-" * 29)

    for category, total in category_totals.items():
        print(f"|{category.title()}: | ₹{total}|")
    
def monthly_report(month, year):
    start_date = datetime(year, month, 1)
    
    if month < 12:
        end_date = datetime(year, month + 1, 1)
    else:
        end_date = datetime(year + 1, 1, 1)

    results = Expense_Tracker.find({"date": {"$gte": start_date, "$lt": end_date}})

    category_totals = {}
    total = 0

    for exp in results:
        category = exp['category']
        amount = exp['amount']
        total += amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print(f"\n📅 Monthly Report ({month}/{year}):")
    for cat in category_totals:
        print(cat.title(), ":", f"₹{category_totals[cat]}")
    
    print("--------------------------")
    print("|Total Expense:| ₹", total)
    print("\n")
 
