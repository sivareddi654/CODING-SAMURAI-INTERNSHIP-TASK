import tkinter as tk
from tkinter import messagebox
import random

number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result_label.config(text="Too Low! Try again.")
        elif guess > number:
            result_label.config(text="Too High! Try again.")
        else:
            messagebox.showinfo("Correct!", "You guessed the number!")
    except:
        result_label.config(text="Please enter a valid number")

app = tk.Tk()
app.title("Number Guessing Game")
app.geometry("300x250")

title = tk.Label(app, text="Guess the Number (1–100)", font=("Arial", 12))
title.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

btn = tk.Button(app, text="Check Guess", command=check_guess)
btn.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=5)

app.mainloop()
