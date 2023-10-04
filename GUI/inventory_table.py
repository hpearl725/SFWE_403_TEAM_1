import os
import tkinter as tk
from tkinter import ttk
import csv

from GUI.inventory import read_inventory
# Uncomment these when building sphinx
# from inventory import read_inventory


def create_inventory_table(frame):
    """
    This function creates an inventory table using a Treeview widget.

    :param frame: The parent frame to which the inventory table will be added.
    :type frame: tk.Frame
    :return: The created inventory table.
    :rtype: ttk.Treeview
    """
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


def show_inventory_table(inventory_tree):
    """
    This function populates the inventory table with data from a CSV file.

    :param inventory_tree: The inventory table to be populated.
    :type inventory_tree: ttk.Treeview
    """
    inventory_tree.delete(*inventory_tree.get_children())  # Clear existing rows

    inventory_path = os.path.join('GUI', 'inventory.csv')
    inventory_dict = read_inventory(inventory_path)

    for row in inventory_dict.values():
        name = row["product_name"]
        quantity = row["in_stock"]
        price = row["price"]
        inventory_tree.insert("", tk.END, values=(name, quantity, price))

    inventory_tree.pack()


def hide_inventory_table(inventory_tree):
    """
    This function hides the inventory table.

    :param inventory_tree: The inventory table to be hidden.
    :type inventory_tree: ttk.Treeview
    """
    inventory_tree.pack_forget()
