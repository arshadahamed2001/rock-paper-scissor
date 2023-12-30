import tkinter as tk
from tkinter import messagebox
import random

user_points = 0
computer_points = 0
winning_score = 10 

def determine_winner(user_choice, computer_choice):
    global user_points
    global computer_points
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_points += 1
        return "You win!"
    else:
        computer_points += 1
        return "Computer wins!"

def user_choice(choice):
    if user_points < winning_score and computer_points < winning_score:
        computer_choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(computer_choices)

        result = determine_winner(choice, computer_choice)

        result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

        score_label.config(text=f"Your Score: {user_points}  Computer Score: {computer_points}")

        if user_points >= winning_score:
            messagebox.showinfo("Game Over", "You win the game!")
            reset_game()
        elif computer_points >= winning_score:
            messagebox.showinfo("Game Over", "Computer wins the game!")
            reset_game()

def reset_game():
    global user_points
    global computer_points
    
    user_points = 0
    computer_points = 0
    
    instruction_label.config(text="Choose Rock, Paper, or Scissors:")
    result_label.config(text="")
    score_label.config(text="Your Score: 0  Computer Score: 0")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instruction_label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack()

score_label = tk.Label(root, text="Your Score: 0  Computer Score: 0", font=("Helvetica", 12))
score_label.pack()

play_again_button = tk.Button(root, text="Reset Game", command=reset_game)
play_again_button.pack()

root.mainloop()
