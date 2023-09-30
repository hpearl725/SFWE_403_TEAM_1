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
        main.username_entry.get.return_value = 'a'
        main.password_entry.get.return_value = '2'

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was called
        mock_showerror.assert_called_once()

        # Check that create_dashboard was not called
        mock_create_dashboard.assert_not_called()

    @patch('main.root.mainloop')
    @patch('main.messagebox.showerror')
    @patch('main.create_dashboard')
    def test_open_dashboard_blank_password(self, mock_create_dashboard, mock_showerror, mock_mainloop):
        # Set the username to a correct value and password to blank
        main.username_entry.get.return_value = 'a'
        main.password_entry.get.return_value = ''

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was called
        mock_showerror.assert_called_once()

        # Check that create_dashboard was not called
        mock_create_dashboard.assert_not_called()

    @patch('main.root.mainloop')
    @patch('main.messagebox.showerror')
    @patch('main.create_dashboard')
    def test_open_dashboard_blank_username(self, mock_create_dashboard, mock_showerror, mock_mainloop):
        # Set the username to blank and password to a correct value
        main.username_entry.get.return_value = ''
        main.password_entry.get.return_value = '1'

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was called
        mock_showerror.assert_called_once()

        # Check that create_dashboard was not called
        mock_create_dashboard.assert_not_called()

    @patch('main.root.mainloop')
    @patch('main.messagebox.showerror')
    @patch('main.create_dashboard')
    def test_open_dashboard_blank_username_and_password(self, mock_create_dashboard, mock_showerror, mock_mainloop):
        # Set the username and password to blank
        main.username_entry.get.return_value = ''
        main.password_entry.get.return_value = ''

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was called
        mock_showerror.assert_called_once()

        # Check that create_dashboard was not called
        mock_create_dashboard.assert_not_called()

    @patch('main.root.mainloop')
    @patch('main.messagebox.showerror')
    @patch('main.create_dashboard')
    def test_open_dashboard_correct_credentials(self, mock_create_dashboard, mock_showerror, mock_mainloop):
        # Set the username and password to correct values
        main.username_entry.get.return_value = 'a'
        main.password_entry.get.return_value = '1'

        # Call the function
        main.open_dashboard()

        # Check that messagebox.showerror was not called
        mock_showerror.assert_not_called()

        # Check that create_dashboard was called
        mock_create_dashboard.assert_called_once()

if __name__ == '__main__':
    unittest.main()
