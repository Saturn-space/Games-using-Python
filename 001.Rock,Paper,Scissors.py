import random
choices = ["rock", "paper", "scissors"]

player = input("Enter your choice (rock, paper, scissors): ").lower()

compute = random.choice(choices)

if player == compute:
    print(f"Both players selected {player}. It's a tie!")

elif(player == "rock" and compute == "scissors") or \
    (player == "paper" and compute == "rock") or \
    (player == "scissors" and compute == "paper"):
    print(f"Player wins! {player} beats {compute}") 

else: print(f"Computer wins! {compute} beats {player}")