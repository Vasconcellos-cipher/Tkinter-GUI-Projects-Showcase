import random
import tkinter as tk
from tkinter import messagebox

WORDS = ["PYTHON", "JAVASCRIPT", "DEVELOPER", "TKINTER", "DATABASE"]

def get_display_word(secret_word, guessed_letters):
    display = []
    for i in secret_word:
        if i in guessed_letters:
            display.append(i)
        else:
            display.append("_")
            
    return " ".join(display)

def draw_body_part(wrong_count):
    if wrong_count == 1:
        # Head (Oval) -> (x1, y1, x2, y2)
        canvas.create_oval(115, 50, 145, 80, width=3)
    elif wrong_count == 2:
        # Torso / Body (Line)
        canvas.create_line(130, 80, 130, 140, width=3)
    elif wrong_count == 3:
        # Left Arm
        canvas.create_line(130, 100, 105, 120, width=3)
    elif wrong_count == 4:
        # Right Arm
        canvas.create_line(130, 100, 155, 120, width=3)
    elif wrong_count == 5:
        # Left Leg
        canvas.create_line(130, 140, 110, 180, width=3)
    elif wrong_count == 6:
        # Right Leg
        canvas.create_line(130, 140, 150, 180, width=3)

def make_guess():
    letter = entry_letter.get().strip().upper()  
    entry_letter.delete(0, tk.END)                
    
    if letter and letter not in kicks:
        kicks.append(letter)
        
        if letter not in word:
            wrong_guesses = [k for k in kicks if k not in word]
            draw_body_part(len(wrong_guesses))
            
            if len(wrong_guesses) == 6:
                messagebox.showinfo("Game Over", f"You lose! The word was: {word}")
                btn_guess.config(state="disabled")
        else:
            display_word = get_display_word(word, kicks)
            word_label.config(text=display_word)
            
            if "_" not in display_word:
                messagebox.showinfo("Congratulations!", "You won!")
                btn_guess.config(state="disabled")

window = tk.Tk()
window.title("Hangman")

canvas = tk.Canvas(window, width=200, height=250, bg="white")
canvas.pack(pady=10)

word = random.choice(WORDS)
kicks = []  

word_label = tk.Label(window, text=get_display_word(word, kicks), font=("Consolas", 18, "bold"))
word_label.pack(pady=20)

# Input
entry_letter = tk.Entry(window, width=5, font=("Consolas", 14), justify="center")
entry_letter.pack(pady=5)

# Kick button 
btn_guess = tk.Button(window, text="Guess", font=("Arial", 12), command=make_guess)
btn_guess.pack(pady=5)

# Fixed hangman design
canvas.create_line(20, 230, 180, 230, width=4)   # Floor
canvas.create_line(50, 230, 50, 20, width=4)     # Vertical Post
canvas.create_line(50, 20, 130, 20, width=4)     # Top Rail
canvas.create_line(130, 20, 130, 50, width=2)    # String

window.mainloop()