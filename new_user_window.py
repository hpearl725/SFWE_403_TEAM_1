import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes


# Function to handle the submit button click event
def submit_user():
    # Get the values from the entry widgets
    username = username_entry.get()
    password = password_entry.get()

    # Validate the values
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
    else:
        # Append the values to the CSV file with a newline character
        with open("credentials.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        # Show a success message
        messagebox.showinfo("Success", "New user added successfully")

        # Clear the entry widgets
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


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
password_label = ttk.Label(frame, text="Password:")
password_entry = ttk.Entry(frame, show="*")

# Create a submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_user)

# Use grid layout to arrange the widgets
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky="w")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky="w")
submit_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Center the entry widgets in the window
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Start the Tkinter main loop for the new user window
new_user_window.mainloop()
