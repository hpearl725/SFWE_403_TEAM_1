from tkinter import ttk


# Function to create the Inventory table
def create_inventory_table(frame):
    # Create a Treeview widget for the Inventory table (hidden initially)
    inventory_tree = ttk.Treeview(frame, columns=("Item", "Qty"), show="headings")

    # Define column headings for Inventory
    inventory_tree.heading("Item", text="Item")
    inventory_tree.heading("Qty", text="Qty")

    # Insert data into the Inventory table (hidden initially)
    inventory_tree.insert("", "end", values=("Medicine 1", "2"))
    inventory_tree.insert("", "end", values=("Medicine 2", "2"))

    return inventory_tree


# Function to show the Inventory table
def show_inventory_table(inventory_tree):
    inventory_tree.pack()


# Function to hide the Inventory table
def hide_inventory_table(inventory_tree):
    inventory_tree.pack_forget()
