import random  # Used to let the computer pick randomly


# Returns a random choice for the computer: "r", "p", or "s"

def get_computer_choice():
    return random.choice(["r", "p", "s"])


# Converts the shorthand letter into a readable word
# Example: "r" -> "Rock"

def choice_to_word(choice):
    return {"r": "Rock", "p": "Paper", "s": "Scissors"}[choice]


# Determines the winner based on player and computer choices
# Returns a string describing the result

def get_winner(player, computer):
    # If both choices are the same → tie
    if player == computer:
        return "It's a tie!"

    # Player winning conditions
    elif (player == "r" and computer == "s") or \
         (player == "s" and computer == "p") or \
         (player == "p" and computer == "r"):
        return "Player Wins!"

    # Otherwise, computer wins
    else:
        return "Computer Wins!"


# Main game loop
# Handles input, scoring, and printing results

def play_game():
    # Score counters
    player_score = computer_score = ties = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'quit'/'q' to exit.\n")

    while True:
        # Get player input
        player = input("Your choice (r for rock/p for paper/s for scissors or quit/q): ").lower().strip()

        # Exit condition
        if player in ["quit", "q"]:
            print(f"\nGame ended. Final Score -> Player: {player_score}, Computer: {computer_score}, Ties: {ties}")
            break

        # Validate input
        if player not in ["r", "p", "s"]:
            print("Invalid choice, try again.\n")
            continue

        # Computer makes a choice
        computer = get_computer_choice()

        # Show choices
        print(f"Player choice: {choice_to_word(player)}")
        print(f"Computer choice: {choice_to_word(computer)}")

        # Determine winner
        result = get_winner(player, computer)
        print(result, "\n")

        # Update scores
        if result == "Player Wins!":
            player_score += 1
        elif result == "Computer Wins!":
            computer_score += 1
        else:
            ties += 1

        # Display updated score
        print(f"Score -> Player: {player_score}, Computer: {computer_score}, Ties: {ties}\n")

# Start the game
play_game()
