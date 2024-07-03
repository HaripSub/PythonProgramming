import tkinter as tk
from tkinter import ttk, messagebox
from translate import Translator


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Source Language Label and Dropdown (if needed)
        ttk.Label(root, text="Source language:").grid(row=0, column=0, padx=10, pady=10)
        self.source_language = ttk.Combobox(root, values=["en", "fr", "es", "de"], state="readonly")
        self.source_language.set("en")
        self.source_language.grid(row=0, column=1, padx=10, pady=10)

        # Destination Language Label and Dropdown
        ttk.Label(root, text="Destination language:").grid(row=1, column=0, padx=10, pady=10)
        self.dest_language = ttk.Combobox(root, values=["fr", "en", "es", "de", "ta"], state="readonly")
        self.dest_language.set("fr")
        self.dest_language.grid(row=1, column=1, padx=10, pady=10)

        # Input Label and Text Area
        ttk.Label(root, text="Enter text to translate:").grid(row=2, column=0, padx=10, pady=10)
        self.input_area = tk.Text(root, width=50, height=10)  # Use Text widget for multiline input
        self.input_area.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # Output Label and Text Area
        ttk.Label(root, text="Translated text:").grid(row=3, column=0, padx=10, pady=10)
        self.output_text = tk.Text(root, width=50, height=10, wrap=tk.WORD)  # Multiline Text widget for output
        self.output_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

        # Translate Button
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=4, column=1, padx=10, pady=10)

        # Clear Button
        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_text)
        self.clear_button.grid(row=4, column=2, padx=10, pady=10)

    def translate_text(self):
        input_text = self.input_area.get("1.0", tk.END).strip()  # Retrieve text from Text widget
        src_lang = self.source_language.get()
        dest_lang = self.dest_language.get()

        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        try:
            translator = Translator(from_lang=src_lang, to_lang=dest_lang)
            translation = translator.translate(input_text)
            self.output_text.delete("1.0", tk.END)  # Clear existing text
            self.output_text.insert(tk.END, translation)
        except Exception as e:
            messagebox.showerror("Error", f"Translation error: {str(e)}")

    def clear_text(self):
        self.input_area.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
