import tkinter as tk
import random

def roll_dice():
    return random.randint(1, 6)

def button_clicked(): 
    dice_number = roll_dice()
    result_label.config(text=f"Result: {dice_number}")

window = tk.Tk()
window.title("Dice Rolling Simulator")
window.geometry("500x350")
window.configure(bg="white")
window.resizable(False, False)

title_label = tk.Label(
    window,
    text="🎲 Dice Rolling Simulator",
    bg="white",
    fg="black",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=30)

result_label = tk.Label(
    window,
    text="Click the button",
    bg="white",
    fg="black",
    font=("Arial", 14),
    wraplength=350,
    justify="center"
)

result_label.pack(pady=40)

roll_button = tk.Button(
    window,
    text="Roll the Dice",
    command=button_clicked,
    font=("Arial", 12, "bold"),
    cursor="hand2"
)

roll_button.pack(pady=20)

window.mainloop()