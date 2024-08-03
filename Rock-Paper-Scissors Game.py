import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x300")
        self.root.configure(bg="#333")

        self.user_score = 0
        self.computer_score = 0

        # Instructions
        self.instructions = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=('Arial', 12), bg="#333", fg="white")
        self.instructions.pack(pady=10)

        # Buttons for choices
        self.rock_button = tk.Button(self.root, text="Rock", font=('Arial', 12), bg="#4CAF50", fg="white", command=lambda: self.play("Rock"))
        self.rock_button.pack(pady=5)
        self.paper_button = tk.Button(self.root, text="Paper", font=('Arial', 12), bg="#4CAF50", fg="white", command=lambda: self.play("Paper"))
        self.paper_button.pack(pady=5)
        self.scissors_button = tk.Button(self.root, text="Scissors", font=('Arial', 12), bg="#4CAF50", fg="white", command=lambda: self.play("Scissors"))
        self.scissors_button.pack(pady=5)

        # Result display
        self.result_label = tk.Label(self.root, text="", font=('Arial', 12), bg="#333", fg="white")
        self.result_label.pack(pady=10)

        # Score display
        self.score_label = tk.Label(self.root, text=f"User: {self.user_score}  Computer: {self.computer_score}", font=('Arial', 12), bg="#333", fg="white")
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")
        
        self.ask_play_again()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "You win!"
        else:
            return "Computer wins!"

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if not play_again:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
