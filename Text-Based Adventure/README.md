# 🎮 Text-Based Adventure

A desktop GUI application built with **Python** and **Tkinter** featuring an interactive decision-based story game where choices determine the outcome.

This project was developed to practice **GUI development**, **functions**, **state management**, **dictionaries**, **nested data structures**, **event-driven programming**, and **code organization**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshots/text-based-adventure.png" width="700">
</p>feat: build interactive text-based adventure GUI with Tkinter

---

## ✨ Features

- 🖥️ Desktop graphical interface built with Tkinter
- 📜 Dynamic story rendering based on player choices
- 🔀 Branching narrative paths with multiple outcomes
- 🔄 Replayable game loop (Play Again functionality)
- 👁️ Dynamic UI adjustments (hides unused buttons on end screens)
- 🧼 Clean and intuitive interface

---

## 🧠 Game Algorithm

```text
Start Game

    │
    ▼

Load Scene Data (Text & Options)

    │
    ▼

Player Clicks a Choice Button

    │
    ▼

Retrieve Destination ID

    │
    ▼

Is it a Final Scene? (Victory / Game Over)

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Show 'Play Again'   Update Text &
Button Only         Load Next Options
    │                   │
    └─────────┬─────────┘
              │
              ▼

Wait for Player Action

```

### Logic Summary

1. The game initializes at the `"start"` scene using a nested dictionary structure.
2. The UI dynamically displays the scene description and configures choice buttons based on available options.
3. When a player clicks a button, the system fetches the destination key from the scene's data.
4. If the destination leads to a game over or victory screen, secondary buttons are hidden using `.pack_forget()`, leaving only a restart option.
5. Clicking restart resets the scene pointer back to `"start"`.

---

## 🛠️ Technologies

* Python 3
* Tkinter

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/tkinter-gui-projects.git](https://github.com/yourusername/tkinter-gui-projects.git)

```

Go to the project folder:

```bash
cd tkinter-gui-projects/Text-Based-Adventure

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

Install dependencies:

```bash
pip install -r requirements.txt

```

Run the application:

```bash
python main.py

```

---

## 📂 Project Structure

```text
Text-Based-Adventure/
│
├── assets/
│   └── screenshots/
│       └── text-based-adventure.png
│
├── README.md
├── main.py
├── requirements.txt
└── .gitignore

```

---

## 📚 Concepts Practiced

* Functions and argument passing
* Lambda functions with default arguments
* Conditional logic (`if`, `else`)
* Dictionaries and nested structures
* State tracking across UI events
* Tkinter Layout Management (`.pack()`, `.pack_forget()`)
* Dynamic Widget Configuration (`.config()`)
* Event-driven programming
* GUI application architecture

---

## 🎯 Learning Objectives

This project was created to reinforce Python programming fundamentals while building a practical desktop application.

The main focus was to manage application state using data structures (nested dictionaries) to drive UI changes dynamically without hardcoding layout transitions.

