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

    @patch('GUI.dashboard.show_inventory_table')
    @patch('GUI.dashboard.hide_patients_table')
    @patch('GUI.dashboard.hide_users_table')
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

    @patch('GUI.dashboard.hide_inventory_table')
    @patch('GUI.dashboard.show_patients_table')
    @patch('GUI.dashboard.hide_users_table')
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

    @patch('GUI.dashboard.hide_inventory_table')
    @patch('GUI.dashboard.hide_patients_table')
    @patch('GUI.dashboard.show_users_table')
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

    @patch('GUI.dashboard.hide_inventory_table')
    @patch('GUI.dashboard.hide_patients_table')
    @patch('GUI.dashboard.hide_users_table')
    @patch('GUI.dashboard.show_add_user_button')
    def test_show_user_button(self, mock_show_add_user_button, mock_hide_users_table, mock_hide_patients_table, mock_hide_inventory_table):
        """
        Test the show_user_button function.
        """
        # Call the function
        dashboard.show_user_button("manager")

        # Check that the appropriate functions were called
        mock_hide_inventory_table.assert_called_once()
        mock_hide_patients_table.assert_called_once()
        mock_hide_users_table.assert_called_once()
        mock_show_add_user_button.assert_called_once()

    @patch('GUI.dashboard.add_user_button')
    def test_hide_add_user_button(self, mock_add_user_button):
        """
        Test the hide_add_user_button function.
        """
        # Set the add_user_button to a MagicMock
        dashboard.add_user_button = mock_add_user_button

        # Call the function
        dashboard.hide_add_user_button()

        # Check that pack_forget was called on the add_user_button
        mock_add_user_button.pack_forget.assert_called_once()

    @patch('GUI.dashboard.add_user_button')
    def test_show_add_user_button(self, mock_add_user_button):
        """
        Test the show_add_user_button function.
        """
        # Set the add_user_button to None
        dashboard.add_user_button = None

        # Call the function
        dashboard.show_add_user_button("manager")

        # Check that a new add_user_button was created and packed
        mock_add_user_button.assert_called_once_with(dashboard.frame, text="Add User", command=dashboard.open_new_user_window("manager"))
        mock_add_user_button.pack.assert_called_once_with(side="top", pady=10)

        # Ensure that the add_user_button is called
        dashboard.add_user_button.assert_called_once()


if __name__ == '__main__':
    unittest.main()
