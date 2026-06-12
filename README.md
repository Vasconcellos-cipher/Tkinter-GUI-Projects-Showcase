# Tkinter GUI Projects Showcase

Welcome to my repository dedicated to desktop applications built using **Python** and **Tkinter**. This space showcases professional, interactive, and robust graphical user interfaces (GUIs) integrated with core Software Engineering and Object-Oriented Programming (OOP) principles.

This repository serves as my personal practical laboratory for my studys roadmap, bridging foundational software logic with future cybersecurity and DevSecOps automations.

## 🚀 Key Features Demonstrated

* **Object-Oriented Programming (OOP):** Deep utilization of inheritance, polymorphism, and encapsulation to build scalable application architectures.
* **Data Persistence:** Storing, reading, and writing application states seamlessly using **JSON** databases.
* **Robust Error Handling:** Implementation of data validation using `try/except` blocks and **custom exceptions** to guarantee an excellent user experience without crashes.
* **Event-Driven Architecture:** Creating highly responsive applications based on user clicks, selections, and inputs.

---

## ✅ Completed Projects

### 📂 Media Catalogue System (`movie_and_series_catalog.py`)

This is the flagship project of the repository. It is a fully functional **Desktop Media Catalogue** that allows users to manage a local database of movies and TV series using an elegant, crash-proof window application.

* **Tech Stack:** Python 3, Tkinter & TTK (modern widgets), JSON (File-based local persistence).
* **Core Architecture:**
1. `Movie` & `TVSeries`: Model classes handling encapsulation and strict data validation (e.g., preventing negative durations or empty fields).
2. `MediaCatalogue`: The controller layer operating sorting/filtering algorithms and managing JSON serialization.
3. `CatalogueApp`: The GUI view layer built with Tkinter, featuring reactive layouts and contextual fields.



---

## 🛠️ How to Run Locally

Since Tkinter is a native Python library, you don't need to install external GUI dependencies. However, you need a local graphical environment (desktop monitor) to render the windows.

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Execution Steps

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)

# 2. Navigate to the project folder
cd YOUR_REPO_NAME

# 3. Run the completed application
python movie_and_series_catalog.py

```

*Note: Running this inside cloud environments without a display server (like GitHub Codespaces) will throw a `$DISPLAY` environment error. Run it on your local machine.*

---

## 💡 Developer Notes & Best Practices for File Architecture

To keep my studies organized and maintain a clean repository, all upcoming projects are designed to be contained within a **single standalone file** per application. This approach ensures code portability and easy review.

Every project in this roadmap strictly follows this professional top-to-bottom template layout inside its file:

```python
# ==========================================
# 1. IMPORTS
# ==========================================
import json
import tkinter as tk
from tkinter import ttk, messagebox
# Project-specific modules (like hashlib, socket, or paramiko) go here

# ==========================================
# 2. LOGIC LAYER (The "Back-End")
# ==========================================
class MediaError(Exception): 
    pass

class Produto: # Or Host, User, etc., depending on the project
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    # Data validation and core logical methods go here

# ==========================================
# 3. GUI VIEW LAYER (The "Front-End")
# ==========================================
class InterfaceApp:
    def __init__(self, root):
        self.root = root
        # GUI construction components (buttons, text fields, tables)
        
    def salvar_dados(self):
        # Functions connecting GUI elements to the logic layer above
        pass

# ==========================================
# 4. APPLICATION RUNNER
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()

```

---

## 🔮 Future Projects (Python & GUI Roadmap)

I am utilizing my next weeks of Python studies to build and add the following 12 projects to this GUI portfolio, moving from foundational programming to advanced security automation:

### 🛍️ General Programming & Core Logic (Getting Started)

* [ ] **Mini Local Marketplace:** A store management app to register products, prices, and dynamically decrease stock levels with a "Sell" button.
* [ ] **Daily Habit Tracker:** A personal routine assistant using Tkinter `Checkbuttons` and a `ttk.Progressbar` that updates as goals are completed.
* [ ] **Personal Finance Budgeter:** An expense tracker that categorizes spending and dynamically changes UI colors (Green/Yellow/Red) based on budget limits.

### 🌐 Network Security & Reconnaissance

* [ ] **Visual Port Scanner:** A multi-threaded network scanner using Python `socket` to map open ports and services into a `ttk.Treeview` table.
* [ ] **IP & Subnet Calculator:** A utility utilizing the `ipaddress` module to visually calculate network boundaries, broadcast IPs, and valid host ranges.

### 🔐 Cryptography & Data Protection

* [ ] **Hash Generator & Verifier:** An integrity tool using `hashlib` to compute and match file hashes (MD5, SHA-256) to detect tampering.
* [ ] **Text Encrypter/Decrypter:** A secure notepad that implements symmetric AES encryption via the `cryptography` library.
* [ ] **Secure Password Manager:** An advanced local coffer that encrypts stored credentials inside a JSON file using a master password.

### 🚀 DevSecOps Automation & Log Analysis

* [ ] **SSH Remote Command Runner:** An infrastructure tool powered by `paramiko` to safely execute administrative commands on remote Linux servers.
* [ ] **Vulnerability Report Dashboard:** A DevSecOps triage tool that parses complex JSON outputs from security scanners (like Trivy or OWASP ZAP) into a color-coded severity dashboard.
* [ ] **Log Monitor & Alert System:** A lightweight visual SIEM that reads server logs in real-time and flashes red alerts upon detecting malicious traffic patterns.
* [ ] **Phishing Link Analyzer:** A defense utility that uses regular expressions to analyze suspicious URLs for malicious patterns and shortening services.
