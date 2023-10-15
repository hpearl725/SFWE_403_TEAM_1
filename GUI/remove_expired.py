import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes
from GUI.inventory import read_inventory,write_inventory
from logs.log import logger, event, events, log_obj

# Function to handle the search button click event
def remove_expired(this_entry,window,ttk_tree):
    # Get the product name from the entry widget
    product_name = this_entry.get()

    # define result variable
    result = None

    # search the contents of the existing inventory tree
    for child in ttk_tree.get_children():
        # if name matches, display expiration status
        if ttk_tree.item(child)["values"][0]==product_name:
            result = ttk_tree.item(child)["values"][2]
            key = child


    if result is None: # no match in inventory tree
        messagebox.showinfo("Product not found", f"Could not find {product_name} in inventory.")
    elif result == "FALSE":
        messagebox.showerror("Product not expired", f"Product {product_name} has not expired.")
    else: # match found, remove it from inventory
        inventory_path = os.path.join('GUI', 'inventory.csv')
        inventory_dict = read_inventory(inventory_path) # read csv
        del inventory_dict[product_name] # drop product
        ttk_tree.delete(key)
        write_inventory(inventory_path, inventory_dict) # write result to csv
        messagebox.showinfo("Product removed", f"Expired product {product_name} successfully removed.")
        
        # Log the removal event
        log = logger(os.path.join("GUI","log.csv"))
        this_event = event("user_action", events.remove_meds.name, f"User removed expired medicine {product_name}")
        log.log(log_obj(this_event, "placeholder username"))

    # Destroy the check inventory window
    window.destroy()


def create_remove_expired_window(inventory_tree):
    # Create the new user window
    entry_window = tk.Tk()
    entry_window.title("Remove expired product")

    # Configure the window to make it non-resizable
    entry_window.geometry("400x200")
    entry_window.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(entry_window)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the content
    frame = ttk.Frame(entry_window)
    frame.pack(expand=True, fill="both")

    # Create a label and entry widgets for username and password
    product_name_label = ttk.Label(frame, text="Name of expired product to remove:")
    product_name_entry = ttk.Entry(frame)

    # Create a submit button
    submit_button = ttk.Button(frame, text="remove from inventory", 
                               command=lambda: remove_expired(product_name_entry,entry_window,inventory_tree))

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