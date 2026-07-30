import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the largest planet in the Solar System?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "Paris", "Rome", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "How many chemical elements are currently in the periodic table?",
        "options": ["108", "118", "128", "98"],
        "answer": "118"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "Vincent van Gogh",
            "Leonardo da Vinci",
            "Pablo Picasso",
            "Claude Monet"
        ],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the fastest land animal?",
        "options": [
            "Cheetah",
            "Lion",
            "Antelope",
            "Peregrine Falcon"
        ],
        "answer": "Cheetah"
    }
]

current_question_index = 0
score = 0

def check_answer(user_choice):
    global current_question_index, score
    
    current_question = questions[current_question_index]
    correct_answer = current_question["answer"]
    
    if user_choice == correct_answer:
        score += 1
        messagebox.showinfo("Result", "✨ Congratulations! Correct answer!")
    else:
        messagebox.showerror("Result", f"❌ Incorrect!\nThe correct answer was: {correct_answer}")
    
    current_question_index += 1
    
    if current_question_index < len(questions):
        load_question()
    else:
        messagebox.showinfo("End of quiz", f"Game over!\nYou got {score} out of {len(questions)} questions right.")
        window.destroy()

def load_question():
    current_question = questions[current_question_index]
    
    question_text = current_question["question"]
    options = current_question["options"]
    
    question_label.config(text=f"question {current_question_index + 1} de {len(questions)}:\n\n{question_text}")
    
    for i in range(4):
        option_text = options[i]
        option_buttons[i].config(
            text=option_text,
            command=lambda opt=option_text: check_answer(opt)
        )


window = tk.Tk()
window.title("Who wants to be a millionaire")
window.geometry("500x380")
window.resizable(False, False)

question_label = tk.Label(
    window, 
    text="", 
    font=("Arial", 11, "bold"), 
    wraplength=460, 
    justify="center"
)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(
        window, 
        text="", 
        font=("Arial", 10), 
        width=38, 
        height=2
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

load_question()
window.mainloop()