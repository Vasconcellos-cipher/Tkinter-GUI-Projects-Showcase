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
    print(frase)

abrir_biscoito()