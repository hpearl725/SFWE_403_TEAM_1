import os
import tkinter as tk
from tkinter import ttk
import csv
from tkinter import messagebox
from GUI.prescriptions import read_prescriptions
from GUI.inventory import read_inventory, write_inventory
from logs.log import logger, event, events, log_obj
from GUI.signature_pad import SignaturePad

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

def add_prescription(current_user):
    prescription_form = PrescriptionForm(current_user)
    prescription_form.window.mainloop()


from reportlab.pdfgen import canvas
from datetime import datetime

def create_blank_pdf(patient_name, date, medicine_name, quantity, price_per_unit, total_price):
    filename = f"{patient_name}_{date}.pdf"
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 18)
    c.drawString(100, 750, f"Patient Name: {patient_name}")
    c.drawString(100, 725, f"Date: {date}")
    c.drawString(100, 700, f"Medicine Name: {medicine_name}")
    c.drawString(100, 675, f"Quantity: {quantity}")
    c.drawString(100, 650, f"Price per unit: ${price_per_unit}")
    c.drawString(100, 625, f"Total Price: ${total_price}")
    c.showPage()
    c.save()

def fill_prescription(current_user, name, medicine_name):
    prescriptions_path = os.path.join('GUI', 'prescriptions.csv')
    prescriptions_list = read_prescriptions(prescriptions_path)

    prescription = next((row for row in prescriptions_list if row["patient_name"] == name and row["product_name"] == medicine_name), None)
    if prescription is None:
        messagebox.showerror("Error", "Prescription not found.")
        return

    inventory_path = os.path.join('GUI', 'inventory.csv')
    inventory_dict = read_inventory(inventory_path)
    
    # Check if the medicine exists in inventory
    if medicine_name not in inventory_dict:
        messagebox.showerror("Warning", "Medicine not found in inventory.")
        return
    
    # Check if the medicine is expired
    if medicine_name in inventory_dict and inventory_dict[medicine_name]["is_expired"] == "TRUE":
        messagebox.showerror("Warning", "The medicine is expired.")
        return

    # Check if there is enough inventory
    if int(inventory_dict[medicine_name]["in_stock"]) < int(prescription["qty"]):
        messagebox.showerror("Warning", "Not enough inventory.")
        return

    signature_window = tk.Toplevel()
    signature_pad = SignaturePad(signature_window)
    confirm_button = tk.Button(signature_window, text="Confirm", command=signature_pad.save_and_close)
    confirm_button.pack()

    prescriptions_list.remove(prescription)

    with open(prescriptions_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["product_name", "qty", "patient_name", "rx_number"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in prescriptions_list:
            writer.writerow(row)

    # Update the inventory and create a log entry
    if medicine_name in inventory_dict:
        inventory_dict[medicine_name]["in_stock"] = str(int(inventory_dict[medicine_name]["in_stock"]) - int(prescription["qty"]))
        write_inventory(inventory_path, inventory_dict)
        
        # Log the login event
        log = logger(os.path.join("GUI","log.csv"))
        price = inventory_dict[medicine_name]["price"]
        qty = prescription["qty"]
        patient_name = prescription["patient_name"]
        rx_number = prescription["rx_number"]
        fill_rx_event = event("user_action", events.fill_rx.name, f"{qty}x {medicine_name} filled at ${price} for {patient_name}, RX#: {rx_number}")
        log.log(log_obj(fill_rx_event, current_user.username))

        # Calculate total price
        price_per_unit = float(inventory_dict[medicine_name]["price"])
        total_price = price_per_unit * int(prescription["qty"])
        # Generate a receipt
        date = datetime.now().strftime("%Y-%m-%d")
        create_blank_pdf(name, date, medicine_name, prescription["qty"], price_per_unit, total_price)
    
def create_fill_prescription_window(current_user):
    window = tk.Toplevel()

    # Create a frame to hold the content
    frame = ttk.Frame(window)
    frame.pack(expand=True, fill="both")
    window.title("Fill Prescription")

    name_label = ttk.Label(frame, text="Name:")
    name_label.pack(side="left", padx=(10, 0))
    name_entry = ttk.Entry(frame)
    name_entry.pack(side="left", padx=(0, 10))

    medicine_label = ttk.Label(frame, text="Medicine Name:")
    medicine_label.pack(side="left", padx=(10, 0))
    medicine_entry = ttk.Entry(frame)
    medicine_entry.pack(side="left", padx=(0, 10))

    ok_button = ttk.Button(window, text="OK", command=lambda: 
                           [fill_prescription(current_user, name_entry.get(), medicine_entry.get()), window.destroy()])
    ok_button.pack(side="left", padx=(10, 0))
