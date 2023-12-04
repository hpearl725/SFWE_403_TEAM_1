import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from logs.log import logger, event, events, log_obj

# Function to handle the search button click event
def check_inventory(this_entry,window,ttk_tree):
    # Get the product name from the entry widget
    product_name = this_entry.get()

    # define result variable
    result = None

    # search the contents of the existing inventory tree
    for child in ttk_tree.get_children():
        # if name matches, display amount in inventory
        if ttk_tree.item(child)["values"][0]==product_name:
            # print(ttk_tree.item(child)["values"][1])
            result = ttk_tree.item(child)["values"][1]


    if result is None: # no match in inventory tree
         messagebox.showinfo("Product not found", f"Could not find {product_name} in inventory.")
    else: # match found, display result in popup window
        messagebox.showinfo("Product found", f"The total amount of {product_name} in inventory is {result}.")

    # Destroy the check inventory window
    window.destroy()


def create_check_inventory_window(inventory_tree):
    # Create the new user window
    entry_window = tk.Toplevel()
    entry_window.title("Check inventory")

    # Configure the window to make it non-resizable
    entry_window.geometry("400x200")
    entry_window.resizable(False, False)

    # Create a frame to hold the content
    frame = ttk.Frame(entry_window)
    frame.pack(expand=True, fill="both")

    # Create a label and entry widgets for username and password
    product_name_label = ttk.Label(frame, text="Name of product to search for:")
    product_name_entry = ttk.Entry(frame)

    # Create a submit button
    submit_button = ttk.Button(frame, text="Search inventory", command=lambda: check_inventory(product_name_entry,entry_window,inventory_tree))

    # Use grid layout to arrange the widgets
    product_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    product_name_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
    submit_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Center the entry widgets in the window
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Start the Tkinter main loop for the new user window
    entry_window.mainloop()
    
def edit_inventory(product, quantity, window, current_user):
    inventory_path = os.path.join('GUI', 'inventory.csv')
    with open(inventory_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        lines = list(csv_reader)
    for i in range(0,len(lines)):
        if lines[i][1] == product:
            break
    
    lines[i][2] = quantity
    
    log = logger(os.path.join("GUI","log.csv"))
    this_event = event("user_action", events.edit_inventory.name, f"Manager Edited Inventory")
    log.log(log_obj(this_event, current_user.username))

    with open(inventory_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)
        
    window.destroy()
    
def create_edit_inventory_window(inventory_tree, current_user):
# Create the window
    edit_inventory_popup = tk.Toplevel()
    edit_inventory_popup.title("Edit Inventory")

    # Configure the window to make it non-resizable
    edit_inventory_popup.geometry("400x180")
    edit_inventory_popup.resizable(False, False)

    # Create a frame to hold the content
    frame = ttk.Frame(edit_inventory_popup)
    frame.pack(expand=True, fill="both")

    name_label = ttk.Label(frame, text="Product:")
    name_label.pack(pady=10)
    name_entry = ttk.Entry(frame)
    name_entry.pack(pady=5)

    quantity_label = ttk.Label(frame, text="Quantity:")
    quantity_label.pack(pady=5)
    quantity_entry = ttk.Entry(frame)
    quantity_entry.pack(pady=5)

    save = ttk.Button(
        frame, text="Save", command=lambda: edit_inventory(name_entry.get(), quantity_entry.get(), edit_inventory_popup, current_user))
    save.pack(pady=5)
