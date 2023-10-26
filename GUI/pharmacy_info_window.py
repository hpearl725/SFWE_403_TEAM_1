from tkinter import ttk
import tkinter as tk
import os
from ttkthemes import ThemedStyle

# Function to create the welcome screen 
def create_welcome_screen():

    # Create the new user window
    new_user_window = tk.Tk()
    new_user_window.title("Pharmacy Information")

    # Configure the window to make it non-resizable
    new_user_window.geometry("600x600")  # Increased height to accommodate additional fields
    new_user_window.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(new_user_window)
    style.set_theme("equilux")  # Use the "equilux" theme or choose another theme

    # Create a frame to hold the content
    frame = ttk.Frame(new_user_window)
    frame.pack(expand=True, fill="both")

    # Create a Label for the welcome message
    welcome_label = ttk.Label(frame, text="Welcome to The Pharmacy of Perception Management System!")
    welcome_label.pack()

    # Specify the relative path to the image file
    image_filename = "logo.png"

    # Get the absolute path to the directory containing the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the absolute path to the image file by joining the directory and the filename
    image_path = os.path.join("GUI","logo.png")
    
    image = tk.PhotoImage(file=image_path)
    image_label = tk.Label(frame, image=image)
    image_label.image = image  # Keep a reference to prevent garbage collection
    image_label.pack()

    hours_label = ttk.Label(frame, text="Hours: 9am-5pm")
    hours_label.pack(side="bottom")

    phone_label = ttk.Label(frame, text="Phone: 323-667-0878")
    phone_label.pack(side="bottom")

    owner_label = ttk.Label(frame, text="Owner: Jim Morrison")
    owner_label.pack(side="bottom")

    address_label = ttk.Label(frame, text="Address: 962 La Cienega Boulevard")
    address_label.pack(side="bottom")

    website_label = ttk.Label(frame, text="Website: pharmacyofperception.com")
    website_label.pack(side="bottom")

    name_label = ttk.Label(frame, text="The Pharmacy of Perception")
    name_label.pack(side="bottom")