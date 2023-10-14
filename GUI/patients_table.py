from tkinter import ttk, Tk, Button, simpledialog, messagebox
import tkinter as tk
from GUI.Create_patients import PatientForm
import os
import csv
# Declare the Add Patient button as a global variable
add_patient_button = None




# Function to create the Patients table
def create_patients_table(frame):
    patients_tree = ttk.Treeview(frame, columns=("Name", "Phone"), show="headings")
    patients_tree.heading("Name", text="Name")
    patients_tree.heading("Phone", text="Phone")
    
    # Load and insert patient data from CSV file
    folder_name = "GUI"
    csv_file = "patients.csv"
    file_path = os.path.join(folder_name, csv_file)

    # Check if the CSV file exists, if it does, read and insert data into the treeview
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = f"{row['First Name']} {row['Last Name']}"
                phone = row["Phone Number"]
                patients_tree.insert("", "end", values=(name, phone))
    
    return patients_tree

def update_patient_data(patients_tree):
    # Clear existing rows
    patients_tree.delete(*patients_tree.get_children())  
    
    folder_name = "GUI"
    csv_file = "patients.csv"
    file_path = os.path.join(folder_name, csv_file)

    # Check if the CSV file exists, if it does, read and insert data into the treeview
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = f"{row['First Name']} {row['Last Name']}"
                phone = row["Phone Number"]
                patients_tree.insert("", "end", values=(name, phone))

# Function to show the Patients table
def show_patients_table(patients_tree):
    update_patient_data(patients_tree)
    patients_tree.pack()
       
# Function to hide the Patients table and the button
def hide_patients_table(patients_tree, button=None):
    patients_tree.pack_forget()
    if button is not None:
        button.pack_forget()

def add_patient():
    patient_form = PatientForm()
    patient_form.window.mainloop()

def update_patient():
    # Get patient name from user
    root = tk.Tk()  # Creating instance of Tk class
    root.withdraw()  # Hide the main window
    patient_name = simpledialog.askstring("Input", "Enter the patient's name:")
    
    if patient_name:  # If a name was entered
        # Fetch patient data from CSV
        with open(os.path.join("GUI","patients.csv"), mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["First Name"] + " " +row["Last Name"] == patient_name:
                    # Found the patient, launch the edit form
                    patient_found_popup(row)
                    return

def patient_found_popup(row):
    popup = tk.Tk()
    popup.title("Edit Patient Information")
    
    label = tk.Label(popup, text="Patient found! Edit information below:")
    label.pack(padx=20, pady=10)

    # Define fields and create labeled entry widgets
    fields = ["First Name", "Last Name", "Date of Birth", "Address", "Phone Number", "Email"]
    entries = {}
    for i, field in enumerate(fields):
        row_frame = ttk.Frame(popup)
        row_frame.pack(fill="x", padx=20, pady=5)
        
        lbl = tk.Label(row_frame, text=f"{field}: ", width=15, anchor="w")
        lbl.pack(side="left")
        
        ent = tk.Entry(row_frame)
        ent.insert(0, row[field])
        ent.pack(fill="x", expand=True)
        
        entries[field] = ent
    
    save_button = tk.Button(popup, text="Save", command=lambda: save_edits(entries, row, popup))
    save_button.pack(pady=10)
    
    popup.mainloop()

def save_edits(entries, original_data, popup):
    # Extracting new data from the entries
    new_data = {field: entry.get() for field, entry in entries.items()}
    
    # File path - adjust as per your requirements
    file_path = os.path.join("GUI", "patients.csv")
    
    # Backup original data and replace with new data
    rows = []
    edited = False

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the row matches the ORIGINAL data (not the edited data)
            if all(row[field] == original_data[field] for field in original_data):
                rows.append(new_data)  # Replace the old data with new data
                edited = True
            else:
                rows.append(row)  # Keep the original data
    
    # Write the modified data back to the CSV file
    if edited:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    else:
        print("No matching row found")
    
    # Close the popup
    popup.destroy()
