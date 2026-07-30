# 🎮 Who Wants to Be a Millionaire

A desktop GUI application built with **Python** and **Tkinter** featuring a trivia quiz game inspired by **Who Wants to Be a Millionaire**.

This project was developed to practice **GUI development**, **functions**, **conditional logic**, **dictionaries**, **lists**, **event-driven programming**, and **code organization**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshot.png" width="700">
</p>
<p align="center">
  <img src="assets/screenshot2.png" width="700">
</p>
<p align="center">
  <img src="assets/screenshot3.png" width="700">
</p>

---

## ✨ Features

- 🖥️ Desktop graphical interface built with Tkinter
- ❓ Multiple-choice trivia questions
- 🎯 Real-time answer validation
- 📊 Dynamic score tracking
- 🔄 Automatic question progression
- 🏆 End-of-game summary screen
- 🧼 Clean and intuitive interface

---

## 🧠 Game Algorithm

```text
Start Quiz

    │
    ▼

Load Question & Options

    │
    ▼

Player selects an Option

    │
    ▼

Is the choice correct?

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Score +1   No points added

    │
    ▼

Are there more questions?

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Load Next   Display Final Score
Question        & Game Over

```

### Logic Summary

1. The game loads the current question and options from a list of dictionaries.
2. The user clicks a button to submit their answer.
3. The program checks if the chosen option matches the correct answer key.
4. If correct, the score is incremented and a success message is displayed.
5. If incorrect, the correct answer is revealed.
6. The game advances to the next index until all questions are answered, then displays the total score.

---

## 🛠️ Technologies

* Python 3
* Tkinter

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/Who-Wants-to-Be-a-Millionaire.git](https://github.com/yourusername/Who-Wants-to-Be-a-Millionaire.git)

```

Go to the project folder:

```bash
cd Who-Wants-to-Be-a-Millionaire

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
Who-Wants-to-Be-a-Millionaire/
│
├── assets/
│   └── screenshot.png
│
├── README.md
├── main.py
├── requirements.txt
└── .gitignore

```

---

## 📚 Concepts Practiced

* Functions
* Function parameters
* Return values
* Conditional statements (`if`, `elif`, `else`)
* Lists
* Dictionaries
* Index manipulation
* Tkinter
* Labels
* Buttons
* Event-driven programming
* GUI application development
* Code organization

---

## 🎯 Learning Objectives

This project was created to reinforce Python programming fundamentals while building a practical desktop application.

The main focus was to improve logical thinking by structuring structured data inside dictionaries and dynamically updating a Tkinter user interface based on user actions.
