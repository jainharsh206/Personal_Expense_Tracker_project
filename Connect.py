from pymongo import MongoClient

def harshi_value():
    print("Welcome Pymongo")
    client = MongoClient("mongodb://localhost:27017/")
    database = client["Expense_data"]  
    return database