from tkinter import ttk


# Function to create the Patients table
# This function create_patients_table is part of this module.
def create_patients_table(frame):
    """
    This function creates a Patients table using a Treeview widget.

    :param frame: The parent frame to which the Patients table will be added.
    :type frame: tk.Frame
    :return: The created Patients table.
    :rtype: ttk.Treeview
    """
    patients_tree = ttk.Treeview(frame, columns=("Name", "Phone"), show="headings")

    patients_tree.heading("Name", text="Name")
    patients_tree.heading("Phone", text="Phone")

    patients_tree.insert("", "end", values=("John Doe", "123-456-7890"))
    patients_tree.insert("", "end", values=("Jane Smith", "987-654-3210"))
    patients_tree.insert("", "end", values=("Alice Johnson", "555-123-4567"))
    patients_tree.insert("", "end", values=("Bob Brown", "777-888-9999"))
    patients_tree.insert("", "end", values=("Eve Wilson", "555-555-5555"))

    return patients_tree


def show_patients_table(patients_tree):
    """
    This function shows the Patients table.

    :param patients_tree: The Patients table to be shown.
    :type patients_tree: ttk.Treeview
    """
    patients_tree.pack()


def hide_patients_table(patients_tree):
    """
    This function hides the Patients table.

    :param patients_tree: The Patients table to be hidden.
    :type patients_tree: ttk.Treeview
    """
    patients_tree.pack_forget()
