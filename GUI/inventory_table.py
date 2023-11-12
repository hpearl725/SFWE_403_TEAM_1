import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from GUI.inventory import read_inventory, get_near_expiry_medicines, write_inventory
import datetime
import csv



def create_inventory_table(frame):
    global inventory_tree
    inventory_tree = ttk.Treeview(frame)
    inventory_tree["columns"] = ("name", "quantity", "expired", "price")

    inventory_tree.column("#0", width=0, stretch=tk.NO)
    inventory_tree.column("name", anchor=tk.W, width=100)
    inventory_tree.column("quantity", anchor=tk.CENTER, width=100)
    inventory_tree.column("expired", anchor=tk.CENTER, width=100)
    inventory_tree.column("price", anchor=tk.E, width=100)

    inventory_tree.heading("#0", text="", anchor=tk.W)
    inventory_tree.heading("name", text="Name", anchor=tk.W)
    inventory_tree.heading("quantity", text="Quantity", anchor=tk.CENTER)
    inventory_tree.heading("expired", text="Expired", anchor=tk.CENTER)
    inventory_tree.heading("price", text="Price", anchor=tk.E)
    
    inventory_tree.tag_bind("row","<Button-2>", lambda event: postPopUpMenu(event))


def postPopUpMenu(event):
    row_id = inventory_tree.identify_row(event.y)
    inventory_tree.selection_set(row_id)
    row_values = inventory_tree.item(row_id)['values']
    popUpMenu = tk.Menu(inventory_tree, tearoff=0,font=("Verdana", 11))
    popUpMenu.add_command(label="Edit/Update", command=lambda: edit_inventory(row_values,row_id))
    popUpMenu.post(event.x_root,event.y_root)

