import streamlit as st
import random
 
def play_game(player_choice):
    computer_choice = random.choice(["🪨rock", "🏳paper", "✂scissors","🖖Spock","🦎lizard"])
    if player_choice == computer_choice:
        result = "It's a tie!"
        return result, computer_choice, "Draw"
    elif player_choice == "🪨rock" and computer_choice == "✂scissors":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🪨rock" and computer_choice == "🦎lizard":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🏳paper" and computer_choice == "🪨rock":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🏳paper" and computer_choice == "🖖Spock":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "✂scissors" and computer_choice == "🏳paper":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "✂scissors" and computer_choice == "🦎lizard":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🖖Spock" and computer_choice == "🪨rock":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🖖Spock" and computer_choice == "✂scissors":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🦎lizard" and computer_choice == "🖖Spock":
        result = "You win!"
        return result, computer_choice, "Win"
    elif player_choice == "🦎lizard" and computer_choice == "🏳paper":
        result = "You win!"
        return result, computer_choice, "Win"
    else:
        result = "You lose!"
        return result, computer_choice, "Lose"

# Set up the UI
st.title("Rock-Paper-Scissors-Spock-Lizard Game")
st.write("""Scissors cuts Paper covers Rock crushes Lizard poisons Spock smashes Scissors
decapitates Lizard eats Paper disproves Spock vaporizes Rock
(and as it always has)crushes Scissors""")

options = ["🪨rock", "🏳paper", "✂scissors","🖖Spock","🦎lizard"]
player_choice = st.radio("Choose your move:", options)

if st.button("Play"):
    result, computer_choice, outcome = play_game(player_choice)
    st.write(f"You chose {player_choice}, and the computer chose {computer_choice}.")
    if outcome == "Win":
        st.success(result, icon="🎉")
    elif outcome == "Lose":
        st.error(result, icon="👎")
    else:
        st.warning(result, icon="🤔")

    # add a counter
    if "counter" not in st.session_state:
        st.session_state["counter"] = {"Win": 0, "Lose": 0, "Draw": 0}

    st.sidebar.header("Score")
    st.session_state["counter"][outcome] += 1
    st.sidebar.write(f"Win: {st.session_state['counter']['Win']}")
    st.sidebar.write(f"Lose: {st.session_state['counter']['Lose']}")
    st.sidebar.write(f"Draw: {st.session_state['counter']['Draw']}")
        
if st.button("Reset"):
    st.session_state["counter"] = {"Win": 0, "Lose": 0, "Draw": 0}
    st.experimental_rerun()

