import os
import tkinter as tk
from tkinter import ttk
import csv
from GUI.inventory import read_inventory, get_near_expiry_medicines
import datetime


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
