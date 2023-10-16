import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def on_submit():

    is_submitted.set(True)  
    window.destroy()  

def create_authorization_page():
    global window, entry_2fa, is_submitted  

    # Use ThemedTk instead of tk.Tk to get access to extra themes
    window = ThemedTk(theme="equilux")
    window.title("2FA Authentication")
    window.geometry("300x160")

    # Manually set background color
    desired_background_color = "#2e2e2e"  # Example color
    window.configure(bg=desired_background_color)

    label = ttk.Label(window, text="Enter your 2FA code:", background=desired_background_color)
    label.pack(pady=15)

    entry_2fa = ttk.Entry(window)
    entry_2fa.pack(pady=15, padx=15, fill=tk.X)
    
    submit_button = ttk.Button(window, text="Submit", command=on_submit)
    submit_button.pack(pady=15)
    

    is_submitted = tk.BooleanVar(window, value=False)  
    window.wait_window()  
    
    return is_submitted.get()


if __name__ == "__main__":
    is_authorization_successful = create_authorization_page()
    print("Was Authorization successful?", is_authorization_successful)
