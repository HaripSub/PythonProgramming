import tkinter as tk
from tkinter import messagebox


def evaluate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")


def clear():
    entry.delete(0, tk.END)


def append_char(char):
    entry.insert(tk.END, char)


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field
entry = tk.Entry(window, width=40)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Create buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', '%'
]

# Add buttons to the window
row = 1
col = 0
for button in buttons:
    action = lambda x=button: append_char(x) if x != "=" else evaluate()
    tk.Button(window, text=button, width=10, command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add a clear button
tk.Button(window, text='C', width=10, command=clear).grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()
