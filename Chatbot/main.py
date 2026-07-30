import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm just a Python script, but I'm doing great! How about you?",
    "what is your name": "I am PyBot, your friendly Tkinter assistant!",
    "help": "I can chat with you! Try saying 'hello', asking my name, or asking for a joke.",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't quite understand that. Can you rephrase?"
}

def get_bot_response(user_message):
    clean_message = user_message.strip().lower()
    
    if clean_message in responses:
        return responses[clean_message] 
    else:
        return responses["default"]
    
def send_message():
    user_text = entry_box.get()
    
    bot_text = get_bot_response(user_text)
    chat_history.insert(tk.END, "You: " + user_text + "\n")
    chat_history.insert(tk.END, "PyBot: " + bot_text + "\n\n")
    
    entry_box.delete(0, tk.END)

window = tk.Tk()
window.title("PyBot - Chatbot")
window.geometry("400x500")

chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, state="normal", width=45, height=20)
chat_history.pack(padx=10, pady=10)

entry_box = tk.Entry(window, width=35)
entry_box.pack(pady=5)


send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()