import json
import os
import tkinter as tk
from tkinter import messagebox, ttk

class MediaError(Exception):
    """Custom exception for media-related errors."""

    def __init__(self, message, obj):
        super().__init__(message)
        self.obj = obj

class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        super().__init__(title, year, director, duration)

        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

class MediaCatalogue:
    """A catalogue that stores media items and handles JSON persistence."""
    def __init__(self):
        self.items = []
        self.file_path = "catalogue.json"
        self.load_data()

    def add(self, media_item):
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)
        self.save_data()

    def remove(self, title):
        """Removes an item from the catalogue by its title."""
        initial_count = len(self.items)
        self.items = [item for item in self.items if item.title.lower() != title.lower()]
        if len(self.items) < initial_count:
            self.save_data()
            return True
        return False

    def get_movies(self):
        return [item for item in self.items if type(item) is Movie]

    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]

    def save_data(self):
        """Converts items into dictionaries and saves them to a JSON file."""
        data_to_save = []
        for item in self.items:
            item_dict = {
                "type": "Movie" if type(item) is Movie else "TVSeries",
                "title": item.title,
                "year": item.year,
                "director": item.director,
                "duration": item.duration
            }
            if isinstance(item, TVSeries):
                item_dict["seasons"] = item.seasons
                item_dict["total_episodes"] = item.total_episodes
            data_to_save.append(item_dict)
        
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)

    def load_data(self):
        """Loads data from JSON file and rebuilds the Movie/TVSeries objects."""
        if not os.path.exists(self.file_path):
            return
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item["type"] == "Movie":
                        obj = Movie(item["title"], item["year"], item["director"], item["duration"])
                    else:
                        obj = TVSeries(item["title"], item["year"], item["director"], item["duration"], item["seasons"], item["total_episodes"])
                    self.items.append(obj)
        except Exception:
            pass

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        movies = self.get_movies()
        series = self.get_tv_series()
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
            result += '\n'
        if series:
            result += '=== TV SERIES ===\n'
            for i, serie in enumerate(series, 1):
                result += f'{i}. {serie}\n'
        return result


