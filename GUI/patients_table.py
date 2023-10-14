from tkinter import ttk, Tk, Button
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
    patient_form = PatientForm()
    patient_form.window.mainloop()