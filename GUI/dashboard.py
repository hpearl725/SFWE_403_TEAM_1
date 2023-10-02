import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import csv
import os
import GUI.inventory_table
import GUI.patients_table
import GUI.users_table

# Declare the Treeview widgets as global variables
inventory_tree = None
patients_tree = None
users_tree = None
frame = None
add_user_button = None


# Function to open the new user window
def open_new_user_window(current_user_role):
    # Check if the current user is a manager
    if current_user_role != "manager":
        messagebox.showerror("Permission Denied", "Only managers can add new users.")
        return

    os.system('python new_user_window.py')


# Create the dashboard window
def create_dashboard(current_user_role):
    global inventory_tree, patients_tree, users_tree, frame, add_user_button
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    # Configure the window to have no border and make it resizable
    dashboard.overrideredirect(True)
    dashboard.geometry("800x600")
    dashboard.resizable(False, False)

    style = ThemedStyle(dashboard)
    style.set_theme("equilux")

    frame = ttk.Frame(dashboard)
    frame.pack(expand=True, fill="both")

    button_frame = ttk.Frame(frame)
    button_frame.pack(side="top", fill="x", padx=10, pady=10)

    inventory_button = ttk.Button(button_frame, text="Inventory", command=show_inventory_table)
    patients_button = ttk.Button(button_frame, text="Patients", command=show_patients_table)
    users_button = ttk.Button(button_frame, text="Users", command=show_users_table)
    settings_button = ttk.Button(button_frame, text="Settings", command=lambda: show_user_button(current_user_role))
    exit_button = ttk.Button(frame, text="Exit", command=dashboard.quit)

    inventory_button.pack(side="left", padx=10)
    patients_button.pack(side="left", padx=10)
    users_button.pack(side="left", padx=10)
    settings_button.pack(side="left", padx=10)

    inventory_tree = GUI.inventory_table.create_inventory_table(frame)
    patients_tree = GUI.patients_table.create_patients_table(frame)
    users_tree = GUI.users_table.create_users_table(frame)

    exit_button.pack(side="bottom", anchor="se", padx=10, pady=10)

    dashboard.mainloop()


def show_inventory_table():
    GUI.inventory_table.show_inventory_table(inventory_tree)
    GUI.patients_table.hide_patients_table(patients_tree)
    GUI.users_table.hide_users_table(users_tree)
    hide_add_user_button()


def show_patients_table():
    GUI.inventory_table.hide_inventory_table(inventory_tree)
    GUI.patients_table.show_patients_table(patients_tree)
    GUI.users_table.hide_users_table(users_tree)
    hide_add_user_button()


def show_users_table():
    GUI.inventory_table.hide_inventory_table(inventory_tree)
    GUI.patients_table.hide_patients_table(patients_tree)
    GUI.users_table.show_users_table(users_tree)
    hide_add_user_button()


def show_user_button(current_user_role):
    GUI.inventory_table.hide_inventory_table(inventory_tree)
    GUI.patients_table.hide_patients_table(patients_tree)
    GUI.users_table.hide_users_table(users_tree)
    show_add_user_button(current_user_role)


def hide_add_user_button():
    global add_user_button
    if add_user_button is not None:
        add_user_button.pack_forget()


def show_add_user_button(current_user_role):
    global add_user_button
    if add_user_button is None:
        add_user_button = ttk.Button(frame, text="Add User", command=lambda: open_new_user_window(current_user_role))
    add_user_button.pack(side="top", pady=10)


if __name__ == "__main__":
    create_dashboard()
