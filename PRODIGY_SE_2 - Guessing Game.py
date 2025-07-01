
import tkinter as tk
import random
from tkinter import messagebox

number = random.randint(1, 100)
count = 0

def check_guess():
    global count, number
    try:
        guess = int(guess_entry.get())
        count += 1

        if guess < number:
            result_label.config(text="Too Low! Try Again.")
        elif guess > number:
            result_label.config(text="Too High! Try Again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed it in {count} tries")
            start_new_game()

    except ValueError:
        result_label.config(text="Please enter a valid number.")

def start_new_game():
    global number, count
    number = random.randint(1, 100)
    count = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100")


window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("300x250")

title_label = tk.Label(window, text="Guess the Number (1-100)", font=("Arial", 14))
title_label.pack(pady=10)

guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack(pady=5)

guess_button = tk.Button(window, text="Check Guess", command=check_guess, font=("Arial", 12))
guess_button.pack(pady=10)

result_label = tk.Label(window, text="Guess a number between 1 and 100", font=("Arial", 12))
result_label.pack(pady=10)

reset_button = tk.Button(window, text="New Game", command=start_new_game)
reset_button.pack(pady=5)

window.mainloop()

