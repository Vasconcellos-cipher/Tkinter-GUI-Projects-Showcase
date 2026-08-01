import random
import tkinter as tk

truths = [
    "What is your biggest fear?",
    "Have you ever lied to a friend?",
    "What is your dream job?"
]

dares = [
    "Do 10 push-ups.",
    "Sing your favorite song.",
    "Dance for 30 seconds."
]

def update_result(text):
    result_label.config(text=text)

def show_truth():
    question = random.choice(truths)
    update_result(question)
    
def show_dare():
    challenge = random.choice(dares)
    update_result(challenge)

window = tk.Tk()

window.title("Truth or Dare")
window.geometry("500x400")

title = tk.Label(
    window,
    text="Truth or Dare",
    font=("Arial", 24, "bold"),
    bg="#2C3E50",
    fg="white"
)

title.pack(pady=20)


result_label = tk.Label(
    window,
    text="Choose Truth or Dare",
    font=("Arial", 16),
    wraplength=400,
    bg="#2C3E50",
    fg="white"
)

result_label.pack(pady=30)

truth_button = tk.Button(
    window,
    text="Truth",
    width=20,
    bg="#27AE60",
    fg="white",
    command=show_truth
)

dare_button = tk.Button(
    window,
    text="Dare",
    width=20,
    bg="#E74C3C",
    fg="white",
    command=show_dare
)

window.configure(bg="#2C3E50")

dare_button.pack(pady=10)

truth_button.pack(pady=10)



window.mainloop()