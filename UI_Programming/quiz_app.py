import tkinter as tk
from tkinter import messagebox
import json
import random


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.configure(bg='lightblue')  # Set background color for the main window

        self.load_questions()

        self.current_question = 0
        self.score = 0

        # Create a frame for centering all widgets
        self.main_frame = tk.Frame(root, bg='lightblue')
        self.main_frame.pack(expand=True)

        # Label to display the chosen category
        self.category_label = tk.Label(self.main_frame, text="", font=('Arial', 14), bg='lightblue')
        self.category_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.question_label = tk.Label(self.main_frame, text="", font=('Arial', 16), wraplength=400, bg='lightblue')
        self.question_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.radio_var = tk.IntVar()  # Variable to track selected option
        self.radio_buttons = []

        for i in range(4):
            radio_button = tk.Radiobutton(self.main_frame, text="", font=('Arial', 14), variable=self.radio_var,
                                          value=i, bg='lightblue')
            radio_button.grid(row=2 + i, column=0, columnspan=2, sticky='w', padx=10, pady=5)
            self.radio_buttons.append(radio_button)

        self.submit_button = tk.Button(self.main_frame, text="Submit", font=('Arial', 14), command=self.check_answer,
                                       bg='green', fg='white')
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=20)

        self.choose_and_display_category()

    def load_questions(self):
        try:
            with open('questions.json', 'r') as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "The questions file was not found.")
            self.root.destroy()
            return

        # Organize questions by category
        self.questions_by_category = {}
        for question in self.questions:
            category = question.get("category", "Uncategorized")
            if category not in self.questions_by_category:
                self.questions_by_category[category] = []
            self.questions_by_category[category].append(question)

    def choose_and_display_category(self):
        # Randomly choose a category
        categories = list(self.questions_by_category.keys())
        chosen_category = random.choice(categories)

        # Update category label to display the chosen category
        self.category_label.config(text=f"Category: {chosen_category}")

        # Select 5 random questions from the chosen category
        self.questions = random.sample(self.questions_by_category[chosen_category], 5)
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])

            # Clear previous selection
            self.radio_var.set(-1)

            # Update radio buttons with choices
            for i, choice in enumerate(question["choices"]):
                self.radio_buttons[i].config(text=choice)

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

        # Change button color based on answer correctness
        if selected_answer == self.questions[self.current_question]["answer"]:
            self.submit_button.config(bg='green')
        else:
            self.submit_button.config(bg='red')

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
