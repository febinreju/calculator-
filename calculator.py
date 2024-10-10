import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Styling the buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 18), padding=10)

# Global variable for the calculator expression
expression = ""

# Function to update the expression
def update_expression(value):
    global expression
    expression += str(value)
    display_var.set(expression)

# Function to evaluate the expression
def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result  # Store result for next calculation
    except:
        display_var.set("Error")
        expression = ""

# Function to clear the display
def clear_display():
    global expression
    expression = ""
    display_var.set("")

# Function to handle backspace
def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

# Create a string variable to store the display value
display_var = tk.StringVar()

# Create the display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Button text and layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and position the buttons
for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=calculate)
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Special buttons for clear and backspace
clear_button = ttk.Button(root, text="C", command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

backspace_button = ttk.Button(root, text="⌫", command=backspace)
backspace_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Adjust grid weights to make the buttons responsive
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main loop of the application
root.mainloop()
