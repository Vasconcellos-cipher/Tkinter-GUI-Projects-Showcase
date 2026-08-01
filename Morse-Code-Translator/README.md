# 📻 Morse Code Translator

A desktop GUI application built with **Python** and **Tkinter** that converts plain text strings into standard Morse code representation in real time.

This project was developed to practice **GUI layout setup**, **dictionary lookups**, **string manipulation**, **event handling**, and **dynamic label updating**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshots/morse_code_translator.png" width="400">
</p>

---

## ✨ Features

- 🖥️ Clean desktop interface built with Tkinter
- 🔤 Automatic text sanitization and normalization (`.strip().upper()`)
- 📻 Fast dictionary-driven Morse code lookups
- 📝 Responsive text display using word wrapping for longer output strings

---

## 🧠 System Algorithm

```text
User Types Text & Clicks 'Translate'

    │
    ▼

Fetch Input via entry_box.get()

    │
    ▼

Normalize String (.strip().upper())

    │
    ▼

Loop Through Characters

    │
    ▼

Is Character in MORSE_CODE_DICT?

    │
┌───┴───┐
│       │
Yes     No
│       │
▼       ▼

Append      Ignore /
Match       Skip
│           │
└─────┬─────┘
      │
      ▼

Join List with Spaces (" ".join())

    │
    ▼

Update Result Label via result_label.config()

```

### Logic Summary

1. The user inputs a text string into the `entry_box` and triggers `send_message()` by clicking `translate_button`.
2. The `text_to_morse()` function strips whitespace and converts characters to uppercase to match the dictionary keys.
3. It iterates through the string, appending mapped Morse representations into a list.
4. The list items are joined by spaces and passed back to update the `result_label`.

---

## 🛠️ Technologies

* Python 3
* Tkinter (`Tk`, `Entry`, `Button`, `Label`)

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/tkinter-gui-projects.git](https://github.com/yourusername/tkinter-gui-projects.git)

```

Go to the project folder:

```bash
cd tkinter-gui-projects/Morse-Code-Translator

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
Morse-Code-Translator/
│
├── assets/
│   └── screenshots/
│       └── morse_code_translator.png
│
├── .gitignore
├── README.md
├── requirements.txt
└── main.py

```

---

## 📝 Commit History Workflow

* `chore: setup project structure and morse code dictionary`
* `feat: add text to morse translation logic`
* `feat: connect GUI components to morse translator logic`
* `docs: add README for morse code translator project`

---

## 📚 Concepts Practiced

* Python dictionary lookups and error handling with `if in`
* String processing methods (`.strip()`, `.upper()`, `" ".join()`)
* Tkinter basic layout management using `.pack()`
* Event binding via button `command` callbacks
* Dynamic label content updates with `.config()`
