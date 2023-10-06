import os
import tkinter as tk
from tkinter import ttk
import csv
from GUI.prescriptions import read_prescriptions


def create_prescriptions_table(frame):
    prescriptions_tree = ttk.Treeview(frame)
    prescriptions_tree["columns"] = ("name", "quantity", "price")

    prescriptions_tree.column("#0", width=0, stretch=tk.NO)
    prescriptions_tree.column("name", anchor=tk.W, width=200)
    prescriptions_tree.column("quantity", anchor=tk.CENTER, width=100)
    prescriptions_tree.column("price", anchor=tk.E, width=100)

    prescriptions_tree.heading("#0", text="", anchor=tk.W)
    prescriptions_tree.heading("name", text="Name", anchor=tk.W)
    prescriptions_tree.heading("quantity", text="Quantity", anchor=tk.CENTER)
    prescriptions_tree.heading("price", text="Price", anchor=tk.E)

    return prescriptions_tree


def show_prescriptions_table(prescriptions_tree):
    prescriptions_tree.delete(*prescriptions_tree.get_children())  # Clear existing rows

    prescriptions_path = os.path.join('GUI', 'prescriptions.csv')
    prescriptions_dict = read_prescriptions(prescriptions_path)

    patients_path = os.path.join('GUI', 'patients.csv')
    patients_dict = read_patients(patients_path)

    for patient in patients_dict.values():
        patient_name = patient["name"]
        patient_node = prescriptions_tree.insert("", tk.END, text=patient_name)

        for row in prescriptions_dict.values():
            if row["patient_name"] == patient_name:
                name = row["product_name"]
                quantity = row["in_stock"]
                price = row["price"]
                prescriptions_tree.insert(patient_node, tk.END, values=(name, quantity, price))

    prescriptions_tree.pack()


def hide_prescriptions_table(prescriptions_tree):
    prescriptions_tree.pack_forget()
