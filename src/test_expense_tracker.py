import unittest
import csv
from datetime import date
from expense_tracker import load_expenses, save_expenses, get_expense_details

# You may need to update this path based on your project structure
import sys
sys.path.append('.')

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_expenses.csv'
        with open(self.test_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'description', 'category', 'amount'])
            writer.writerow(['2023-05-01', 'Groceries', 'Food', '50.0'])
            writer.writerow(['2023-05-03', 'Gas', 'Transportation', '30.0'])

    def tearDown(self):
        import os
        os.remove(self.test_file)

    def test_load_expenses(self):
        expenses = load_expenses(self.test_file)
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0]['date'], '2023-05-01')
        self.assertEqual(expenses[0]['description'], 'Groceries')
        self.assertEqual(expenses[0]['category'], 'Food')
        self.assertEqual(expenses[0]['amount'], '50.0')

    def test_save_expenses(self):
        expenses = [
            {'date': '2023-05-10', 'description': 'Dinner', 'category': 'Food', 'amount': 25.0},
            {'date': '2023-05-12', 'description': 'Movie', 'category': 'Entertainment', 'amount': 15.0}
        ]
        save_expenses(expenses, self.test_file)
        loaded_expenses = load_expenses(self.test_file)
        self.assertEqual(len(loaded_expenses), 2)
        self.assertEqual(loaded_expenses[0]['date'], '2023-05-10')
        self.assertEqual(loaded_expenses[0]['description'], 'Dinner')
        self.assertEqual(loaded_expenses[0]['category'], 'Food')
        self.assertEqual(loaded_expenses[0]['amount'], '25.0')

    def test_get_expense_details(self):
        # Simulate user input
        user_inputs = ['2023-05-15', 'Rent', 'Housing', '1000']
        with unittest.mock.patch('builtins.input', side_effect=user_inputs):
            expense = get_expense_details()
            self.assertEqual(expense['date'], '2023-05-15')
            self.assertEqual(expense['description'], 'Rent')
            self.assertEqual(expense['category'], 'Housing')
            self.assertEqual(expense['amount'], 1000.0)