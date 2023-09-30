import pytest
from unittest.mock import MagicMock
import main

# Mock the username and password Entry widgets
@pytest.fixture
def mock_entries(monkeypatch):
    mock_username_entry = MagicMock()
    mock_password_entry = MagicMock()
    monkeypatch.setattr(main, 'username_entry', mock_username_entry)
    monkeypatch.setattr(main, 'password_entry', mock_password_entry)
    return mock_username_entry, mock_password_entry

def test_open_dashboard(mock_entries):
    mock_username_entry, mock_password_entry = mock_entries

    # Set the username and password to an incorrect value
    mock_username_entry.get.return_value = 'wrong_username'
    mock_password_entry.get.return_value = 'wrong_password'

    with pytest.raises(Exception) as e_info:
        # Call the function
        main.open_dashboard()

    # Check that messagebox.showerror was called
    assert 'Login Failed' in str(e_info.value)

    # Check that create_dashboard was not called
    assert not main.create_dashboard.called
