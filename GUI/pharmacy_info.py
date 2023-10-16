from tkinter import ttk
import tkinter as tk
import os

# Function to create the welcome screen 
def create_welcome_screen(frame):

    #Name, web, address, owner, phone, hours
    global welcome_label, website_label, name_label, address_label, owner_label, phone_label, hours_label, image_label

    # Create a Label for the welcome message
    welcome_label = tk.Label(frame, text="Welcome to The Pharmacy of Perception Management System!", padx=50, pady=25)
    welcome_label.pack()

    # Specify the relative path to the image file
    image_filename = "logo.png"

    # Get the absolute path to the directory containing the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the absolute path to the image file by joining the directory and the filename
    image_path = os.path.join(current_directory, image_filename)
    
    image = tk.PhotoImage(file=image_path)
    image_label = tk.Label(frame, image=image)
    image_label.image = image  # Keep a reference to prevent garbage collection
    image_label.pack()

    hours_label = tk.Label(frame, text="Hours: 9am-5pm")
    hours_label.pack(side="bottom")

    phone_label = tk.Label(frame, text="Phone: 323-667-0878")
    phone_label.pack(side="bottom")

    owner_label = tk.Label(frame, text="Owner: Jim Morrison")
    owner_label.pack(side="bottom")

    address_label = tk.Label(frame, text="Address: 962 La Cienega Boulevard")
    address_label.pack(side="bottom")

    website_label = tk.Label(frame, text="Website: pharmacyofperception.com")
    website_label.pack(side="bottom")

    name_label = tk.Label(frame, text="The Pharmacy of Perception")
    name_label.pack(side="bottom")


# Function to show the welcome screen 
def show_welcome_screen():
    welcome_label.pack()
    image_label.pack()

    hours_label.pack(side="bottom")
    phone_label.pack(side="bottom")
    owner_label.pack(side="bottom")
    address_label.pack(side="bottom")
    website_label.pack(side="bottom")
    name_label.pack(side="bottom")

# Function to hide the welcome screen 
def hide_welcome_screen():

    welcome_label.pack_forget()
    image_label.pack_forget()

    website_label.pack_forget()
    name_label.pack_forget()
    address_label.pack_forget()
    owner_label.pack_forget()
    phone_label.pack_forget()
    hours_label.pack_forget()