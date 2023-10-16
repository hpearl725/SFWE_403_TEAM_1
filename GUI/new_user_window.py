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
def submit_user(username_entry,window):
    """
    This function handles the submit button click event.

    It gets the values from the entry widgets, generates a random password,
    appends the values to the CSV file, shows a success message, and destroys the window.
    """
    # Get the values from the entry widgets
    username = username_entry.get()

    # Generate a random password
    password = generate_password(10)

    # Append the values to the CSV file with a newline character
    with open(os.path.join("GUI","credentials.csv"), "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, True, "staff"])

    # Show a success message and destroy the window
    messagebox.showinfo("Success", f"New user added successfully. The temporary password is {password}")

    # Destroy the window
    window.destroy()


def create_new_user_window():
    # Create the new user window
    new_user_window = tk.Tk()
    new_user_window.title("New User")

    # Configure the window to have no border and make it resizable
    new_user_window.overrideredirect(True)
    new_user_window.geometry("400x200")
    new_user_window.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(new_user_window)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the content
    frame = ttk.Frame(new_user_window)
    frame.pack(expand=True, fill="both")

    # Create a label and entry widgets for username and password
    username_label = ttk.Label(frame, text="Username:")
    username_entry = ttk.Entry(frame)

    # Create a submit button
    submit_button = ttk.Button(frame, text="Submit", command=lambda: submit_user(username_entry,new_user_window))

    # Use grid layout to arrange the widgets
    username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    username_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
    submit_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Center the entry widgets in the window
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    # Start the Tkinter main loop for the new user window
    new_user_window.mainloop()
