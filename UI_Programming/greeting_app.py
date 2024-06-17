import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def show_greeting():
    name = name_entry.get()
    if name:
        try:
            current_hour = datetime.now().hour
            # Determine the appropriate greeting based on the current hour
            if 5 <= current_hour <= 11:
                greeting = "Good morning"
            elif 12 <= current_hour <= 17:
                greeting = "Good afternoon"
            elif 18 <= current_hour <= 21:
                greeting = "Good evening"
            else:
                greeting = "Good night"

            # Show the greeting message
            messagebox.showinfo("Hello", f"{greeting}, {name}!")

            # Clear the entry field
            name_entry.delete(0, tk.END)
        except Exception as e:
            # Show an error message in case of unexpected error
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    else:
        # Show a warning if the name field is empty
        messagebox.showwarning("Input Error", "Please enter your name.")


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# Create the main window
window = tk.Tk()
window.title("Greeting App")

# Center the window
center_window(window)

# Create a label
name_label = tk.Label(window, text="Enter your name:")
name_label.pack(pady=10)

# Create an entry field
name_entry = tk.Entry(window)
name_entry.pack(pady=5)

# Create a button
greet_button = tk.Button(window, text="Greet the user", command=show_greeting)
greet_button.pack(pady=10)

# Run the application
window.mainloop()
