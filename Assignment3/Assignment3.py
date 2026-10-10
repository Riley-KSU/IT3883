# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Riley Dunevent
# Assignment Number: Assignment 3
# Due Date: 10/11/2025
# Purpose: Convert miles per gallon to kilometers per liter.
# Resources: I used the class D2L notes and examples from D2L. I also used W3 schools pyton material to help with this assignment.

from tkinter import *


# Convert the user input and handle blank boxes or letters.
def fuel_converter(*args):
    try:
        mpg = float(mpg_user.get())
        result = mpg * 0.425143707
        kmpl_converted.set(f"{result:.6f}")
    except ValueError:
        kmpl_converted.set("Please enter a number")


# Creates the window.
root = Tk()
root.title("MPG converter to KmPL")

# Store the user input and converted output.
mpg_user = StringVar()
kmpl_converted = StringVar()

# Create and position the labels and input box.
mpg_label = Label(root, text="Miles per gallon:")
mpg_label.grid(row=0, column=0, padx=10, pady=10)

mpg_entry = Entry(root, textvariable=mpg_user)
mpg_entry.grid(row=0, column=1, padx=10, pady=10)

kml_label = Label(root, text="Kilometers per liter:")
kml_label.grid(row=1, column=0, padx=10, pady=10)

result_label = Label(root, textvariable=kmpl_converted, width=22)
result_label.grid(row=1, column=1, padx=10, pady=10)

# Calls convert whenever the input changes.
mpg_user.trace_add("write", fuel_converter)

# Keeps the window open and waiting for user input.
root.mainloop()
