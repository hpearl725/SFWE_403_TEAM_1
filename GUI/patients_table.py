from tkinter import ttk, Tk, Button
from GUI.Create_patients import PatientForm

# Declare the Add Patient button as a global variable
add_patient_button = None

# Function to create the Patients table
def create_patients_table(frame):
    patients_tree = ttk.Treeview(frame, columns=("Name", "Phone"), show="headings")
    patients_tree.heading("Name", text="Name")
    patients_tree.heading("Phone", text="Phone")
    
    patients_tree.insert("", "end", values=("John Doe", "123-456-7890"))
    patients_tree.insert("", "end", values=("Jane Smith", "987-654-3210"))
    patients_tree.insert("", "end", values=("Alice Johnson", "555-123-4567"))
    patients_tree.insert("", "end", values=("Bob Brown", "777-888-9999"))
    patients_tree.insert("", "end", values=("Eve Wilson", "555-555-5555"))

    return patients_tree


# Function to show the Patients table and a button beneath it
def show_patients_table(patients_tree):
    patients_tree.pack()
    

def add_patient():
    patient_form = PatientForm()
    patient_form.save_patient_info()


# Function to hide the Patients table and the button
def hide_patients_table(patients_tree, button=None):
    patients_tree.pack_forget()
    if button is not None:
        button.pack_forget()
