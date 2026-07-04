import tkinter as tk
import random

def roll_dice():
    return random.randint(1, 6)
   
def button_clicked(): 
    dice_number = roll_dice()
    result_label.config(text=f"Result: {dice_number}")

window = tk.Tk()
window.title()

window.geometry()

result_label = tk.Label(
    window,
    text="Click the button",
    bg="white",
    fg="black",
    font=("Arial", 14),
    wraplength=350,
    justify="center"
)

'''
title_label



input_entry

roll_button

exit_button

result

dice_number
'''
#Label()

#Button()

#pack()

#mainloop()