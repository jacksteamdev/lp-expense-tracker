import csv
from datetime import datetime


def load_expenses(file_path="expenses.csv"):
    """Load expenses from a CSV file."""
    expenses = []
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return expenses


def save_expenses(expenses, file_path="expenses.csv"):
    """Save expenses to a CSV file."""
    fieldnames = ["date", "description", "category", "amount"]
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
    except IOError:
        print(f"Error writing to file: {file_path}")


def get_expense_details():
    """Prompt the user for expense details."""
    date_str = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    category = input("Enter the category: ")
    amount_str = input("Enter the amount: ")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        amount = float(amount_str)
    except ValueError:
        print("Invalid date or amount format.")
        return None

    return {
        "date": date.isoformat(),
        "description": description,
        "category": category,
        "amount": amount,
    }


def add_expense(expenses):
    """Add a new expense."""
    expense = get_expense_details()
    if expense:
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully.")


def list_expenses(expenses):
    """Display all expenses in a tabular format."""
    if not expenses:
        print("No expenses found.")
        return

    print(
        "{:<10} {:<20} {:<15} {:<10}".format(
            "Date", "Description", "Category", "Amount"
        )
    )
    print("-" * 60)

    for expense in sorted(
        expenses, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=True
    ):
        date = datetime.strptime(expense["date"], "%Y-%m-%d").date()
        amount = float(expense["amount"])  # Convert amount to float
        print(
            "{:<10} {:<20} {:<15} {:<10.2f}".format(
                date.isoformat(), expense["description"], expense["category"], amount
            )
        )


def display_menu():
    """Display the menu options."""
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Quit")


if __name__ == "__main__":
    expenses = load_expenses()
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
