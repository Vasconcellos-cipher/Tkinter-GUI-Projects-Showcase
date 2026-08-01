# 🎯 Truth or Dare Game

A simple and colorful desktop party game built with **Python** and **Tkinter** that randomly selects truths and dares at the click of a button.

This project was developed to practice **GUI layout design**, **randomized data selection**, **widget re-configuration**, and **event-driven programming**.

---

## 📸 Screenshot

<p align="center">
  <img src="assets/screenshots/truth_or_dare.png" width="400">
</p>

---

## ✨ Features

- 🎨 Custom dark theme layout (`#2C3E50`) with color-coded buttons
- 🎲 Random selection of Truths and Dares using Python's `random` module
- 📝 Dynamic text updates without recreating UI widgets
- 📱 Responsive text wrapping (`wraplength=400`) for longer questions/challenges

---

## 🧠 System Algorithm

```text
User Clicks 'Truth' or 'Dare' Button

    │
    ▼

Trigger Callback (show_truth / show_dare)

    │
    ▼

Select Random Item via random.choice()

    │
    ▼

Pass Selected Text to update_result()

    │
    ▼

Re-configure Label: result_label.config(text=text)

```

### Logic Summary

1. When the user clicks either the **Truth** or **Dare** button, the corresponding event handler (`show_truth()` or `show_dare()`) is executed.
2. The handler picks a random string from the respective list using Python's `random.choice()`.
3. The selected string is passed to `update_result()`, which updates the existing `result_label` using `.config(text=...)`.

---

## 🛠️ Technologies

* Python 3
* Tkinter (`Tk`, `Label`, `Button`)
* `random` module

---

## 🚀 How to Run

Clone the repository:

```bash
git clone [https://github.com/yourusername/tkinter-gui-projects.git](https://github.com/yourusername/tkinter-gui-projects.git)

```

Go to the project folder:

```bash
cd tkinter-gui-projects/truth_or_dare

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
truth_or_dare/
│
├── assets/
│   └── screenshots/
│       └── truth_or_dare.png
│
├── .gitignore
├── README.md
└── main.py

```

---

## 📝 Commit History Workflow

* `chore: setup project structure and venv for truth_or_dare`
* `feat: build truth or dare game layout and selection logic`
* `docs: add README for truth or dare project`

---

## 📚 Concepts Practiced

* Dynamic label modification using `.config()`
* Working with list data and the `random` standard library
* Configuring widget colors (`bg`, `fg`), fonts, and padding (`pady`)
* Clean event binding through `command` parameters
* Conventional Git commit practices