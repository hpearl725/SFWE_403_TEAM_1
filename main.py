import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes
from dashboard import create_dashboard


# Function to validate the login credentials and open the dashboard
def open_dashboard():
    username = username_entry.get()
    password = password_entry.get()

    # Global variable to store the role of the current user
    global current_user_role

    # Open the .csv file and search for the username and password
    with open("credentials.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        for i, row in enumerate(rows):
            if row[0] == username and row[1] == password:
                current_user_role = row[3]
                if row[2] == 'True':
                    new_password = simpledialog.askstring("New Password", "Enter new password:", show='*')
                    rows[i] = [username, new_password, False]
                    with open("credentials.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                root.destroy()  # Close the login window
                create_dashboard(current_user_role)  # Open the dashboard window
                return

    messagebox.showerror("Login Failed", "Incorrect username or password")


# Create the main login window
root = tk.Tk()
root.title("Login Page")

# Configure the window to have no border and make it resizable
root.overrideredirect(True)
root.geometry("400x200")
root.resizable(False, False)

# Create a ThemedStyle instance for the modern theme
style = ThemedStyle(root)
style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

# Create a frame to hold the content
frame = ttk.Frame(root)
frame.pack(expand=True, fill="both")

# Create labels and entry widgets for username and password
username_label = ttk.Label(frame, text="Username:")
username_label.pack(pady=10)
username_entry = ttk.Entry(frame)
username_entry.pack(pady=5)

password_label = ttk.Label(frame, text="Password:")
password_label.pack()
password_entry = ttk.Entry(frame, show="*")  # Show asterisks for password
password_entry.pack(pady=10)

# Create the Login button
login_button = ttk.Button(frame, text="Login", command=open_dashboard)
login_button.pack()

# Center the login window on the screen
root.geometry("+%d+%d" % ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2,
                          (root.winfo_screenheight() - root.winfo_reqheight()) / 2))

# Start the Tkinter main loop for the login page
root.mainloop()


def current_user_role():
    return current_user_role
