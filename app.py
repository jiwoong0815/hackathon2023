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
        result = "You win!"
    elif player_choice == "spock" and computer_choice == "scissors":
        result = "You win!"
    elif player_choice == "lizard" and computer_choice == "spock":
        result = "You win!"
    elif player_choice == "lizard" and computer_choice == "paper":
        result = "You win!"
    else:
        result = "You lose!"
    return result, computer_choice


st.title("Rock-Paper-Scissors Game")
counter_win=0
counter_lose=0
counter_draw=0
options = ["rock", "paper", "scissors","spock","lizard"]
player_choice = st.radio("Choose your move:", options)

if st.button("Play"):
    result, computer_choice = play_game(player_choice)
    st.write(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    if result == "You win!":
        st.success(result, icon="🎉")
        counter_win+=1
    elif result == "You lose!":
        st.error(result, icon="👎")
        counter_lose+=1
    else:
        st.warning(result, icon="🤔")
        counter_draw+=1

    
if st.button("Reset"):
    st.experimental_rerun()
