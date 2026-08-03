# 🪓 Hangman Game

A classical desktop **Hangman** game built with **Python** and **Tkinter**, using `tk.Canvas` to dynamically render the hangman structure and stickman figure as errors accumulate.

This project was developed to practice **GUI layout design**, **Canvas shape creation**, **game state management**, and **interactive event handling**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshots/hangman.png" width="400">
</p>

---

## ✨ Features

- 🖥️ Desktop GUI interface built using Tkinter
- 🎨 Dynamic 2D rendering using `tk.Canvas` (`create_line`, `create_oval`)
- 🔤 Real-time letter normalization (`.strip().upper()`)
- ⚠️ Win/Loss detection with `messagebox` feedback and button disabling

---

## 🧠 Game Logic Flow

```text
User Enters Letter & Clicks 'Guess'

    │
    ▼

Normalize Input (.strip().upper())

    │
    ▼

Is Letter Valid & Unused?

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Add to      Ignore
kicks List
│
▼

Is Letter in Word?

    │
┌───┴─────────────┐
│                 │
Yes               No
│                 │
▼                 ▼

Update Display    Calculate Wrong Guesses
Word Label        & Draw Body Part on Canvas
│                 │
▼                 ▼

Check Win:        Check Loss:
No '_' left?      Errors == 6?
│                 │
▼                 ▼

Show Win Dialog   Show Game Over Dialog
& Disable Button  & Disable Button

```

---

## 🛠️ Technologies

* Python 3
* Tkinter (`Tk`, `Canvas`, `Label`, `Entry`, `Button`, `messagebox`)
* Standard library modules (`random`)

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/tkinter-gui-projects.git](https://github.com/yourusername/tkinter-gui-projects.git)

```

Go to the project folder:

```bash
cd tkinter-gui-projects/Hangman

```

Create a virtual environment:

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
Hangman/
│
├── assets/
│   └── hangman.png
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py

```

---

## 📝 Commit History Workflow

* `chore: setup project structure and venv for hangman`
* `feat: add secret word progress logic for hangman`
* `feat: implement GUI layout and Canvas stickman rendering`
* `docs: add README for hangman project`

---

## 📚 Concepts Practiced

* Dynamic 2D vector drawing using `tk.Canvas` coordinates ($X, Y$)
* Tracking game states with lists and string manipulation
* Dialogue feedback pop-ups using `tkinter.messagebox`
* Disabling GUI controls dynamically with `.config(state="disabled")`

```


