import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function for password generation
def generate_password():
    entry.delete(0, END)

    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

    password = ""

    # Check selected strength
    if var.get() == 1:
        # Low strength
        characters = lower
    elif var.get() == 2:
        # Medium strength
        characters = upper
    elif var.get() == 3:
        # Strong strength
        characters = symbols
    else:
        # If no option is selected
        print("Please choose an option")
        return

    # Generate the password
    for i in range(length):
        password += random.choice(characters)

    # Insert the password into the entry field
    entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    random_password = entry.get()
    pyperclip.copy(random_password)

# Main Function
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of GUI window
root.title("Random Password Generator")

# Create label and entry to show the generated password
Random_password = Label(root, text="Password")
Random_password.grid(row=0, column=0, padx=10, pady=10)
entry = Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1, column=0, padx=10, pady=10)

# Create buttons for copying password and generating password
copy_button = Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=10, pady=10)
generate_button = Button(root, text="Generate", command=generate_password)
generate_button.grid(row=0, column=3, padx=10, pady=10)

# Create radio buttons for password strength
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=2)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky='E')

# Combo Box for length of password
combo = Combobox(root, textvariable=var1)
combo['values'] = tuple(range(8, 33))  # Values from 8 to 32
combo.current(0)
combo.grid(column=1, row=1, padx=10, pady=10)

# Start the GUI
root.mainloop()
