import unittest
from app import app
from app import get_db_connection

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.conn = get_db_connection()

    def tearDown(self):
        self.conn.close()

    def test_add_asset(self):
        response = self.app.post('/add_asset', data={
            'asset_name': 'Test Asset',
            'serial_number': '123456',
            'category': 'Test Category',
            'location': 'Test Location',
            'status': 'in_use'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after adding asset
        # Check if the added asset exists in the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM assets WHERE asset_name = 'Test Asset'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)  # Asset should exist in the database

    def test_edit_asset(self):
        # Assuming there is an asset with id=1 in the database
        response = self.app.post('/edit_asset/1', data={
            'asset_name': 'Updated Asset Name',
            'serial_number': '789012',
            'category': 'Updated Category',
            'location': 'Updated Location',
            'status': 'in_storage'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after editing asset
        # Check if the asset with id=1 has been updated in the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM assets WHERE id = 1")
        result = cursor.fetchone()
        self.assertIsNotNone(result)  # Asset should exist in the database
        self.assertEqual(result[1], 'Updated Asset Name')  # Asset name should be updated

    def test_delete_asset(self):
        # Assuming there is an asset with id=2 in the database
        response = self.app.post('/delete_asset/2')
        self.assertEqual(response.status_code, 302)  # Redirect after deleting asset
        # Check if the asset with id=2 has been deleted from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM assets WHERE id = 2")
        result = cursor.fetchone()
        self.assertIsNone(result)  # Asset should not exist in the database

if __name__ == '__main__':
    unittest.main()
