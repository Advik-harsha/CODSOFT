# Creating a Simple Calculator 
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#333")

        # StringVar to store the input
        self.input_text = tk.StringVar()

        # Entry widget to display the input and result
        self.input_field = tk.Entry(self.root, textvariable=self.input_text, font=('Arial', 18), bd=10, 
                                    insertwidth=4, width=14, borderwidth=4, justify='right', bg="#eee")
        self.input_field.grid(row=0, column=0, columnspan=4, pady=20)

        # Add buttons
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        button_colors = {
            '0': "#4CAF50", '1': "#4CAF50", '2': "#4CAF50", '3': "#4CAF50", '4': "#4CAF50",
            '5': "#4CAF50", '6': "#4CAF50", '7': "#4CAF50", '8': "#4CAF50", '9': "#4CAF50",
            'C': "#f44336", '=': "#ff9800", '/': "#2196F3", '*': "#2196F3", '-': "#2196F3", '+': "#2196F3"
        }

        row_val = 1
        col_val = 0

        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                               bg=button_colors[text], fg="white", bd=0, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights to make buttons expand with window
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.input_text.set('')
        elif char == '=':
            try:
                result = eval(self.input_text.get())
                self.input_text.set(result)
            except Exception as e:
                self.input_text.set("Error")
        else:
            current_text = self.input_text.get()
            self.input_text.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
