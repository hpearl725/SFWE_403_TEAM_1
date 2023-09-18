import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# Declare the Treeview widgets as global variables
inventory_tree = None
patients_tree = None
users_tree = None

# Function to create the dashboard window with the Inventory table
def create_dashboard():
    global inventory_tree, patients_tree, users_tree  # Access the global tree variables
    # Create the dashboard window
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    # Create a ThemedStyle instance for modern themes
    style = ThemedStyle(dashboard)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the buttons and table
    frame = ttk.Frame(dashboard)
    frame.pack(padx=20, pady=20)

    # Create buttons for Inventory, Patients, Users, and Settings
    inventory_button = ttk.Button(frame, text="Inventory", command=show_inventory_table)
    patients_button = ttk.Button(frame, text="Patients", command=show_patients_table)
    users_button = ttk.Button(frame, text="Users", command=show_users_table)
    settings_button = ttk.Button(frame, text="Settings")

    # Pack buttons in a row
    inventory_button.pack(side="left", padx=10)
    patients_button.pack(side="left", padx=10)
    users_button.pack(side="left", padx=10)
    settings_button.pack(side="left", padx=10)

    # Create a Treeview widget for the Inventory table (hidden initially)
    inventory_tree = ttk.Treeview(frame, columns=("Item", "Qty"), show="headings")

    # Define column headings for Inventory
    inventory_tree.heading("Item", text="Item")
    inventory_tree.heading("Qty", text="Qty")

    # Insert data into the Inventory table (hidden initially)
    inventory_tree.insert("", "end", values=("Medicine 1", "2"))
    inventory_tree.insert("", "end", values=("Medicine 2", "2"))

    # Create a Treeview widget for the Patients table (hidden initially)
    patients_tree = ttk.Treeview(frame, columns=("Name", "Phone"), show="headings")

    # Define column headings for Patients
    patients_tree.heading("Name", text="Name")
    patients_tree.heading("Phone", text="Phone")

    # Insert example data into the Patients table (hidden initially)
    patients_tree.insert("", "end", values=("John Doe", "123-456-7890"))
    patients_tree.insert("", "end", values=("Jane Smith", "987-654-3210"))
    patients_tree.insert("", "end", values=("Alice Johnson", "555-123-4567"))
    patients_tree.insert("", "end", values=("Bob Brown", "777-888-9999"))
    patients_tree.insert("", "end", values=("Eve Wilson", "555-555-5555"))

    # Create a Treeview widget for the Users table (hidden initially)
    users_tree = ttk.Treeview(frame, columns=("Username", "Role"), show="headings")

    # Define column headings for Users
    users_tree.heading("Username", text="Username")
    users_tree.heading("Role", text="Role")

    # Insert example data into the Users table (hidden initially)
    users_tree.insert("", "end", values=("user1", "Admin"))
    users_tree.insert("", "end", values=("user2", "User"))
    users_tree.insert("", "end", values=("user3", "User"))

    # Start the Tkinter main loop for the dashboard
    dashboard.mainloop()

# Function to show the Inventory table
def show_inventory_table():
    inventory_tree.pack()
    patients_tree.pack_forget()  # Hide the Patients table
    users_tree.pack_forget()  # Hide the Users table

# Function to show the Patients table
def show_patients_table():
    patients_tree.pack()
    inventory_tree.pack_forget()  # Hide the Inventory table
    users_tree.pack_forget()  # Hide the Users table

# Function to show the Users table
def show_users_table():
    users_tree.pack()
    inventory_tree.pack_forget()  # Hide the Inventory table
    patients_tree.pack_forget()  # Hide the Patients table

if __name__ == "__main__":
    create_dashboard()
