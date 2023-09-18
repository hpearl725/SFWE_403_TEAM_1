import tkinter as tk
from tkinter import messagebox
from dashboard import create_dashboard

# Function to validate the login credentials and open the dashboard
def open_dashboard():
    username = username_entry.get()
    password = password_entry.get()

    # Replace these with your actual username and password
    correct_username = "a"
    correct_password = "1"

    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()  # Close the login window
        create_dashboard()  # Open the dashboard window
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Create the main login window
root = tk.Tk()
root.title("Login Page")

# Create labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Show asterisks for password
password_entry.pack(pady=10)

# Create the Login button
login_button = tk.Button(root, text="Login", command=open_dashboard)
login_button.pack()

# Center the login window on the screen
root.geometry("+%d+%d" % ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2,
                            (root.winfo_screenheight() - root.winfo_reqheight()) / 2))

# Start the Tkinter main loop for the login page
root.mainloop()
