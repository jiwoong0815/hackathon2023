import streamlit as sp
import random

# Define the game logic
def play_game(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    else:
        result = "You lose!"
    return result, computer_choice

# Set up the UI
st.title("Rock-Paper-Scissors Game")

options = ["rock", "paper", "scissors"]
player_choice = st.radio("Choose your move:", options)

if st.button("Play"):
    result, computer_choice = play_game(player_choice)
    st.write(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    st.write(result)