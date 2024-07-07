import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def convert_length():
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        # Conversion factors relative to meters
        conversion_factors = {
            'Meters': 1,
            'Centimeters': 100,
            'Millimeters': 1000,
            'Kilometers': 0.001,
            'Inches': 39.3701,
            'Feet': 3.28084,
            'Yards': 1.09361,
            'Miles': 0.000621371
        }

        # Convert input to meters, then from meters to the desired unit
        value_in_meters = value / conversion_factors[from_unit]
        result = value_in_meters * conversion_factors[to_unit]

        # Round result to 2 decimal places
        rounded_result = round(result, 2)

        result_label.config(text=f"Converted value: {rounded_result} {to_unit.lower()}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")
    from_combobox.set("Meters")
    to_combobox.set("Centimeters")


# Create main window
root = tk.Tk()
root.title("Unit Conversion")
root.geometry("350x300")

# Create entry frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry_label = tk.Label(entry_frame, text="Enter value to convert:")
entry_label.pack(side=tk.LEFT, padx=5)
entry = tk.Entry(entry_frame)
entry.pack(side=tk.LEFT, padx=5)
entry.focus()

# Create combobox frame for selecting units
combobox_frame = tk.Frame(root)
combobox_frame.pack(pady=10)

from_label = tk.Label(combobox_frame, text="From:")
from_label.pack(side=tk.LEFT, padx=5)
from_var = tk.StringVar()
from_combobox = ttk.Combobox(combobox_frame, textvariable=from_var, values=[
                             "Meters", "Centimeters", "Millimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"])
from_combobox.set("Meters")  # default value
from_combobox.pack(side=tk.LEFT, padx=5)

to_label = tk.Label(combobox_frame, text="To:")
to_label.pack(side=tk.LEFT, padx=5)
to_var = tk.StringVar()
to_combobox = ttk.Combobox(combobox_frame, textvariable=to_var, values=[
                           "Meters", "Centimeters", "Millimeters", "Kilometers", "Inches", "Feet", "Yards", "Miles"])
to_combobox.set("Centimeters")  # default value
to_combobox.pack(side=tk.LEFT, padx=5)

# Create button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert", command=convert_length)
convert_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Create result label frame
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="")
result_label.pack()

# Run the application
root.mainloop()
