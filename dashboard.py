import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

import inventory_table
import patients_table
import users_table

# Declare the Treeview widgets as global variables
inventory_tree = None
patients_tree = None
users_tree = None
frame = None  # Define 'frame' as a global variable
add_user_button = None  # Define 'add_user_button' as a global variable

# Function to create the dashboard window with the Inventory, Patients, and Users tables
def create_dashboard():
    global inventory_tree, patients_tree, users_tree, frame, add_user_button  # Access the global variables
    # Create the dashboard window
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    # Configure the window to have no border and make it resizable
    dashboard.overrideredirect(True)
    dashboard.geometry("800x600")
    dashboard.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(dashboard)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the content
    frame = ttk.Frame(dashboard)
    frame.pack(expand=True, fill="both")

    # Create a horizontal frame for buttons
    button_frame = ttk.Frame(frame)
    button_frame.pack(side="top", fill="x", padx=10, pady=10)

    # Create buttons for Inventory, Patients, Users, Settings, and Exit
    inventory_button = ttk.Button(button_frame, text="Inventory", command=show_inventory_table)
    patients_button = ttk.Button(button_frame, text="Patients", command=show_patients_table)
    users_button = ttk.Button(button_frame, text="Users", command=show_users_table)
    settings_button = ttk.Button(button_frame, text="Settings", command=show_user_button)
    exit_button = ttk.Button(frame, text="Exit", command=dashboard.quit)

    # Pack buttons horizontally with padding
    inventory_button.pack(side="left", padx=10)
    patients_button.pack(side="left", padx=10)
    users_button.pack(side="left", padx=10)
    settings_button.pack(side="left", padx=10)

    # Call the functions from the separate files to create the trees
    inventory_tree = inventory_table.create_inventory_table(frame)
    patients_tree = patients_table.create_patients_table(frame)
    users_tree = users_table.create_users_table(frame)

    # Create an Exit button at the bottom right
    exit_button.pack(side="bottom", anchor="se", padx=10, pady=10)

    # Start the Tkinter main loop for the dashboard
    dashboard.mainloop()

# Function to show the Inventory table
def show_inventory_table():
    inventory_table.show_inventory_table(inventory_tree)
    patients_table.hide_patients_table(patients_tree)
    users_table.hide_users_table(users_tree)
    hide_add_user_button()

# Function to show the Patients table
def show_patients_table():
    inventory_table.hide_inventory_table(inventory_tree)
    patients_table.show_patients_table(patients_tree)
    users_table.hide_users_table(users_tree)
    hide_add_user_button()

# Function to show the Users table
def show_users_table():
    inventory_table.hide_inventory_table(inventory_tree)
    patients_table.hide_patients_table(patients_tree)
    users_table.show_users_table(users_tree)
    hide_add_user_button()

# Function to show settings buttons and hide the tables
def show_user_button():
    # Hide the table views
    inventory_table.hide_inventory_table(inventory_tree)
    patients_table.hide_patients_table(patients_tree)
    users_table.hide_users_table(users_tree)
    show_add_user_button()

# Function to hide the "Add User" button
def hide_add_user_button():
    global add_user_button
    if add_user_button is not None:
        add_user_button.pack_forget()

# Function to show the "Add User" button
def show_add_user_button():
    global add_user_button
    if add_user_button is None:
        add_user_button = ttk.Button(frame, text="Add User")
    add_user_button.pack(side="top", pady=10)

if __name__ == "__main__":
    create_dashboard()