# using tkiner create a function that can be called which will collect the name, dob, address, phone number, and email
# of a patient and store it in a csv file. 

import tkinter as tk
from tkinter import ttk
import csv
import os

class PatientForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Patient Information Form")

        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=20)

        self.fname_entry = self.create_label_entry(frame, "First Name:", 0)
        self.lname_entry = self.create_label_entry(frame, "Last Name:", 1)
        self.dob_entry = self.create_label_entry(frame, "Date of Birth:", 2)
        self.address_entry = self.create_label_entry(frame, "Address:", 3)
        self.phone_entry = self.create_label_entry(frame, "Phone Number:", 4)
        self.email_entry = self.create_label_entry(frame, "Email:", 5)

        save_button = ttk.Button(frame, text="Save", command=self.save_patient_info)
        save_button.grid(row=6, columnspan=2, pady=10)

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

        # Check if any of the fields are empty
        if not fname or not lname or not dob or not address or not phone or not email:
            #Show an error message
            
            return

        # Create a dictionary to hold the patient information
        patient_info = {
            "First Name": fname,
            "Last Name": lname,  
            "Date of Birth": dob,
            "Address": address,
            "Phone Number": phone,
            "Email": email
        }

        # Define the CSV file path
        folder_name = "GUI"
        csv_file = "patients.csv"
        file_path = os.path.join(folder_name, csv_file)

        # Check if 'GUI' folder exists, if not, create it
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Check if the CSV file exists, and if not, create it with a header row
        if not os.path.exists(file_path):
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=patient_info.keys())
                writer.writeheader()

        # Append the patient information to the CSV file
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=patient_info.keys())
            writer.writerow(patient_info)

        # Clear the entry fields after saving
        self.fname_entry.delete(0, 'end')
        self.lname_entry.delete(0, 'end')
        self.dob_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')

    

        # Provide a success message w/ okay button
        