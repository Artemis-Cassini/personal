# Importing tkinter module
import tkinter as tk
from tkinter import *

# Creating a window
window = Tk()
window.title("Weight Converter")  # Title of the window
window.geometry("500x500")  # Geometry of the window

# Variable to hold the input weight
kg = StringVar()

# Header Label
Label(window, text="WEIGHT CONVERTER", font=("Arial", 20), bg="black", fg="yellow").pack(pady=10)

# Input Section
Label(window, text="Enter the weight in Kgs", font=("Arial", 14)).pack(pady=5)
Entry(window, textvariable=kg).pack(pady=5)  # Entry field

# Result Label
result_label = Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Conversion Functions
def convert_to_gram():
    try:
        kg_value = float(kg.get())
        gram = kg_value * 1000
        result_label.config(text=f"This weight in grams is: {gram} grams")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

def convert_to_ounce():
    try:
        kg_value = float(kg.get())
        ounce = kg_value * 35.274
        result_label.config(text=f"This weight in ounces is: {ounce} ounces")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

def convert_to_pound():
    try:
        kg_value = float(kg.get())
        pound = kg_value * 2.20462
        result_label.config(text=f"This weight in pounds is: {pound} pounds")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

# Buttons
Button(window, text="Convert to Gram", bg="blue", fg="white", command=convert_to_gram).pack(pady=5)
Button(window, text="Convert to Ounce", bg="blue", fg="white", command=convert_to_ounce).pack(pady=5)
Button(window, text="Convert to Pound", bg="blue", fg="white", command=convert_to_pound).pack(pady=5)

# Run the application
window.mainloop()