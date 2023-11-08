from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk


# Function to create the pharmacy info window 
def create_info_window():
    # Create the window
    pharm_info_window = tk.Toplevel()
    pharm_info_window.title("Pharmacy Information")

    # Configure the window to make it non-resizable
    pharm_info_window.geometry("500x260")
    pharm_info_window.resizable(False, False)

    # Create a frame to hold the content
    frame = ttk.Frame(pharm_info_window)
    frame.pack(expand=True, fill="both")

    hours_label2 = ttk.Label(frame, text="\nThank you for using the Pharmacy Management System version 1.0!\n")
    hours_label2.pack(side="top")

    # Create the absolute path to the image file by joining the directory and the filename
    logo_path = os.path.join("GUI","arizona_small.png")
    
    # Create a PhotoImage object of the image in the path
    logo_image = Image.open(logo_path)
    photo_object = ImageTk.PhotoImage(logo_image)

    # label to display the image
    photo_label = ttk.Label(frame, image=photo_object)
    photo_label.image = photo_object
    photo_label.pack(side="top")

    # label to act as header for pharmacy info
    header_label = ttk.Label(frame, text="\nPharmacy information:")
    header_label.pack(side="top")

    # create a string to display pharmacy info
    info_string = ("Name: Wildcat Pharmacy (main campus location)\n"
                   "Website: sfwe.engineering.arizona.edu\n"
                   "Address: The University of Arizona | Tucson, AZ 85721\n"
                   "Owner: Harrison Pearl\n"
                   "Phone: 520-555-1234\n"
                   "Hours: 9am-5pm, Mon-Fri\n"
                   )
    
    # label to display pharmacy info
    info_label = ttk.Label(frame, text=info_string)
    info_label.pack(side="top")

