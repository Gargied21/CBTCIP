def get_player_choice(player_number):
    while True:
        choice = input(f"Player {player_number}, enter your choice (rock, paper, or scissors): ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    player1_choice = get_player_choice(1)
    player2_choice = get_player_choice(2)
    
    result = determine_winner(player1_choice, player2_choice)
    print(f"\nPlayer 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")
    print(result)

if __name__ == "__main__":
    play_game()
