import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from pymongo import MongoClient


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.configure(bg='lightblue')  # Set background color for the main window

        self.connect_to_db()
        self.load_questions()

        self.current_question = 0
        self.score = 0

        self.setup_ui()

    def connect_to_db(self):
        try:
            self.client = MongoClient(
                'mongodb+srv://haripriyasubramanian:eMzz0qKkY15KfEfN@cluster0.2qhc3hk.mongodb.net/')
            self.db = self.client['questionsdb']
            self.questions_collection = self.db['questions']
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while connecting to the database: {e}")
            self.root.destroy()

    def load_questions(self):
        try:
            questions_cursor = self.questions_collection.find()
            self.questions = list(questions_cursor)
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred while loading questions from the database: {e}")
            self.root.destroy()

        # Organize questions by category
        self.questions_by_category = {}
        for question in self.questions:
            category = question.get("category", "Uncategorized")
            if category not in self.questions_by_category:
                self.questions_by_category[category] = []
            self.questions_by_category[category].append(question)

    def setup_ui(self):
        # Create a frame for centering all widgets
        self.main_frame = tk.Frame(self.root, bg='lightblue')
        self.main_frame.pack(expand=True, padx=20, pady=20)

        # Category selection
        self.category_var = tk.StringVar(self.main_frame)
        self.category_var.set("Select a category")  # default value
        self.category_combobox = ttk.Combobox(self.main_frame, textvariable=self.category_var, state="readonly",
                                              font=('Arial', 14))
        self.category_combobox['values'] = list(self.questions_by_category.keys())
        self.category_combobox.grid(row=0, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(self.main_frame, text="Start Quiz", font=('Arial', 14),
                                      command=self.choose_and_display_category, bg='green', fg='white')
        self.start_button.grid(row=1, column=0, columnspan=2, pady=20)

        self.category_label = tk.Label(self.main_frame, text="", font=('Arial', 14), bg='lightblue')
        self.category_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.question_label = tk.Label(self.main_frame, text="", font=('Arial', 16), wraplength=400, bg='lightblue')
        self.question_label.grid(row=3, column=0, columnspan=2, pady=20)

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)  # Ensure it starts with a value not matching any option
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(self.main_frame, text="", font=('Arial', 14), variable=self.radio_var,
                                          value=i, bg='lightblue')
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(self.main_frame, text="Submit", font=('Arial', 14), command=self.check_answer,
                                       bg='green', fg='white')

    def choose_and_display_category(self):
        chosen_category = self.category_var.get()
        if chosen_category == "Select a category":
            messagebox.showwarning("Warning", "Please select a category.")
            return

        # Update category label to display the chosen category
        self.category_label.config(text=f"Category: {chosen_category}")

        # Select 5 random questions from the chosen category
        self.questions = random.sample(self.questions_by_category[chosen_category], 5)
        self.current_question = 0
        self.score = 0

        # Hide category selection widgets and start button
        self.category_combobox.grid_forget()
        self.start_button.grid_forget()

        # Display the category label
        self.category_label.grid()

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])

            # Clear previous selection
            self.radio_var.set(-1)

            # Update radio buttons with choices and display them
            for i, choice in enumerate(question["choices"]):
                self.radio_buttons[i].config(text=choice)
                self.radio_buttons[i].grid(row=4 + i, column=0, columnspan=2, sticky='w', padx=10, pady=5)

            # Display the submit button
            self.submit_button.grid(row=8, column=0, columnspan=2, pady=20)

            # Reset button color
            self.submit_button.config(bg='green')
        else:
            self.show_result()

    def check_answer(self):
        # Check if an option is selected
        if self.radio_var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer before submitting.")
            return

        selected_index = self.radio_var.get()
        selected_answer = self.questions[self.current_question]["choices"][selected_index]

        # Check if the selected answer is correct
        if selected_answer == self.questions[self.current_question]["answer"]:
            self.score += 1

        # Move to the next question
        self.current_question += 1

        # Display next question or end quiz
        self.display_question()

    def show_result(self):
        # Calculate the final score
        final_score = self.score

        # Determine pass/fail based on a threshold (e.g., 3 out of 5)
        pass_threshold = 3
        if final_score >= pass_threshold:
            result_message = f"Congratulations! You passed the quiz with a score of {final_score}/{len(self.questions)}."
        else:
            result_message = f"Sorry, you did not pass the quiz. Your score was {final_score}/{len(self.questions)}."

        # Display the result message
        messagebox.showinfo("Quiz Completed", result_message)
        self.root.destroy()


# Create the main window
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
