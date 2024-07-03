import tkinter as tk


def send_message():
    user_message = entry_box.get()
    if user_message:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + user_message + "\n")
        chat_display.config(state=tk.DISABLED)
        entry_box.delete(0, tk.END)
        respond_to_message(user_message)


def respond_to_message(message):
    # Basic responses for learning Python
    message = message.lower()
    if "hello" in message:
        bot_message = "Hello! I'm here to help you learn Python. Ask me anything!"
    elif "variable" in message:
        bot_message = ("In Python, a variable is used to store information. "
                       "For example:\n"
                       "```\n"
                       "x = 5\n"
                       "y = 'Hello'\n"
                       "```\n"
                       "Here, `x` is an integer variable, and `y` is a string variable.")
    elif "function" in message:
        bot_message = ("A function in Python is defined using the `def` keyword. "
                       "For example:\n"
                       "```\n"
                       "def greet(name):\n"
                       "    return 'Hello, ' + name\n"
                       "print(greet('Alice'))\n"
                       "```\n"
                       "This defines a function `greet` that takes a name as an argument and returns a greeting.")
    elif "loop" in message:
        bot_message = ("Python has two main types of loops: `for` and `while`. "
                       "For example:\n"
                       "```\n"
                       "# For loop\n"
                       "for i in range(5):\n"
                       "    print(i)\n"
                       "\n"
                       "# While loop\n"
                       "count = 0\n"
                       "while count < 5:\n"
                       "    print(count)\n"
                       "    count += 1\n"
                       "```\n"
                       "These loops will print numbers from 0 to 4.")
    elif "list" in message:
        bot_message = ("A list in Python is a collection of items. "
                       "For example:\n"
                       "```\n"
                       "my_list = [1, 2, 3, 4, 5]\n"
                       "print(my_list)\n"
                       "print(my_list[0])  # Accessing the first item\n"
                       "```\n"
                       "Lists can contain different data types and can be accessed using indices.")
    elif "bye" or "quit" in message:
        bot_message = "Goodbye! Have a great day!"
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "Bot: " + bot_message + "\n")
        chat_display.config(state=tk.DISABLED)
        root.update()  # Update the display to show the goodbye message
        root.after(2000, root.quit)  # Close the application after 3000 milliseconds (3 seconds)
        return
    else:
        bot_message = "I'm sorry, I don't understand that. Can you ask about Python concepts like variables, " \
                      "functions, loops, or lists? "

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "Bot: " + bot_message + "\n")
    chat_display.config(state=tk.DISABLED)


# Initialize the main window
root = tk.Tk()
root.title("Python Learning Chat Box")

# Create a chat display area
chat_display = tk.Text(root, height=20, width=60, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Add an initial greeting message
chat_display.config(state=tk.NORMAL)
chat_display.insert(tk.END, "Bot: Hello! I'm here to help you learn Python. Ask me anything!\n")
chat_display.config(state=tk.DISABLED)

# Create an entry box for typing messages
entry_box = tk.Entry(root, width=40)
entry_box.pack(side=tk.LEFT, padx=10, pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the application
root.mainloop()
