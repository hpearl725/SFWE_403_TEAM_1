import os
import tkinter as tk
from tkinter import ttk
import csv
from GUI.prescriptions import read_prescriptions

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
    prescriptions_dict = read_prescriptions(prescriptions_path)

    patients_path = os.path.join('patient_info.csv')
    patients_dict = read_patients(patients_path)

    for patient in patients_dict.values():
        patient_name = patient["First Name"] + " " + patient["Last Name"]
        patient_node = prescriptions_tree.insert("", 'end', text=patient_name, open=True)

        for row in prescriptions_dict.values():
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