def edit_inventory(data_array, item_index):
    item_index = item_index[1:]
    item_index = int(item_index)
    edit_inventory_window = tk.Toplevel()
    edit_inventory_window.title("Edit/Update Inventory")
    
    frame = ttk.Frame(edit_inventory_window)
    frame.pack(expand=True, fill="both")
    
    entries = []
    for i, value in enumerate(data_array):
        label = tk.Label(frame, text=f"Element {i + 1}:")
        label.grid(row=i, column=0, padx=5, pady=5)

        entry_var = tk.StringVar(value=str(value))
        entry = tk.Entry(frame, textvariable=entry_var)
        entry.grid(row=i, column=1, padx=5, pady=5)

        entries.append(entry_var)
    
    def save_changes():
        # Retrieve the edited values from entry widgets
        edited_values = [entry.get() for entry in entries]
        
        #update the csv with new values
        with open("GUI/inventory.csv", 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            lines = list(csv_reader)

        # Update the specific row with the edited values
        edited_values.insert(0,item_index)
        lines[item_index][0] = edited_values[0]
        lines[item_index][1] = edited_values[1]
        lines[item_index][2] = edited_values[2]
        lines[item_index][5] = edited_values[3]
        lines[item_index][6] = edited_values[4]      

        # Write the updated content back to the CSV file
        with open("GUI/inventory.csv", 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(lines)
            
        show_inventory_table()
        edit_inventory_window.destroy()
        
    save_button = tk.Button(frame, text="Save Changes", command=save_changes)
    save_button.grid(row=len(data_array), column=0, columnspan=2, pady=10)

def show_inventory_table():
    inventory_tree.delete(*inventory_tree.get_children()
                          )  # Clear existing rows

    inventory_path = os.path.join('GUI', 'inventory.csv')
    inventory_dict = read_inventory(inventory_path)

    for row in inventory_dict.values():
        name = row["product_name"]
        quantity = row["in_stock"]
        expired = row["is_expired"]
        price = row["price"]
        inventory_tree.insert("", tk.END, values=(name, quantity, expired, price),tags=("row"))

    inventory_tree.pack()



def hide_inventory_table():
    inventory_tree.pack_forget()

    
def create_near_expiry_table(frame):
    near_expiry_tree = ttk.Treeview(frame)
    near_expiry_tree["columns"] = ("name", "remaining_days")

    near_expiry_tree.column("#0", width=0, stretch=tk.NO)
    near_expiry_tree.column("name", anchor=tk.W, width=100)
    near_expiry_tree.column("remaining_days", anchor=tk.CENTER, width=100)

    near_expiry_tree.heading("#0", text="", anchor=tk.W)
    near_expiry_tree.heading("name", text="Name", anchor=tk.W)
    near_expiry_tree.heading("remaining_days", text="Remaining Days", anchor=tk.CENTER)

    return near_expiry_tree

def show_near_expiry_table(near_expiry_tree):
    near_expiry_tree.delete(*near_expiry_tree.get_children())  # Clear existing rows

    near_expiry_medicines = get_near_expiry_medicines()

    if near_expiry_medicines:  # Only show the table if there are near expiry medicines
        for medicine in near_expiry_medicines:
            name = medicine["product_name"]
            remaining_days = (datetime.datetime.strptime(medicine["date_expires"], "%m/%d/%Y").date() - datetime.date.today()).days
            near_expiry_tree.insert("", tk.END, values=(name, remaining_days))

        near_expiry_tree.pack()


def hide_near_expiry_table(near_expiry_tree):
    if near_expiry_tree is not None:
        near_expiry_tree.pack_forget()
def is_near_expiry():
    near_expiry_medicines = get_near_expiry_medicines()
    return bool(near_expiry_medicines)


def place_order_popup():
    # Create the window
    place_order_popup = tk.Toplevel()
    place_order_popup.title("Order information")

    # Configure the window to make it non-resizable
    place_order_popup.geometry("400x180")
    place_order_popup.resizable(False, False)

    # Create a frame to hold the content
    frame = ttk.Frame(place_order_popup)
    frame.pack(expand=True, fill="both")

    name_label = ttk.Label(frame, text="Name:")
    name_label.pack(pady=10)
    name_entry = ttk.Entry(frame)
    name_entry.pack(pady=5)

    quantity_label = ttk.Label(frame, text="Quantity:")
    quantity_label.pack(pady=5)
    quantity_entry = ttk.Entry(frame)
    quantity_entry.pack(pady=5)

    place_order_button = ttk.Button(
        frame, text="Place Order", command=lambda: messagebox.showinfo(
            "Order confirmation", f"Your order of {quantity_entry.get()} {name_entry.get()} has been placed.\n\n"
            "When the order arrives, use the Receive Inventory button to add the medicine to the pharmacy database."))
    place_order_button.pack(pady=5)


def add_new_medicine_popup():
    new_medicine_popup = tk.Toplevel()
    new_medicine_popup.title("Add New Medicine")

    # Create a frame to hold the content
    frame = ttk.Frame(new_medicine_popup)
    frame.pack(expand=True, fill="both")

    # Configure the window to make it non-resizable
    new_medicine_popup.geometry("200x300")
    new_medicine_popup.resizable(False, False)

    name_label = ttk.Label(frame, text="Name:")
    name_label.pack(pady=10)
    name_entry = ttk.Entry(frame)
    name_entry.pack()

    quantity_label = ttk.Label(frame, text="Quantity:")
    quantity_label.pack(pady=10)
    quantity_entry = ttk.Entry(frame)
    quantity_entry.pack()

    expiry_date_label = ttk.Label(frame, text="Expiry Date: (MM/DD/YYYY)")
    expiry_date_label.pack(pady=10)
    expiry_date_entry = ttk.Entry(frame)
    expiry_date_entry.pack()

    price_label = ttk.Label(frame, text="Price: (USD)")
    price_label.pack(pady=10)
    price_entry = ttk.Entry(frame)
    price_entry.pack()

    def update_inventory():
        inventory_path = os.path.join('GUI', 'inventory.csv')
        inventory_dict = read_inventory(inventory_path)
        new_medicine = name_entry.get()
        new_quantity = int(quantity_entry.get())
        new_expiry_date = expiry_date_entry.get()
        new_price = price_entry.get()

        if new_medicine in inventory_dict:
            inventory_dict[new_medicine]["in_stock"] = str(int(inventory_dict[new_medicine]["in_stock"]) + new_quantity)
        else:
            inventory_dict[new_medicine] = {"product_name" : new_medicine,
                                            "ID_number" : str(len(inventory_dict) + 1),
                                            "in_stock" : str(new_quantity),
                                            "date_added" : datetime.date.today().strftime('%m/%d/%Y'),
                                            "date_expires" : new_expiry_date,
                                            "is_expired" : "FALSE",
                                            "price" : new_price}

        write_inventory(inventory_path, inventory_dict)
        new_medicine_popup.destroy()

    add_medicine_button = ttk.Button(frame, text="Confirm", command = update_inventory)
    add_medicine_button.pack(pady=10)
