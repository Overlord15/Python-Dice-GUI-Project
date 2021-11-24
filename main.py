import tkinter as tk
import random

window = tk.Tk()

window.maxsize(900, 700)
window.minsize(900, 700)
window.grid
window.title = ("DICE ROLLER SIMULATOR")
header = tk.Label(window, text="DICE ROLLER", font=(
    "Stencil Regular", 50), bg="magenta").pack(fill=tk.X)
dicelabel = tk.Label(window, font=("bold", 400))


def roll():
    number = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    dicelabel.config(text=f"{random.choice(number)}")
    dicelabel.pack()


button1 = tk.Button(window, text="Roll The Dice", font=("Arial Rounded MT Bold", 20), bg="cyan",
                    fg="red", relief=tk.RAISED, height=2, width=10, command=lambda:roll()).pack(side=tk.TOP)


window.mainloop()
