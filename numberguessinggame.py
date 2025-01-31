import tkinter as tk
from tkinter import *
import random

# Initialize the main window
win = tk.Tk()
win.geometry("750x750")
win.title("Number Guessing Game")

# Define variables before using them in widgets
hint = StringVar()
score = IntVar()
final_score = IntVar()
guess = IntVar()

# Set initial values for the variables
hint.set("Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

# Define the target number to guess
num = random.randint(1, 50)

# Define the function to check the guess
def fun():
    try:
        x = guess.get()
        if score.get() > 0:
            if x < 1 or x > 50:
                hint.set("Invalid input! Guess a number between 1 and 50.")
            elif num == x:
                hint.set("Congrats! YOU WON!!!")
            elif num > x:
                hint.set("Your guess was too low. Try a higher number.")
            elif num < x:
                hint.set("Your guess was too high. Try a lower number.")
            
            # Reduce the score
            score.set(score.get() - 1)
            final_score.set(score.get())
            
            # Check if score reaches 0
            if score.get() <= 0 and num != x:
                hint.set("Game Over! You Lost.")
        else:
            hint.set("Game Over! You Lost.")
    except TclError:
        hint.set("Enter a valid number.")

# Create widgets
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Label(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Label(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

# Run the application
win.mainloop()