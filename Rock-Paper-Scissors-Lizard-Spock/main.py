import random
import tkinter as tk


choices = [
    "Rock",
    "Paper",
    "Scissors",
    "Lizard",
    "Spock"
]

wins = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Rock", "Scissors"]
}


game_mode = None
player1_choice = None


def check_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"

    elif choice2 in wins[choice1]:
        return "Player 1 Wins"

    else:
        return "Player 2 Wins"


def select_mode(mode):
    global game_mode
    global player1_choice

    game_mode = mode
    player1_choice = None

    result_label.config(text="")

    if mode == "computer":
        player2_entry.config(state="disabled")
        status_label.config(
            text="Player 1, choose your option."
        )

    else:
        player2_entry.config(state="normal")
        status_label.config(
            text="Player 1, choose your option."
        )


def play(choice):
    global player1_choice

    if game_mode is None:
        status_label.config(
            text="Choose a game mode first."
        )
        return

    player1_name = player1_entry.get().strip()

    if player1_name == "":
        player1_name = "Player 1"

    if game_mode == "computer":
        opponent_name = "Computer"
        opponent_choice = random.choice(choices)

        show_result(
            player1_name,
            choice,
            opponent_name,
            opponent_choice
        )

    else:
        player2_name = player2_entry.get().strip()

        if player2_name == "":
            player2_name = "Player 2"

        if player1_choice is None:
            player1_choice = choice

            status_label.config(
                text=f"{player2_name}, choose your option."
            )

            result_label.config(
                text=f"{player1_name} has already chosen."
            )

        else:
            show_result(
                player1_name,
                player1_choice,
                player2_name,
                choice
            )

            player1_choice = None


def show_result(name1, choice1, name2, choice2):
    result = check_winner(choice1, choice2)

    if result == "Player 1 Wins":
        winner = f"{name1} Wins!"

    elif result == "Player 2 Wins":
        winner = f"{name2} Wins!"

    else:
        winner = "Draw!"

    result_label.config(
        text=(
            f"{name1}: {choice1}\n"
            f"{name2}: {choice2}\n\n"
            f"{winner}"
        )
    )

    status_label.config(
        text="Choose an option to play again."
    )


window = tk.Tk()
window.title("Rock Paper Scissors Lizard Spock")
window.geometry("700x550")
window.configure(bg="white")
window.resizable(False, False)


title_label = tk.Label(
    window,
    text="Rock Paper Scissors Lizard Spock",
    bg="white",
    fg="black",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)


player1_label = tk.Label(
    window,
    text="Player 1 Name:",
    bg="white"
)

player1_label.pack()


player1_entry = tk.Entry(
    window,
    width=30,
    justify="center"
)

player1_entry.pack(pady=5)


player2_label = tk.Label(
    window,
    text="Player 2 Name:",
    bg="white"
)

player2_label.pack()


player2_entry = tk.Entry(
    window,
    width=30,
    justify="center"
)

player2_entry.pack(pady=5)


mode_label = tk.Label(
    window,
    text="Choose opponent:",
    bg="white",
    font=("Arial", 12, "bold")
)

mode_label.pack(pady=(15, 5))


mode_frame = tk.Frame(
    window,
    bg="white"
)

mode_frame.pack(pady=5)


computer_button = tk.Button(
    mode_frame,
    text="Player vs Computer",
    command=lambda: select_mode("computer")
)

computer_button.pack(
    side="left",
    padx=5
)


player_button = tk.Button(
    mode_frame,
    text="Player vs Player",
    command=lambda: select_mode("player")
)

player_button.pack(
    side="left",
    padx=5
)


status_label = tk.Label(
    window,
    text="Choose a game mode first.",
    bg="white",
    font=("Arial", 12)
)

status_label.pack(pady=20)


choices_frame = tk.Frame(
    window,
    bg="white"
)

choices_frame.pack(pady=10)


for choice in choices:
    choice_button = tk.Button(
        choices_frame,
        text=choice,
        width=10,
        command=lambda selected_choice=choice: play(
            selected_choice
        )
    )

    choice_button.pack(
        side="left",
        padx=5
    )


result_label = tk.Label(
    window,
    text="",
    bg="white",
    fg="black",
    font=("Arial", 14, "bold"),
    justify="center"
)

result_label.pack(pady=25)


window.mainloop()