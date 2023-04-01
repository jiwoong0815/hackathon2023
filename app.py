import streamlit as st
import random

def play_game(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors","spock","lizard"])
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif player_choice == "rock" and computer_choice == "lizard":
        result = "You win!"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    elif player_choice == "paper" and computer_choice == "spock":
        result = "You win!"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    elif player_choice == "scissors" and computer_choice == "lizard":
        result = "You win!"
    elif player_choice == "spock" and computer_choice == "rock":
        result = "you win!"
    elif player_choice == "spock" and computer_choice == "scissors":
        result = "you win!"
    elif player_choice == "lizard" and computer_choice == "spock":
        result = "you win!"
    elif player_choice == "lizard" and computer_choice == "paper":
        result = "you win!"
    else:
        result = "You lose!"
    return result, computer_choice

# Set up the UI
st.title("Rock-Paper-Scissors Game")

options = ["rock", "paper", "scissors","spock","lizard"]
player_choice = st.radio("Choose your move:", options)

if st.button("Play"):
    result, computer_choice = play_game(player_choice)
    st.write(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    if result == "you win!":
        st.success(result,,icon=)
    if result == "you lose!":
        st.