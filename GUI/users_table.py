import tkinter as tk
from tkinter import ttk


# Function to create the Users table
def create_users_table(frame):
    # Create a Treeview widget for the Users table (hidden initially)
    users_tree = ttk.Treeview(frame, columns=("Username", "Role"), show="headings")

    # Define column headings for Users
    users_tree.heading("Username", text="Username")
    users_tree.heading("Role", text="Role")

    # Insert example data into the Users table (hidden initially)
    users_tree.insert("", "end", values=("user1", "Admin"))
    users_tree.insert("", "end", values=("user2", "User"))
    users_tree.insert("", "end", values=("user3", "User"))

    return users_tree


# Function to show the Users table
def show_users_table(users_tree):
    users_tree.pack()


# Function to hide the Users table
def hide_users_table(users_tree):
    users_tree.pack_forget()


def change_password(current_user_role):
    if current_user_role == "Manager":
        # function to get users name for which to change their password
        print("Change password button pressed")
    else:
       # will need to get user, not just the role
       non_manager_change_password()

def non_manager_change_password():
    # function to change password for current user
    window = tk.Tk()
    window.title("Password Change")

    # Create and configure widgets
    password_label = tk.Label(window, text="Enter your password:")
    password_entry = tk.Entry(window, show="*")
    submit_button = tk.Button(window, text="Submit", command=check_password)

    # Pack widgets
    password_label.pack(pady=10)
    password_entry.pack(pady=5)
    submit_button.pack()

    # Start the main loop
    window.mainloop()