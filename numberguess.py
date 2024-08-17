def get_hidden_number():
    while True:
        hidden_number = input("Player 1, please enter the multi-digit number for Player 2 to guess: ")
        if hidden_number.isdigit():
            return hidden_number
        else:
            print("Invalid input. Please enter a number.")

def get_guess(length):
    while True:
        guess = input(f"Player 2, please guess the {length}-digit number: ")
        if guess.isdigit() and len(guess) == length:
            return guess
        else:
            print(f"Invalid input. Please enter a {length}-digit number.")

def play_game():
    hidden_number = get_hidden_number()
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_guess(len(hidden_number))
        attempts += 1

        if guess == hidden_number:
            guessed_correctly = True
            print(f"Congratulations, Player 2! You've guessed the number {hidden_number} correctly in {attempts} attempts.")
        else:
            print("Wrong guess, try again!")

if __name__ == "__main__":
    play_game()
