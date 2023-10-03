import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

def on_submit():
    # [Put your code verification logic here]
    # print("2FA Code Submitted:", entry_2fa.get())
    is_submitted.set(True)  # Set the flag to True since it's submitted
    window.destroy()  # Close the window

def create_authorization_page():
    global window, entry_2fa, is_submitted  # Make these variables accessible in on_submit
    
    window = ThemedTk(theme="equilux")
    window.title("2FA Authentication")
    window.geometry("300x150")

    label = ttk.Label(window, text="Enter your 2FA code:")
    label.pack(pady=15)

    entry_2fa = ttk.Entry(window)
    entry_2fa.pack(pady=15, padx=15, fill=tk.X)
    
    submit_button = ttk.Button(window, text="Submit", command=on_submit)
    submit_button.pack(pady=15)
    
    is_submitted = tk.BooleanVar(window, value=False)  # Create a boolean flag
    window.wait_window()  # Wait until the window is destroyed
    
    return is_submitted.get()  # Return the flag value

# Example usage:
is_authorization_successful = create_authorization_page()
print("Was Authorization successful?", is_authorization_successful)

if __name__ == "__main__":
    create_authorization_page()