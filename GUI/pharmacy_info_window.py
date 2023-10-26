from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

# Function to create the pharmacy info window 
def create_info_window():

    # Create the window
    new_user_window = tk.Toplevel()
    new_user_window.title("Pharmacy Information")

    # Configure the window to make it non-resizable
    new_user_window.geometry("600x600")
    new_user_window.resizable(False, False)

    # Create a ThemedStyle instance for the modern theme
    style = ThemedStyle(new_user_window)
    style.set_theme("equilux")  # Use the "equilux" theme

    # Create a frame to hold the content
    frame = ttk.Frame(new_user_window)
    frame.pack(expand=True, fill="both")

    # Create a Label for the welcome message
    welcome_label = ttk.Label(frame, text="Welcome to The Pharmacy of Perception Management System!")
    welcome_label.pack()

    # Create the absolute path to the image file by joining the directory and the filename
    logo_path = os.path.join("GUI","logo.png")
    
    # Create a PhotoImage object of the image in the path
    logo_image = Image.open(logo_path)
    photo_object = ImageTk.PhotoImage(logo_image)

    # create a label to display the image
    photo_label = ttk.Label(frame, image=photo_object)
    photo_label.image = photo_object
    photo_label.pack(side="top")

    hours_label = ttk.Label(frame, text="Hours: 9am-5pm")
    hours_label.pack(side="top")

    phone_label = ttk.Label(frame, text="Phone: 323-667-0878")
    phone_label.pack(side="top")

    owner_label = ttk.Label(frame, text="Owner: Jim Morrison")
    owner_label.pack(side="top")

    address_label = ttk.Label(frame, text="Address: 962 La Cienega Boulevard")
    address_label.pack(side="top")

    website_label = ttk.Label(frame, text="Website: pharmacyofperception.com")
    website_label.pack(side="top")

    name_label = ttk.Label(frame, text="The Pharmacy of Perception")
    name_label.pack(side="top")
