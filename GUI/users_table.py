import csv
import os
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
    # Clear existing rows
    users_tree.delete(*users_tree.get_children())

    # Load and insert user data from CSV file
    file_path = os.path.join("GUI", "users.csv")

    # Check if the CSV file exists, if it does, read and insert user data into the treeview
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users_tree.insert("", "end", values=(row["username"], row["role"]))
    else:
        pass # placeholder for error message
    users_tree.pack()


# Function to hide the Users table
def hide_users_table(users_tree):
    users_tree.pack_forget()
