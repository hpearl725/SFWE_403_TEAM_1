import tkinter as tk
from tkinter import ttk
import csv
from GUI.inventory import read_inventory

# This function create_inventory_table is part of this module.
def create_inventory_table(frame):
    inventory_tree = ttk.Treeview(frame)
    inventory_tree["columns"] = ("name", "quantity", "price")

    inventory_tree.column("#0", width=0, stretch=tk.NO)
    inventory_tree.column("name", anchor=tk.W, width=200)
    inventory_tree.column("quantity", anchor=tk.CENTER, width=100)
    inventory_tree.column("price", anchor=tk.E, width=100)

    inventory_tree.heading("#0", text="", anchor=tk.W)
    inventory_tree.heading("name", text="Name", anchor=tk.W)
    inventory_tree.heading("quantity", text="Quantity", anchor=tk.CENTER)
    inventory_tree.heading("price", text="Price", anchor=tk.E)

    return inventory_tree

# This function show_inventory_table is part of this module.
def show_inventory_table(inventory_tree):
    inventory_tree.delete(*inventory_tree.get_children())  # Clear existing rows

    inventory_dict = read_inventory("GUI/inventory.csv")

    for row in inventory_dict.values():
        name = row["product_name"]
        quantity = row["in_stock"]
        price = row["price"]
        inventory_tree.insert("", tk.END, values=(name, quantity, price))

    inventory_tree.pack()

# This function hide_inventory_table is part of this module.
def hide_inventory_table(inventory_tree):
    inventory_tree.pack_forget()
