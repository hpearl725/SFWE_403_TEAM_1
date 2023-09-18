import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

# Declare the Treeview widgets as global variables
inventory_tree = None
patients_tree = None
users_tree = None
frame = None  # Define 'frame' as a global variable

# Function to create the dashboard window with the Inventory table
def create_dashboard():
    global inventory_tree, patients_tree, users_tree, frame  # Access the global variables
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
    settings_button = ttk.Button(button_frame, text="Settings", command=show_hello_world_button)
    exit_button = ttk.Button(frame, text="Exit", command=dashboard.quit)

    # Pack buttons horizontally with padding
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

    # Create an Exit button at the bottom right
    exit_button.pack(side="bottom", anchor="se", padx=10, pady=10)

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

# Function to show "Hello World" button and hide the table
def show_hello_world_button():
    global frame  # Access the global 'frame' variable
    inventory_tree.pack_forget()
    patients_tree.pack_forget()
    users_tree.pack_forget()
    
 # Create a "Hello World" button
    hello_world_button = ttk.Button(frame, text="Hello World")
    hello_world_button.pack(side="top", pady=10)

if __name__ == "__main__":
    create_dashboard()