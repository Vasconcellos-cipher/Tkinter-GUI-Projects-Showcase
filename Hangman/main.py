import random

WORDS = ["PYTHON", "JAVASCRIPT", "DEVELOPER", "TKINTER", "DATABASE"]

def get_display_word(secret_word, guessed_letters):
    
    display = []
    
    for i in secret_word:
        if i in guessed_letters:
            display.append(i)
        else:
            display.append("_")
            
    return " ".join(display)
        
palavra = random.choice(WORDS)
chutes = ["P", "Y"]

print(get_display_word(palavra, chutes))