import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#333")

        # Label for length input
        self.length_label = tk.Label(self.root, text="Password Length:", font=('Arial', 12), bg="#333", fg="white")
        self.length_label.pack(pady=10)

        # Entry for length input
        self.length_entry = tk.Entry(self.root, font=('Arial', 12), width=10)
        self.length_entry.pack(pady=10)

        # Checkbuttons for complexity
        self.include_upper = tk.BooleanVar()
        self.include_lower = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        self.upper_check = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.include_upper, font=('Arial', 12), bg="#333", fg="white", selectcolor="#333")
        self.upper_check.pack(pady=5)
        self.lower_check = tk.Checkbutton(self.root, text="Include Lowercase", variable=self.include_lower, font=('Arial', 12), bg="#333", fg="white", selectcolor="#333")
        self.lower_check.pack(pady=5)
        self.digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.include_digits, font=('Arial', 12), bg="#333", fg="white", selectcolor="#333")
        self.digits_check.pack(pady=5)
        self.special_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.include_special, font=('Arial', 12), bg="#333", fg="white", selectcolor="#333")
        self.special_check.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(self.root, text="Generate Password", font=('Arial', 12), bg="#4CAF50", fg="white", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Display generated password
        self.password_label = tk.Label(self.root, text="", font=('Arial', 12), bg="#333", fg="white")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0.")
            return

        characters = ""
        if self.include_upper.get():
            characters += string.ascii_uppercase
        if self.include_lower.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
