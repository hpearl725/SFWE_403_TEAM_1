from tkinter import ttk


# Function to create the Patients table
# This function create_patients_table is part of this module.
def create_patients_table(frame):
    # Create a Treeview widget for the Patients table (hidden initially)
    patients_tree = ttk.Treeview(frame, columns=("Name", "Phone"), show="headings")

    # Define column headings for Patients
    patients_tree.heading("Name", text="Name")
    patients_tree.heading("Phone", text="Phone")

    # Insert example data into the Patients table (hidden initially)
    patients_tree.insert("", "end", values=("John Doe", "123-456-7890"))
    patients_tree.insert("", "end", values=("Jane Smith", "987-654-3210"))
    patients_tree.insert("", "end", values=("Alice Johnson", "555-123-4567"))
    patients_tree.insert("", "end", values=("Bob Brown", "777-888-9999"))
    patients_tree.insert("", "end", values=("Eve Wilson", "555-555-5555"))

    return patients_tree


# Function to show the Patients table
# This function show_patients_table is part of this module.
def show_patients_table(patients_tree):
    patients_tree.pack()


# Function to hide the Patients table
# This function hide_patients_table is part of this module.
def hide_patients_table(patients_tree):
    patients_tree.pack_forget()
