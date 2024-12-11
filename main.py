from game import NumberGuessingGame


def main():
    """
    Main function to run the Number Guessing Game.
    Handles game loop and multiple rounds.
    """
    print("Welcome to the Ultimate Number Guessing Game!")

    while True:
        # Create a new game instance
        game = NumberGuessingGame()

        # Run a single game round
        game.play_round()

        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
