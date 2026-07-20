import tkinter as tk
import random
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.resizable(False, False)
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)
    player_label.config(text=f"You Chose: {player_choice}")
    computer_label.config(text=f"Computer Chose: {computer_choice}")
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    result_label.config(text=result)
    score_label.config(
        text=f"Player: {player_score}      Computer: {computer_score}"
    )
title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)
player_label = tk.Label(root, text="You Chose: ", font=("Arial", 14))
player_label.pack(pady=10)
computer_label = tk.Label(root, text="Computer Chose: ", font=("Arial", 14))
computer_label.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=20)
score_label = tk.Label(
    root,
    text="Player: 0      Computer: 0",
    font=("Arial", 14)
)
score_label.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack(pady=30)
rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)
paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 12),
    width=10,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)
def reset():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_label.config(text="You Chose:")
    computer_label.config(text="Computer Chose:")
    result_label.config(text="")
    score_label.config(text="Player: 0      Computer: 0")
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    command=reset
)
reset_btn.pack(pady=20)
root.mainloop()