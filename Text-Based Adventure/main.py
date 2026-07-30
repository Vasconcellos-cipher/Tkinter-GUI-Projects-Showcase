import tkinter as tk

scenes = {
    "start": {
        "text": "You are searching for the legendary Gold Mine. Before you lies a choice:\nthe Dark Forest (dense and rough) or the Open Road (smooth, but suspiciously easy...)",
        "options": ["Enter the Dark Forest", "Take the Open Road"],
        "destinations": ["forest", "road"]
    },
    "forest": {
        "text": "The forest is dense. You reach a rushing river with an old rope bridge and a steep rocky trail beside it.",
        "options": ["Cross the rope bridge", "Climb the rocky trail"],
        "destinations": ["bridge_end", "victory"]
    },
    "road": {
        "text": "The road is suspiciously easy. Suddenly, you hear a click beneath your feet—a trapdoor with a lever right beside it!",
        "options": ["Pull the lever to disable the trap", "Jump over the trapdoor"],
        "destinations": ["lever_end", "victory"]
    },
    "bridge_end": {
        "text": "The bridge snaps! You fall into the river. GAME OVER.",
        "options": ["Play Again"],
        "destinations": ["start"]
    },
    "lever_end": {
        "text": "It was a trick! The lever opens the trapdoor beneath you. GAME OVER.",
        "options": ["Play Again"],
        "destinations": ["start"]
    },
    "victory": {
        "text": "You bypassed the danger and safely arrived at the Gold Mine! YOU WIN!",
        "options": ["Play Again"],
        "destinations": ["start"]
    }
}

current_scene_id = "start"

def make_choice(destination_id):
    """Updates the screen elements based on the player's choice."""
    global current_scene_id
    current_scene_id = destination_id
    
    scene = scenes[current_scene_id]
    
    story_label.config(text=scene["text"])

    button_1.config(
        text=scene["options"][0],
        command=lambda dest=scene["destinations"][0]: make_choice(dest)
    )
    
    if len(scene["options"]) > 1:
        button_2.config(
            text=scene["options"][1],
            command=lambda dest=scene["destinations"][1]: make_choice(dest)
        )
        button_2.pack(pady=5)  
    else:
        button_2.pack_forget()  

window = tk.Tk()
window.title("Text-Based Adventure")
window.geometry("500x350")

story_label = tk.Label(
    window, 
    text=scenes["start"]["text"], 
    font=("Arial", 11), 
    wraplength=450, 
    justify="center"
)
story_label.pack(pady=30)

button_1 = tk.Button(
    window, 
    text=scenes["start"]["options"][0], 
    width=35, 
    command=lambda dest=scenes["start"]["destinations"][0]: make_choice(dest)
)
button_1.pack(pady=5)

button_2 = tk.Button(
    window, 
    text=scenes["start"]["options"][1], 
    width=35, 
    command=lambda dest=scenes["start"]["destinations"][1]: make_choice(dest)
)
button_2.pack(pady=5)

# 4. Main Event Loop
window.mainloop()