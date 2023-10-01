from tkinter import ttk

from inventory import FIELDNAMES, read_inventory, write_inventory

# Function to create the Inventory table
def create_inventory_table(frame):
    # Create a Treeview widget for the Inventory table (hidden initially)
    inventory_tree = ttk.Treeview(frame, columns=FIELDNAMES, show="headings")

    # set inventory column widths so that all columns will fit in the frame
    # also define the column headings for the table from fieldnames
    for name in FIELDNAMES:
        inventory_tree.column(name, width=100)
        inventory_tree.heading(name, text=name)
    
    # read inventory from csv and store as dictionary
    inventory_dictionary = read_inventory("inventory.csv")

    # insert each product's information into table
    for product in inventory_dictionary.values():
        inventory_tree.insert("", "end", values = tuple(product.values()))

    return inventory_tree

# Function to show the Inventory table
def show_inventory_table(inventory_tree):
    inventory_tree.pack()

# Function to hide the Inventory table
def hide_inventory_table(inventory_tree):
    inventory_tree.pack_forget()