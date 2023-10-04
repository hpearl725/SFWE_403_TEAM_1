import unittest
from unittest.mock import patch, MagicMock
import GUI.dashboard as dashboard


class TestDashboard(unittest.TestCase):
    """
    This class contains unit tests for the dashboard module.
    """

    def setUp(self):
        # Mock the inventory_tree, patients_tree, users_tree, and frame variables
        dashboard.inventory_tree = MagicMock()
        dashboard.patients_tree = MagicMock()
        dashboard.users_tree = MagicMock()
        dashboard.frame = MagicMock()
        # Mock the show_add_user_button function
        self.mock_show_add_user_button = patch('GUI.dashboard.show_add_user_button', MagicMock()).start()

    @patch('GUI.dashboard.GUI.inventory_table.hide_inventory_table')
    @patch('GUI.dashboard.GUI.patients_table.show_patients_table')
    @patch('GUI.dashboard.GUI.users_table.hide_users_table')
    @patch('GUI.dashboard.hide_add_user_button')
    def test_show_patients_table(self, mock_hide_add_user_button, mock_hide_users_table, mock_show_patients_table, mock_hide_inventory_table):
        """
        Test the show_patients_table function.
        """
        # Call the function
        dashboard.show_patients_table()

        # Check that the appropriate functions were called
        mock_hide_inventory_table.assert_called_once()
        mock_show_patients_table.assert_called_once()
        mock_hide_users_table.assert_called_once()
        mock_hide_add_user_button.assert_called_once()

    @patch('GUI.dashboard.GUI.inventory_table.hide_inventory_table')
    @patch('GUI.dashboard.GUI.patients_table.hide_patients_table')
    @patch('GUI.dashboard.GUI.users_table.show_users_table')
    @patch('GUI.dashboard.hide_add_user_button')
    def test_show_users_table(self, mock_hide_add_user_button, mock_show_users_table, mock_hide_patients_table, mock_hide_inventory_table):
        """
        Test the show_users_table function.
        """
        # Call the function
        dashboard.show_users_table()

        # Check that the appropriate functions were called
        mock_hide_inventory_table.assert_called_once()
        mock_hide_patients_table.assert_called_once()
        mock_show_users_table.assert_called_once()
        mock_hide_add_user_button.assert_called_once()

    @patch('GUI.dashboard.GUI.inventory_table.show_inventory_table')
    @patch('GUI.dashboard.GUI.patients_table.hide_patients_table')
    @patch('GUI.dashboard.GUI.users_table.hide_users_table')
    @patch('GUI.dashboard.hide_add_user_button')
    def test_show_inventory_table(self, mock_hide_add_user_button, mock_hide_users_table, mock_hide_patients_table, mock_show_inventory_table):
        """
        Test the show_inventory_table function.
        """
        # Call the function
        dashboard.show_inventory_table()

        # Check that the appropriate functions were called
        mock_show_inventory_table.assert_called_once()
        mock_hide_patients_table.assert_called_once()
        mock_hide_users_table.assert_called_once()
        mock_hide_add_user_button.assert_called_once()


if __name__ == '__main__':
    unittest.main()