class CatalogueApp:
    """GUI Application using Tkinter."""
    def __init__(self, root):
        self.root = root
        self.root.title("Media Catalogue System")
        self.root.geometry("650x550")
        self.catalogue = MediaCatalogue()

        # --- SEÇÃO DE EXIBIÇÃO ---
        self.lbl_title = tk.Label(root, text="Media Catalogue", font=("Arial", 16, "bold"))
        self.lbl_title.pack(pady=10)

        self.txt_display = tk.Text(root, width=75, height=15)
        self.txt_display.pack(pady=5)
        self.update_display()

        # --- SEÇÃO DE BUSCA E REMOÇÃO ---
        frame_search = tk.LabelFrame(root, text="Search & Remove Operations")
        frame_search.pack(pady=10, fill="x", padx=20)

        tk.Label(frame_search, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_search = tk.Entry(frame_search, width=30)
        self.ent_search.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(frame_search, text="Search", command=self.search_item, bg="#007BFF", fg="white").grid(row=0, column=2, padx=5, pady=5)
        tk.Button(frame_search, text="Remove", command=self.remove_item, bg="#DC3545", fg="white").grid(row=0, column=3, padx=5, pady=5)

        # --- SEÇÃO DE CADASTRO ---
        frame_add = tk.LabelFrame(root, text="Add New Media")
        frame_add.pack(pady=10, fill="x", padx=20)

        # Seleção de tipo (Filme ou Série)
        tk.Label(frame_add, text="Type:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_type = ttk.Combobox(frame_add, values=["Movie", "TV Series"], state="readonly", width=12)
        self.combo_type.current(0)
        self.combo_type.grid(row=0, column=1, padx=5, pady=5)
        self.combo_type.bind("<<ComboboxSelected>>", self.toggle_fields)

        # Campos Comuns
        tk.Label(frame_add, text="Title:").grid(row=1, column=0, padx=5, pady=5)
        self.ent_title = tk.Entry(frame_add, width=20)
        self.ent_title.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_add, text="Year:").grid(row=1, column=2, padx=5, pady=5)
        self.ent_year = tk.Entry(frame_add, width=8)
        self.ent_year.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame_add, text="Director/Creator:").grid(row=2, column=0, padx=5, pady=5)
        self.ent_director = tk.Entry(frame_add, width=20)
        self.ent_director.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_add, text="Duration (min):").grid(row=2, column=2, padx=5, pady=5)
        self.ent_duration = tk.Entry(frame_add, width=8)
        self.ent_duration.grid(row=2, column=3, padx=5, pady=5)

        # Campos exclusivos de Séries (inicialmente ocultos ou desativados)
        self.lbl_seasons = tk.Label(frame_add, text="Seasons:")
        self.lbl_seasons.grid(row=3, column=0, padx=5, pady=5)
        self.ent_seasons = tk.Entry(frame_add, width=8, state="disabled")
        self.ent_seasons.grid(row=3, column=1, padx=5, pady=5)

        self.lbl_episodes = tk.Label(frame_add, text="Episodes:")
        self.lbl_episodes.grid(row=3, column=2, padx=5, pady=5)
        self.ent_episodes = tk.Entry(frame_add, width=8, state="disabled")
        self.ent_episodes.grid(row=3, column=3, padx=5, pady=5)

        # Botão salvar
        tk.Button(frame_add, text="Save to Catalogue", command=self.save_item, bg="#28A745", fg="white", font=("Arial", 10, "bold")).grid(row=4, column=0, columnspan=4, pady=10)

    def toggle_fields(self, event):
        """Enables or disables seasons/episodes fields depending on selection."""
        if self.combo_type.get() == "TV Series":
            self.ent_seasons.config(state="normal")
            self.ent_episodes.config(state="normal")
        else:
            self.ent_seasons.config(state="disabled")
            self.ent_episodes.config(state="disabled")

    def update_display(self):
        """Refreshes the textbox with current catalogue data."""
        self.txt_display.config(state="normal")
        self.txt_display.delete("1.0", tk.END)
        self.txt_display.insert(tk.END, str(self.catalogue))
        self.txt_display.config(state="disabled")

    def save_item(self):
        """Reads entry fields, validates, and adds item to catalogue."""
        try:
            title = self.ent_title.get()
            year = int(self.ent_year.get())
            director = self.ent_director.get()
            duration = int(self.ent_duration.get())

            if self.combo_type.get() == "Movie":
                item = Movie(title, year, director, duration)
            else:
                seasons = int(self.ent_seasons.get())
                episodes = int(self.ent_episodes.get())
                item = TVSeries(title, year, director, duration, seasons, episodes)

            self.catalogue.add(item)
            self.update_display()
            messagebox.showinfo("Success", f"'{title}' added successfully!")
            self.clear_fields()

        except ValueError as e:
            messagebox.showerror("Validation Error", f"Invalid input values:\n{e}")
        except MediaError as e:
            messagebox.showerror("Catalogue Error", str(e))

    def search_item(self):
        """Searches for items matching the text query."""
        query = self.ent_search.get().lower()
        if not query:
            self.update_display()
            return

        results = [item for item in self.catalogue.items if query in item.title.lower()]
        
        self.txt_display.config(state="normal")
        self.txt_display.delete("1.0", tk.END)
        if results:
            self.txt_display.insert(tk.END, f"--- Search Results for '{query}' ---\n\n")
            for i, item in enumerate(results, 1):
                self.txt_display.insert(tk.END, f"{i}. {item}\n")
        else:
            self.txt_display.insert(tk.END, f"No media found matching '{query}'.")
        self.txt_display.config(state="disabled")

    def remove_item(self):
        """Removes item based on exact/partial title match."""
        title_to_remove = self.ent_search.get()
        if not title_to_remove:
            messagebox.showwarning("Warning", "Please type a title to remove.")
            return

        if self.catalogue.remove(title_to_remove):
            self.update_display()
            messagebox.showinfo("Success", f"'{title_to_remove}' removed from catalogue.")
            self.ent_search.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Could not find '{title_to_remove}' in the catalogue.")

    def clear_fields(self):
        self.ent_title.delete(0, tk.END)
        self.ent_year.delete(0, tk.END)
        self.ent_director.delete(0, tk.END)
        self.ent_duration.delete(0, tk.END)
        self.ent_seasons.delete(0, tk.END)
        self.ent_episodes.delete(0, tk.END)


# --- EXECUÇÃO DO APLICATIVO ---
# Substitua o final do seu código por isso no Colab:
if __name__ == "__main__":
    from pyvirtualdisplay import Display

    # Cria uma tela virtual invisível no servidor do Google
    display = Display(visible=0, size=(800, 600))
    display.start()

    root = tk.Tk()
    app = CatalogueApp(root)

    # Como o Colab não abre janelas físicas, usamos um update rápido
    # para simular o app ou testar se ele compila sem erros!
    root.update()
    print("A interface gráfica foi inicializada com sucesso na nuvem!")
    
    
#!apt-get install -y xvfb python3-tk
#!pip install pyvirtualdisplay
