import os
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from GUI.prescriptions import read_prescriptions
from GUI.inventory import read_inventory, write_inventory

def read_patients(filename):
    patients_dict = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            patient_name = row["First Name"] + " " + row["Last Name"]
            patients_dict[patient_name] = row
    return patients_dict


def create_prescriptions_table(frame):
    prescriptions_tree = ttk.Treeview(frame)
    prescriptions_tree["columns"] = ("name", "quantity")

    prescriptions_tree.column("#0", width=200, stretch=tk.NO)
    prescriptions_tree.column("name", anchor=tk.W, width=200)
    prescriptions_tree.column("quantity", anchor=tk.CENTER, width=100)

    prescriptions_tree.heading("#0", text="Patient Name", anchor=tk.W)
    prescriptions_tree.heading("name", text="Medicine Name", anchor=tk.W)
    prescriptions_tree.heading("quantity", text="Quantity", anchor=tk.CENTER)

    return prescriptions_tree


def show_prescriptions_table(prescriptions_tree):
    prescriptions_tree.delete(*prescriptions_tree.get_children())  # Clear existing rows

    prescriptions_path = os.path.join('GUI', 'prescriptions.csv')
    prescriptions_list = read_prescriptions(prescriptions_path)

    patients_path = os.path.join('patient_info.csv')
    patients_dict = read_patients(patients_path)

    for patient in patients_dict.values():
        patient_name = patient["First Name"] + " " + patient["Last Name"]
        patient_node = prescriptions_tree.insert("", 'end', text=patient_name, open=True)

        for row in prescriptions_list:
            if row["patient_name"] == patient_name:
                name = row["product_name"]
                quantity = row["qty"]
                prescriptions_tree.insert(patient_node, 'end', values=(name, quantity))

    prescriptions_tree.pack()


def hide_prescriptions_table(prescriptions_tree):
    prescriptions_tree.pack_forget()
from GUI.create_prescription import PrescriptionForm

def add_prescription():
    prescription_form = PrescriptionForm()
    prescription_form.window.mainloop()
def fill_prescription(name, medicine_name):

    prescriptions_path = os.path.join('GUI', 'prescriptions.csv')
    prescriptions_list = read_prescriptions(prescriptions_path)

    prescription = next((row for row in prescriptions_list if row["patient_name"] == name and row["product_name"] == medicine_name), None)
    if prescription is None:
        return

    # Check if the medicine is expired
    inventory_path = os.path.join('GUI', 'inventory.csv')
    inventory_dict = read_inventory(inventory_path)
    if medicine_name in inventory_dict and inventory_dict[medicine_name]["is_expired"] == "TRUE":
        messagebox.showerror("Warning", "The medicine is expired.")
        return

    prescriptions_list.remove(prescription)

    with open(prescriptions_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["product_name", "qty", "patient_name"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in prescriptions_list:
            writer.writerow(row)

    # Update the inventory
    if medicine_name in inventory_dict:
        inventory_dict[medicine_name]["in_stock"] = str(int(inventory_dict[medicine_name]["in_stock"]) - int(prescription["qty"]))
        write_inventory(inventory_path, inventory_dict)

def create_fill_prescription_window():
    window = tk.Toplevel()
    window.title("Fill Prescription")

    name_label = ttk.Label(window, text="Name:")
    name_label.pack(side="left", padx=(10, 0))
    name_entry = ttk.Entry(window)
    name_entry.pack(side="left", padx=(0, 10))

    medicine_label = ttk.Label(window, text="Medicine Name:")
    medicine_label.pack(side="left", padx=(10, 0))
    medicine_entry = ttk.Entry(window)
    medicine_entry.pack(side="left", padx=(0, 10))

    ok_button = ttk.Button(window, text="OK", command=lambda: [fill_prescription(name_entry.get(), medicine_entry.get()), window.destroy()])
    ok_button.pack(side="left", padx=(10, 0))
