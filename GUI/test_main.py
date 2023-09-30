import unittest
from unittest.mock import patch, MagicMock
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        # Mock the username and password Entry widgets
        main.username_entry = MagicMock()
        main.password_entry = MagicMock()

    @patch('main.root.mainloop')
    @patch('main.messagebox.showerror')
    @patch('main.create_dashboard')
    def test_open_dashboard(self, mock_create_dashboard, mock_showerror, mock_mainloop):
        # Set the username and password to an incorrect value
        main.username_entry.get.return_value = 'wrong_username'
        main.password_entry.get.return_value = 'wrong_password'

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was called
        mock_showerror.assert_called_once()

        # Check that create_dashboard was not called
        mock_create_dashboard.assert_not_called()

if __name__ == '__main__':
    unittest.main()
