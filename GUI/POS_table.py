import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Global variables to keep track of the POS system state
total_amount = 0.00
product_entry = None
quantity_entry = None
price_entry = None
POS_tree = None
total_amount_label = None

def create_POS_table(frame):
    # Initialize Treeview with the correct column names
    pos_tree = ttk.Treeview(frame, columns=("Product", "Quantity", "Price"))

    # Configure the columns
    pos_tree.column("#0", width=0, stretch=tk.NO)  # This is the invisible first column
    pos_tree.column("Product", anchor=tk.W, width=120)
    pos_tree.column("Quantity", anchor=tk.CENTER, width=80)
    pos_tree.column("Price", anchor=tk.CENTER, width=80)

    # Configure the column headings
    pos_tree.heading("#0", text="", anchor=tk.W)
    pos_tree.heading("Product", text="Product", anchor=tk.W)
    pos_tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
    pos_tree.heading("Price", text="Price", anchor=tk.CENTER)

    return pos_tree


def show_pos_table(parent):
    pos_tree = create_POS_table(parent)
    pos_tree.pack(pady=10, fill="both", expand=True)

    # Create a container for the POS entry fields and buttons
    pos_container = ttk.Frame(parent)
    pos_container.pack(padx=10, pady=10, fill='x', expand=True)

    # Product Label and Entry
    product_label = ttk.Label(pos_container, text="Product:")
    product_label.pack(side="left", padx=5)
    product_entry = ttk.Entry(pos_container)
    product_entry.pack(side="left", fill="x", expand=True, padx=5)

    # Quantity Label and Entry
    quantity_label = ttk.Label(pos_container, text="Quantity:")
    quantity_label.pack(side="left", padx=5)
    quantity_entry = ttk.Entry(pos_container)
    quantity_entry.pack(side="left", fill="x", expand=True, padx=5)

    # Price Label and Entry
    price_label = ttk.Label(pos_container, text="Price:")
    price_label.pack(side="left", padx=5)
    price_entry = ttk.Entry(pos_container)
    price_entry.pack(side="left", fill="x", expand=True, padx=5)

    # Add Product Button
    add_product_button = ttk.Button(pos_container, text="Add Product", command=lambda: add_product(product_entry, quantity_entry, price_entry, pos_tree, total_amount_label))
    add_product_button.pack(side="left", padx=5)

    # Process Sale Button and Total Amount Label
    process_sale_button = ttk.Button(parent, text="Process Sale", command=lambda: process_sale(pos_tree, total_amount_label))
    process_sale_button.pack(pady=5)

    total_amount_label = ttk.Label(parent, text=f"Total Amount: ${total_amount:.2f}")
    total_amount_label.pack(pady=5)


def add_product():
    global total_amount
    try:
        quantity = float(quantity_entry.get())
        price = float(price_entry.get())
        product_name = product_entry.get()
        total_amount += quantity * price

        # Add product details to the list
        POS_tree.insert('', tk.END, values=(product_name, quantity, price))

        # Update total label
        total_amount_label.config(text=f"Total Amount: ${total_amount:.2f}")
    except ValueError:
        messagebox.showerror(title="Invalid Entry", message="Please enter a valid number for the quantity and price.")

    # Clear the entry fields            
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def process_sale():
    global total_amount
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    total_amount = 0.00
    total_amount_label.config(text=f"Total Amount: ${total_amount:.2f}")

def hide_POS_table(pos_tree):
    # global product_entry, quantity_entry, price_entry, total_amount_label
    # product_entry.pack_forget()
    # quantity_entry.pack_forget()
    # price_entry.pack_forget()
    # pos_tree.pack_forget()
    # total_amount_label.pack_forget()
    return None

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
