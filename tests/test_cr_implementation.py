import unittest
import json
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))
from app import app, USERS, DATA_FILE

class TestInventoryTracker(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
        # Setup mock data file
        self.test_data_file = 'test_items.json'
        # Override DATA_FILE in app context (This is tricky with global vars, 
        # but for this simple app we can monkeypatch the save/load functions or just backup/restore)
        # Better approach for this simple script: Just ensure we clean up
        
        # Backup original data
        if os.path.exists(DATA_FILE):
            os.rename(DATA_FILE, DATA_FILE + '.bak')
            
        # Create empty data
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

    def tearDown(self):
        # Restore original data
        if os.path.exists(DATA_FILE + '.bak'):
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
            os.rename(DATA_FILE + '.bak', DATA_FILE)
        elif os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def add_item(self, name, quantity):
        return self.app.post('/add', data=dict(
            name=name,
            quantity=quantity
        ), follow_redirects=True)

    def test_cr003_role_access(self):
        """CR-003: Test Role Management"""
        # 1. Admin Login
        rv = self.login('admin', 'admin')
        self.assertIn(b'Welcome', rv.data)
        self.assertIn(b'Admin', rv.data)
        self.logout()
        
        # 2. Viewer Login
        rv = self.login('viewer', 'viewer')
        self.assertIn(b'Viewer', rv.data)
        
        # Viewer tries to add item
        rv = self.app.post('/add', data=dict(name='Test', quantity=10), follow_redirects=True)
        # Should not add, length should still be 0
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 0)

    def test_cr001_edit_item(self):
        """CR-001: Test Item Editing"""
        self.login('manager', 'manager')
        
        # Add Item
        self.add_item('Old Name', 10)
        
        # Edit Item (ID should be 1)
        rv = self.app.post('/edit/1', data=dict(
            name='New Name',
            quantity=20
        ), follow_redirects=True)
        
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            
        self.assertEqual(data[0]['name'], 'New Name')
        self.assertEqual(data[0]['quantity'], '20')
        self.assertIn('last_modified', data[0])
        self.assertEqual(data[0]['modified_by'], 'manager')

    def test_cr002_search_filter(self):
        """CR-002: Test Search & Filter"""
        self.login('admin', 'admin')
        self.add_item('Apple', 10)
        self.add_item('Banana', 20)
        self.add_item('Cherry', 30)
        
        # Test Search
        rv = self.app.get('/dashboard?search=apple')
        self.assertIn(b'Apple', rv.data)
        self.assertNotIn(b'Banana', rv.data)
        
        # Test Quantity Filter (Min)
        rv = self.app.get('/dashboard?min_qty=25')
        self.assertNotIn(b'Apple', rv.data)
        self.assertNotIn(b'Banana', rv.data)
        self.assertIn(b'Cherry', rv.data)

if __name__ == '__main__':
    unittest.main()
