import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from logs.log import logger, event, events, log_obj

def on_submit(username):

    is_submitted.set(True) 

    # Log the login event
    log = logger(os.path.join("GUI","log.csv"))
    login_event = event("user_action", events.login.name, "User logged in")
    log.log(log_obj(login_event, username))

    window.destroy()  

def create_authorization_page(username):
    global window, entry_2fa, is_submitted  

    window = tk.Toplevel()
    window.title("2FA Authentication")
    window.geometry("300x160")

    frame = ttk.Frame(window)
    frame.pack(expand=True, fill="both")

    label = ttk.Label(frame, text="Enter your 2FA code:")
    label.pack(pady=15)

    entry_2fa = ttk.Entry(frame)
    entry_2fa.pack(pady=15, padx=15, fill=tk.X)
    
    submit_button = ttk.Button(frame, text="Submit", command=lambda: on_submit(username))
    submit_button.pack(pady=15)
    
    is_submitted = tk.BooleanVar(frame, value=False)  
    window.wait_window()  
    
    return is_submitted.get()


if __name__ == "__main__":
    is_authorization_successful = create_authorization_page()
    print("Was Authorization successful?", is_authorization_successful)
