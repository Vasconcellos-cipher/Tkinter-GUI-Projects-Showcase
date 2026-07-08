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

def check_winner(choice1, choice2):
    
    if choice1 == choice2:
        return "Draw"
    
    elif choice2 in wins[choice1]:
        return "Player 1 Wins"

    else:
        return "Player 2 Wins"
    
def choose_your_player():

    mode = input("Choose opponent (1 - Computer | 2 - Player 2): ")

    if mode == "1":

        opponent_name = "Computer"
        opponent_choice = random.choice(choices)

    elif mode == "2":

        opponent_name = input("Player 2 name: ")
        opponent_choice = input(
            "Player 2 choice (Rock/Paper/Scissors/Lizard/Spock): "
        ).capitalize()

    else:
        print("Invalid option.")
        return None, None

    return opponent_name, opponent_choice

print("=== Rock Paper Scissors Lizard Spock ===\n")

player1_name = input("Player 1 name: ")
player1_choice = input(
    "Player 1 choice (Rock/Paper/Scissors/Lizard/Spock): "
).capitalize()

opponent_name, opponent_choice = choose_your_player()

if opponent_choice is not None:

    result = check_winner(player1_choice, opponent_choice)

    print("\n---------------------------")
    print(f"{player1_name}: {player1_choice}")
    print(f"{opponent_name}: {opponent_choice}")
    print("---------------------------")

    if result == "Player 1 Wins":
        print(f"🏆 {player1_name} Wins!")

    elif result == "Player 2 Wins":
        print(f"🏆 {opponent_name} Wins!")

    else:
        print("🤝 Draw!")