import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, scrolledtext
from GUI.inventory import read_inventory, get_near_expiry_medicines, write_inventory,get_low_inventory_items
import datetime
from logs.log import logger, event, events, log_obj
import re  # For input validation with regular expression matching


def create_inventory_table(frame):
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

    return inventory_tree


def show_inventory_table(inventory_tree):
    inventory_tree.delete(*inventory_tree.get_children()
                          )  # Clear existing rows

    inventory_path = os.path.join('GUI', 'inventory.csv')
    inventory_dict = read_inventory(inventory_path)

    for row in inventory_dict.values():
        name = row["product_name"]
        quantity = row["in_stock"]
        expired = row["is_expired"]
        price = row["price"]
        inventory_tree.insert("", tk.END, values=(name, quantity, expired, price))

    inventory_tree.pack()


def hide_inventory_table(inventory_tree):
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

def low_inventory_popup():

    low_inventory_items = get_low_inventory_items()

    if not low_inventory_items:
        return
    else:
        messagebox.showwarning("Low inventory","\n".join([f"Low Inventory Item: {item['product_name']}" for item in low_inventory_items]))


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


def add_new_medicine_popup(current_user):
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

    def update_inventory(current_user):
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
        log = logger(os.path.join("GUI","log.csv"))
        login_event = event("user_action", events.add_meds.name, f"User added {new_quantity}x {new_medicine} priced at ${new_price} to inventory with expiry date {new_expiry_date}")
        log.log(log_obj(login_event, current_user.username))
        new_medicine_popup.destroy()

    add_medicine_button = ttk.Button(frame, text="Confirm", command = lambda:update_inventory(current_user))
    add_medicine_button.pack(pady=10)

def validate_date_format(date_str):
    # Regular expression for matching DD/MM/YYYY format
    if not re.match(r'\d{1,2}/\d{1,2}/\d{4}', date_str):
        return False
    return True

def check_and_generate_report():
    start_date = starting_entry.get()
    end_date = ending_entry.get()

    # Validate dates
    if not validate_date_format(start_date) or not validate_date_format(end_date):
        messagebox.showerror("Invalid Date", "Please enter dates in DD/MM/YYYY format.")
        return

    # If dates are valid, generate the report
    messagebox.showinfo("Inventory Report Generated!",
                        f"The inventory report for the time period: {start_date} to {end_date} has been generated.\n")

def inventory_report_popup():
    # Create the window
    inventory_report_popup = tk.Toplevel()
    inventory_report_popup.title("Inventory Report Period")

    # Configure the window to make it non-resizable
    inventory_report_popup.geometry("400x180")
    inventory_report_popup.resizable(False, False)

    # Create a frame to hold the content
    frame = ttk.Frame(inventory_report_popup)
    frame.pack(expand=True, fill="both")

    # Update labels to indicate the expected date format
    starting_label = ttk.Label(frame, text="Start date (DD/MM/YYYY):")
    starting_label.pack(pady=10)
    global starting_entry
    starting_entry = ttk.Entry(frame)
    starting_entry.pack(pady=5)

    ending_label = ttk.Label(frame, text="End date (DD/MM/YYYY):")
    ending_label.pack(pady=5)
    global ending_entry
    ending_entry = ttk.Entry(frame)
    ending_entry.pack(pady=5)

    generate_inventory_report_button = ttk.Button(
        frame, text="Generate Report", command=check_and_generate_report)
    generate_inventory_report_button.pack(pady=5)