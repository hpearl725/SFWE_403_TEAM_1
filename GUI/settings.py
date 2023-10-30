import os
import sys
import csv
import tkinter as tk
from logs.log import logger, log_obj, event, events
# function that uses tkinter to create a window to change the password of the current user which asks for current password before changing it


def change_password(current_user):
    # function that checks if the current password entered is correct
    current_password = None
    window = tk.Tk()
    window.title('Change Password')
    window.geometry('400x150')
    window.resizable(False, False)
    # creating the labels and entries for the window
    if current_user.role != 'manager':
        current_password_label = tk.Label(window, text='Current Password: ')
        current_password = tk.Entry(window, show='*')
    new_password_label = tk.Label(window, text='New Password: ')
    new_password = tk.Entry(window, show='*')
    confirm_password_label = tk.Label(window, text='Confirm Password: ')
    confirm_password = tk.Entry(window, show='*')
    # creating the button that changes the password
    change_password_button = tk.Button(window, text='Change Password', command=lambda: change_password_button_click(
        window, current_user, current_password, new_password, confirm_password, current_user.username))

    current_password_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
    current_password.grid(row=0, column=1, padx=10, pady=5, sticky='w')
    new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    new_password.grid(row=1, column=1, padx=10, pady=5, sticky='w')
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
    confirm_password.grid(row=2, column=1, padx=10, pady=5, sticky='w')
    change_password_button.grid(
        row=3, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

    # function that checks if the current password entered is correct


def change_password_button_click(window, current_user, current_password, new_password, confirm_password, alt_user):
    # if the current password entered is correct, it will change the password and close the window
    if type(alt_user) != str:
        alt_user = alt_user.get()

    if current_user.role == 'manager' or current_password.get() == current_user.password:
        if new_password.get() == confirm_password.get():
            current_user.password = new_password.get()
            if alt_user != current_user.username:
                with open(os.path.join("GUI", 'users.csv'), 'r') as file:
                    reader = csv.reader(file)
                    users = list(reader)
                    for user in users:
                        if user[1] == alt_user:
                            user[2] = new_password.get()
                            with open(os.path.join("GUI", 'users.csv'), 'w') as file:
                                writer = csv.writer(file)
                                writer.writerows(users)
            else:
                current_user.save()
            window.destroy()
            # log the login event
            log = logger(os.path.join("GUI", "log.csv"))
            if alt_user == current_user.username:
                login_event = event(
                    "user_action", events.change_password.name, f"{current_user.username} changed their password")
            else:
                login_event = event(
                    "user_action", events.change_password.name, f"{current_user.username} changed {alt_user}\'s password")
            log.log(log_obj(login_event, current_user.username))
        else:
            # a popup window that says the password entered is incorrect
            popup = tk.Tk()
            popup.title('Error')
            popup.geometry('300x100')
            popup.resizable(False, False)
            popup_label = tk.Label(
                popup, text='New Passwords do not match. Please try again.')
            popup_label.pack()
            retry_button = tk.Button(
                popup, text='Retry', command=popup.destroy)
            retry_button.pack()
            popup.mainloop()
    else:
        # a popup window that says the password entered is incorrect
        popup = tk.Tk()
        popup.title('Error')
        popup.geometry('300x100')
        popup.resizable(False, False)
        popup_label = tk.Label(popup, text='Incorrect Password.')
        popup_label.pack()
        retry_button = tk.Button(popup, text='Retry', command=popup.destroy)
        retry_button.pack()
        popup.mainloop()


def change_user_settings(current_user):
    # a popup window that asks for the username of the user which they want to change the password of
    window = tk.Tk()
    window.title('Change User Settings')
    window.geometry('400x150')
    window.resizable(False, False)
    # creating the labels and entries for the window
    username_label = tk.Label(window, text='Username: ')
    username = tk.Entry(window)
    new_password_label = tk.Label(window, text='New Password: ')
    new_password = tk.Entry(window, show='*')
    confirm_password_label = tk.Label(window, text='Confirm Password: ')
    confirm_password = tk.Entry(window, show='*')
    # creating the button that changes the password
    change_password_button = tk.Button(window, text='Change Password', command=lambda: change_password_button_click(
        window, current_user, None, new_password, confirm_password, username))

    username_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
    username.grid(row=0, column=1, padx=10, pady=5, sticky='w')
    new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
    new_password.grid(row=1, column=1, padx=10, pady=5, sticky='w')
    confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
    confirm_password.grid(row=2, column=1, padx=10, pady=5, sticky='w')
    change_password_button.grid(
        row=3, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

    window.mainloop()


if __name__ == '__main__':
    change_password('admin')
