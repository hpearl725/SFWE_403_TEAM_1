import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes

import secrets
import string


# Function to generate a random password
# This function generate_password is part of this module.
def generate_password(length):
    """
    This function generates a random password.

    :param length: The length of the password.
    :type length: int
    :return: The generated password.
    :rtype: str
    """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


# Function to handle the submit button click event
# This function submit_user is part of this module.
def submit_user(user_entry,window):
    """
    This function handles the submit button click event.

    It gets the values from the entry widgets, generates a random password,
    appends the values to the CSV file, shows a success message, and destroys the window.
    """
    # Get the values from the entry widgets
    row =  [get_max_id()+1] + [x[1].get() for x in user_entry] +  [0,'True', 'False']
    # Generate a random password
    password = generate_password(10)
    row.insert(2, password)
    # Append the values to the CSV file with a newline character
    with open(os.path.join("GUI","users.csv"), "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    # Show a success message and destroy the window
    messagebox.showinfo("Success", f"New user added successfully. The temporary password is {password}")

    # Destroy the window
    window.destroy()


def create_new_user_window():
    # Create the new user window
    new_user_window = tk.Tk()
    new_user_window.title("New User")

    # Configure the window to make it non-resizable
    new_user_window.geometry("400x400")  # Increased height to accommodate additional fields
    new_user_window.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(new_user_window)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the content
    frame = ttk.Frame(new_user_window)
    frame.pack(expand=True, fill="both")

    # Create labels and entry widgets for additional fields
    # need to get maxid from users.csv
    fields = [
        ("Username:", ttk.Entry(frame)),
        ("First Name:", ttk.Entry(frame)),
        ("Last Name:", ttk.Entry(frame)),
        ("Date of Birth:", ttk.Entry(frame)),
        ("Phone Number:", ttk.Entry(frame)),
        ("Email Address:", ttk.Entry(frame)),
        ("Role:", ttk.Combobox(frame, width=18, 
                               values=("manager","pharmacist","technician","cashier"), 
                               state="readonly"))
    ]

    # Create a submit button
    submit_button = ttk.Button(frame, text="Submit", command=lambda: submit_user(fields, new_user_window))

    # Use grid layout to arrange the widgets
    for i, (label_text, entry_widget) in enumerate(fields):
        label = ttk.Label(frame, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry_widget.grid(row=i, column=1, padx=10, pady=5, columnspan=2, sticky="w")

    submit_button.grid(row=len(fields), column=0, columnspan=3, padx=10, pady=10)

    # Center the entry widgets in the window
    for i in range(len(fields) + 1):
        frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Start the Tkinter main loop for the new user window
    new_user_window.mainloop()

def get_max_id():
    try:
        with open(os.path.join("GUI","users.csv"), 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Skip the header row if it exists
            next(reader, None)
            # Count the number of entries in the CSV file
            num_entries = sum(1 for row in reader)
            return num_entries
    except FileNotFoundError:
        print("The 'users.csv' file does not exist.")
        return 0
    except Exception as e:
        print("An error occurred:", str(e))
        return 0