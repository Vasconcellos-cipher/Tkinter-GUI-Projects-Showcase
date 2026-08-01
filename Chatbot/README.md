# 💬 PyBot - Tkinter Chatbot

A desktop GUI application built with **Python** and **Tkinter** featuring an interactive rule-based chatbot with scrollable conversation history.

This project was developed to practice **GUI development**, **text widget manipulation**, **event handling**, **dictionary lookups**, **string sanitization**, and **clean project architecture**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshots/chatbot.png" width="400">
</p>

---

## ✨ Features

- 🖥️ Desktop graphical interface built with Tkinter
- 📜 Scrollable chat history using `ScrolledText`
- 🤖 Rule-based keyword matching with fallback responses
- 🧹 Automatic input field clearing after message dispatch
- 💬 Clean message formatting separating user and bot turns

---

## 🧠 System Algorithm

```text
User Enters Text & Clicks 'Send'

    │
    ▼

Fetch Input via entry_box.get()

    │
    ▼

Is the Message Non-Empty?

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Sanitize String        Ignore Action
(.strip().lower())
    │
    ▼

Search Key in Responses Dictionary

    │
┌───┴───┐
│       │
Found   Not Found
│       │
▼       ▼

Return      Return Default
Match       Fallback Text
    │           │
    └─────┬─────┘
          │
          ▼

Append Both Messages to chat_history (.insert())

    │
    ▼

Clear Input Field (.delete(0, tk.END))

```

### Logic Summary

1. User types a prompt into `entry_box` and triggers the `send_message()` callback via `send_button`.
2. The system retrieves the text string using `.get()` and strips whitespace while lowering case for normalization.
3. The cleaned string is checked against the keys in the `responses` dictionary.
4. If a match exists, the associated response string is returned; otherwise, a default fallback message is served.
5. Both the user input and bot response are appended to `chat_history` via `.insert(tk.END, ...)` before clearing `entry_box` with `.delete(0, tk.END)`.

---

## 🛠️ Technologies

* Python 3
* Tkinter (`scrolledtext`, `Entry`, `Button`, `Tk`)

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/tkinter-gui-projects.git](https://github.com/yourusername/tkinter-gui-projects.git)

```

Go to the project folder:

```bash
cd tkinter-gui-projects/chatbot

```

Create a virtual environment (optional):

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate

```

Run the application:

```bash
python main.py

```

---

## 📂 Project Structure

```text
chatbot/
│
├── assets/
│   └── screenshots/
│       └── chatbot.png
│
├── .gitignore
├── README.md
└── main.py

```

---

## 📝 Commit History Workflow

This project followed conventional commits across its development cycle:

* `chore: setup project structure and venv for chatbot`
* `feat: create chatbot response logic and dictionary`
* `feat: build base tkinter layout for chatbot`
* `feat: connect user input and message display`
* `docs: add README for chatbot project`

---

## 📚 Concepts Practiced

* String processing (`.strip()`, `.lower()`)
* Dictionary state lookups with default fallbacks
* Tkinter layout elements (`Tk`, `ScrolledText`, `Entry`, `Button`)
* Event handling using `command` callbacks
* Text insertion and clearing (`.insert()`, `.delete()`)
* Conventional Git commit patterns and workspace isolation (`venv`)

---

## 🎯 Learning Objectives

This project was created to reinforce Python GUI fundamentals by building a functional desktop messaging layout.

The core focus was connecting user input widgets to dictionary-driven evaluation functions and rendering dynamic updates inside scrollable text views.
