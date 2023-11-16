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
from GUI.users import createUser

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

    # Open the .csv file and search for the username and password
    credentials_file_path = os.path.join('GUI', 'users.csv')

    # flag to prevent additional login attempts after user is locked out
    this_user_locked = False

    with open(credentials_file_path, "r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for i, row in enumerate(rows):
            if row[1] == username:
                if int(row[9]) == 5: # failed attempts stop incrementing after 5
                    messagebox.showerror("Login attempts", "Too many failed attempts")
                    this_user_locked = True
                else:
                    if row[2] == password:
                        if create_authorization_page(username):
                            current_user = createUser(row[0])
                            if row[10] == 'True':
                                new_password = simpledialog.askstring("New Password", "Enter new password:", show='*')
                                row[2] = new_password
                                row[10] = 'False'
                                rows[i] = row
                                with open(credentials_file_path, "w", newline='', encoding='utf-8') as file:
                                    writer = csv.writer(file)
                                    writer.writerows(rows)
                            
                            # Close the login window
                            root.destroy()
                            
                            # Open the dashboard window
                            create_dashboard(current_user)

                            return
                    else:
                        with open(credentials_file_path, "w", newline='', encoding='utf-8') as file:
                            rows[i][9] =  str(int(rows[i][9]) + 1)
                            if rows[i][9]=="5": # write locked status to csv if attempts reach 5
                                rows[i][11] = "True"
                            writer = csv.writer(file)
                            writer.writerows(rows)
    
    if not this_user_locked:
        messagebox.showerror("Login Failed", "Incorrect username or password")


# Create the main login window
root = tk.Tk()
root.title("Login Page")

# Configure the login window to make it non-resizable
root.geometry("400x180")
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
