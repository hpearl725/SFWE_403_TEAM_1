# using tkiner create a function that can be called which will collect the name, dob, address, phone number, and email
# of a patient and store it in a csv file. 

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

class PatientForm:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Patient Information Form")

        self.fname_label = ttk.Label(self.window, text="First Name:")
        self.fname_entry = ttk.Entry(self.window)

        self.lname_label = ttk.Label(self.window, text="Last Name:")
        self.lname_entry = ttk.Entry(self.window)

        self.dob_label = ttk.Label(self.window, text="Date of Birth:")
        self.dob_entry = ttk.Entry(self.window)

        self.address_label = ttk.Label(self.window, text="Address:")
        self.address_entry = ttk.Entry(self.window)

        self.phone_label = ttk.Label(self.window, text="Phone Number:")
        self.phone_entry = ttk.Entry(self.window)

        self.email_label = ttk.Label(self.window, text="Email:")
        self.email_entry = ttk.Entry(self.window)

        self.save_button = ttk.Button(self.window, text="Save", command=self.save_patient_info)

        self.fname_label.pack()
        self.fname_entry.pack()
        self.lname_label.pack()
        self.lname_entry.pack()
        self.dob_label.pack()
        self.dob_entry.pack()
        self.address_label.pack()
        self.address_entry.pack()
        self.phone_label.pack()
        self.phone_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.save_button.pack()

    def create_label_entry(self, parent, label_text, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky="w")
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, padx=10)
        return entry
    
    def save_patient_info(self):
        # Get the values entered by the user
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        dob = self.dob_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Construct a full name to validate against existing records.
       

        # Validate the entries. (Optional: Add more validation as per requirement.)
        if not (fname and lname and dob and address and phone and email):
            tk.messagebox.showerror("Error", "All fields must be filled.")
            return

        patients_filepath = os.path.join('GUI', 'patients.csv')

        # Check if a patient with the same name already exists.
        try:
            with open(patients_filepath, mode='r', newline='', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    if row and row[0] + " " + row[1] == fname + " " + lname:  # Assuming name is the first column
                        tk.messagebox.showerror("Error", "Patient already exists.")
                        return
        except FileNotFoundError:
            # Handle the case where the file doesn't exist yet.
            pass

        # Add new patient info to the CSV file.
        with open(patients_filepath, mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([fname,lname, dob, address, phone, email])
        # Clear the entry fields after saving
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.dob_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.window.destroy()



    

    

        # Provide a success message w/ okay button
        