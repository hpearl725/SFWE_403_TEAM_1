import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from ttkthemes import ThemedStyle  # Import ThemedStyle from ttkthemes
from GUI.authorization_page import create_authorization_page
from GUI.dashboard import create_dashboard
from GUI.authorization_page import create_authorization_page
from logs.log import logger, event, events, log_obj


def open_dashboard():
    """
    Validate the login credentials and open the dashboard.

    This function retrieves the username and password entered by the user,
    checks them against the credentials stored in a CSV file, and opens the
    dashboard if the credentials are valid. If the "change password" flag is
    set for the user, it prompts the user to enter a new password.

    :return: None
    """
    username = username_entry.get()
    password = password_entry.get()

    # Global variable to store the role of the current user
    global current_user_role

    # Open the .csv file and search for the username and password
    credentials_file_path = os.path.join('GUI', 'credentials.csv')
    with open(credentials_file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        for i, row in enumerate(rows):

            if row[0] == username:
                if row[4] >= 5:
                    raise Exception("Too many failed attempts")
                if row[1] == password:
                    current_user_role = row[3]
                    if row[2] == 'True':
                        new_password = simpledialog.askstring("New Password", "Enter new password:", show='*')

                        rows[i] = [username, new_password, False, current_user_role]
                        with open("credentials.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                    
                    # Close the login window
                    root.destroy()
                    
                    # Open the dashboard window
                    create_dashboard(current_user_role)

                    # Log the login event
                    log = logger("logs\log.csv")
                    login_event = event("user_action", events.login.name, "User logged in")
                    log.log(log_obj(login_event, username))

                    return
                else:
                    with open("credentials.csv", "w") as file:
                        rows[i] = [row[0], row[1], row[2], row[3], int(row[4])+1]
                        writer = csv.writer(file)
                        writer.writerows(rows)

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
    """
    Get the role of the current user.

    This function returns the role of the current user, which is stored in the
    global variable `current_user_role`.

    :return: The role of the current user.
    """
    return current_user_role
