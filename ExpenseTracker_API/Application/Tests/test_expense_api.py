import unittest
import requests

class TestExpenseAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000/expenses'  # Update the base URL accordingly

    def test_add_expense(self):
        # Test adding an expense
        data = {
            'description': 'Test expense',
            'amount': 10.50,
            'category': 'Test',
            'expenseDate': '2024-04-01T12:00:00'  # Update with appropriate date
        }
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 200)  # Assuming the server returns 200 on success

    def test_get_expense(self):
        # Test getting an expense
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)  # Assuming the server returns 200 on success
        # Add assertions to check if the response data matches expected format

    def test_edit_expense(self):
        # Test editing an expense
        expense_id = 0  # Assuming you have an existing expense ID to edit
        data = {
            'description': 'Updated expense description',
            'amount': 20.00,
            'category': 'Updated category',
            'expenseDate': '2024-04-01T12:00:00'  # Update with appropriate date
        }
        response = requests.put(f'{self.base_url}/{expense_id}', json=data)
        self.assertEqual(response.status_code, 200)  # Assuming the server returns 200 on success

    def test_delete_expense(self):
        # Test deleting an expense
        expense_id = 0  # Assuming you have an existing expense ID to delete
        response = requests.delete(f'{self.base_url}/{expense_id}')
        self.assertEqual(response.status_code, 200)  # Assuming the server returns 200 on success

if __name__ == '__main__':
    unittest.main()
