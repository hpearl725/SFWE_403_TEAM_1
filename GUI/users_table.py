from tkinter import ttk


# Function to create the Users table
def create_users_table(frame):
    # Create a Treeview widget for the Users table (hidden initially)
    users_tree = ttk.Treeview(frame, columns=("Username", "Role"), show="headings")

    # Define column headings for Users
    users_tree.heading("Username", text="Username")
    users_tree.heading("Role", text="Role")
    return users_tree


# Function to show the Users table
def show_users_table(users_tree):
    # Insert example data into the Users table (hidden initially)
    users_tree.insert("", "end", values=("user1", "Admin"))
    users_tree.insert("", "end", values=("user2", "User"))
    users_tree.insert("", "end", values=("user3", "User"))
    users_tree.pack()


# Function to hide the Users table
def hide_users_table(users_tree):
    users_tree.pack_forget()
