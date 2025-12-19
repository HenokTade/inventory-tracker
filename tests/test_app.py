"""
Unit tests for Inventory Tracker Application
"""
import unittest
import json
import os
import sys

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app, load_items, save_items

class TestInventoryTracker(unittest.TestCase):
    
    def setUp(self):
        """Set up test client and test data"""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'test_secret_key'
        self.client = self.app.test_client()
        
        # Create test data file
        self.test_data_file = 'test_items.json'
        app.config['DATA_FILE'] = self.test_data_file
        
    def tearDown(self):
        """Clean up test data"""
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
    
    def test_index_redirect(self):
        """Test that index redirects to login"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)
    
    def test_login_page_loads(self):
        """Test that login page loads successfully"""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
    
    def test_valid_login(self):
        """Test login with valid credentials"""
        response = self.client.post('/login', data={
            'username': 'admin',
            'password': 'admin'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_login(self):
        """Test login with invalid credentials"""
        response = self.client.post('/login', data={
            'username': 'wrong',
            'password': 'wrong'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Credentials', response.data)
    
    def test_dashboard_requires_login(self):
        """Test that dashboard requires authentication"""
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)
    
    def test_load_items_empty(self):
        """Test loading items from empty file"""
        items = load_items()
        self.assertEqual(items, [])
    
    def test_save_and_load_items(self):
        """Test saving and loading items"""
        test_items = [
            {'id': 1, 'name': 'Test Item', 'quantity': '10'}
        ]
        save_items(test_items)
        loaded_items = load_items()
        self.assertEqual(loaded_items, test_items)
    
    def test_logout(self):
        """Test logout functionality"""
        # Login first
        with self.client as c:
            c.post('/login', data={
                'username': 'admin',
                'password': 'admin'
            })
            # Then logout
            response = c.get('/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
