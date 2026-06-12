# Tkinter GUI Projects Showcase

Welcome to my repository dedicated to desktop applications built using **Python** and **Tkinter**. This space showcases professional, interactive, and robust graphical user interfaces (GUIs) integrated with core Software Engineering principles.

## 🚀 Key Features Demonstrated
* **Object-Oriented Programming (OOP):** Deep utilization of inheritance, polymorphism, and encapsulation to build scalable application architectures.
* **Data Persistence:** Storing, reading, and writing application states seamlessly using **JSON** databases.
* **Robust Error Handling:** Implementation of data validation using `try/except` blocks and **custom exceptions** to guarantee an excellent user experience without crashes.
* **Event-Driven Architecture:** Creating highly responsive applications based on user clicks, selections, and inputs.

---

## 📂 Featured Project: Media Catalogue System

The flagship project in this repository is a **Desktop Media Catalogue**. It allows users to manage a database of movies and TV series using an elegant and crash-proof window application.

### Tech Stack
* **Language:** Python 3
* **GUI Framework:** Tkinter & TTK (for modern widgets)
* **Database:** JSON (File-based local persistence)

### Core Architecture
The system separates the business logic from the visual presentation layer:
1.  **`Movie` & `TVSeries`:** Model classes handling encapsulation and strict data validation (e.g., preventing negative durations or empty fields).
2.  **`MediaCatalogue`:** The controller layer that operates filtering algorithms (separating direct parent classes from child subclasses) and manages JSON serialization/deserialization.
3.  **`CatalogueApp`:** The GUI view layer built with Tkinter, utilizing reactive grid layouts and contextual entry fields (fields activate or deactivate depending on whether you are registering a Movie or a TV Series).

---

## 🛠️ How to Run Locally

Since Tkinter is a native Python library, you don't need to install external GUI dependencies. However, you need a local graphical environment (desktop monitor) to render the windows.

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Execution Steps
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
