import random
import tkinter as tk

frases = [
    "Great opportunities begin with small steps.",
    "Believe in yourself and success will follow.",
    "Today is a perfect day to learn something new.",
    "Patience and persistence always pay off.",
    "Every challenge is a chance to grow.",
    "A positive mindset opens many doors.",
    "Your hard work will bring great results.",
    "Good things come to those who never give up.",
    "Stay curious, and amazing things will happen.",
    "The future belongs to those who keep learning."
]

def abrir_biscoito():
    frase = random.choice(frases)
    frase_label.config(text=frase)

janela = tk.Tk()
janela.title("Fortune Cookie")
janela.geometry("500x350")
janela.configure(bg="black")
janela.resizable(False, False)
frase_label = tk.Label(
    janela,
    text="Click the button",
    bg="white",
    fg="black",
    font=("Arial", 14),
    wraplength=350,
    justify="center"
)

frase_label.pack(pady=70)

botao = tk.Button(
    janela,
    text="🥠 Open Fortune Cookie",
    command=abrir_biscoito,
    cursor="hand2",
    font=("Arial", 11, "bold")
)

botao.pack(pady=20)

janela.mainloop()
