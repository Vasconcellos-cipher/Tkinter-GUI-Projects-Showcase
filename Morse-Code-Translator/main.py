import tkinter as tk

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

def text_to_morse(text):
    translator_message = text.strip().upper()
    peaces_morse = []
    
    for i in translator_message:
        if i in MORSE_CODE_DICT:
            peaces_morse.append(MORSE_CODE_DICT[i])
        
    return " ".join(peaces_morse)

def send_message():
    user_text = entry_box.get()
    morse_result = text_to_morse(user_text)
    result_label.config(text=morse_result)

window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x500")

entry_box = tk.Entry(window, width=35)
entry_box.pack(pady=20)

translate_button = tk.Button(window, text="Translate", command=send_message)
translate_button.pack(pady=5)

result_label = tk.Label(window, text="Your Morse code will appear here", font=("Arial", 14), wraplength=350)
result_label.pack(pady=20)

window.mainloop()