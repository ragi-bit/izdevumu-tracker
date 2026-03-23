expenses = []

def add_expense(date, amount, category, description):
    expense = {
        "date": date,
        "amount": float(amount),
        "category": category,
        "description": description
    }
    expenses.append(expense)

def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)

def get_expenses():
    return expenses

def filter_by_month(month):
    return [e for e in expenses if e["date"].startswith(month)]

def get_summary():
    total = sum(e["amount"] for e in expenses)
    categories = {}

    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    return total, categories