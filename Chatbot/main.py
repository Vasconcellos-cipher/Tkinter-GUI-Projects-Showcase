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
    
# Teste temporário no terminal:
print(get_bot_response("Hello"))
print(get_bot_response("what is your name"))
print(get_bot_response("qualquer coisa que nao existe"))