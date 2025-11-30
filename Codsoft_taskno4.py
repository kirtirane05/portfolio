# Rock-Paper-Scissors Game - Version 2
# Made using Python

import random

def get_computer_choice():
    """Return a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    """Determine the winner of the round."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """Main game loop."""
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Type 'quit' anytime to exit the game.\n")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice == "quit":
            print("\n👋 Thanks for playing!")
            print(f"Final Score → You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 You are the winner overall!")
            elif user_score < computer_score:
                print("💻 Computer wins overall!")
            else:
                print("🤝 It's an overall tie!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠ Invalid input! Please enter rock, paper, or scissors.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"💻 Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"🏆 Score → You: {user_score} | Computer: {computer_score}\n")

# Run the game
play_game()
