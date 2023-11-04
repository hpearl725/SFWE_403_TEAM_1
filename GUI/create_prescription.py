import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import csv
import os

class PrescriptionForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Add Prescription")

        self.patient_name_label = ttk.Label(self.window, text="Patient Name:")
        self.patient_name_entry = ttk.Entry(self.window)

        self.product_name_label = ttk.Label(self.window, text="Product Name:")
        self.product_name_entry = ttk.Entry(self.window)

        self.qty_label = ttk.Label(self.window, text="Qty:")
        self.qty_entry = ttk.Entry(self.window)

        self.submit_button = ttk.Button(self.window, text="Submit", command=self.save_prescription_info)

        self.patient_name_label.pack()
        self.patient_name_entry.pack()
        self.product_name_label.pack()
        self.product_name_entry.pack()
        self.qty_label.pack()
        self.qty_entry.pack()
        self.submit_button.pack()

    def save_prescription_info(self):
        patient_name = self.patient_name_entry.get()
        product_name = self.product_name_entry.get()
        qty = self.qty_entry.get()

        with open(os.path.join('GUI', 'prescriptions.csv'), mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] == product_name and row[2] == patient_name:
                    tkinter.messagebox.showerror("Error", "Prescription for this product already exists for this patient.")
                    return

        with open(os.path.join('GUI', 'prescriptions.csv'), mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([product_name, qty, patient_name])

        self.window.destroy()
