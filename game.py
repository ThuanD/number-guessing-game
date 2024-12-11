import random
import time
from high_scores import HighScores


class NumberGuessingGame:
    """
    A class to manage the Number Guessing Game logic.
    """

    DIFFICULTY_LEVELS = {
        1: {"name": "Easy", "chances": 10},
        2: {"name": "Medium", "chances": 5},
        3: {"name": "Hard", "chances": 3},
    }

    def __init__(self):
        """
        Initialize game parameters.
        """
        self.high_scores = HighScores()

    def _get_difficulty(self):
        """
        Allow user to select game difficulty.

        Returns:
            dict: Difficulty level details
        """
        print("\nPlease select the difficulty level:")
        for key, level in self.DIFFICULTY_LEVELS.items():
            print(f"{key}. {level['name']} ({level['chances']} chances)")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in self.DIFFICULTY_LEVELS:
                    return self.DIFFICULTY_LEVELS[choice]
                raise ValueError
            except ValueError:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def _generate_hints(self, target, guess):
        """
        Generate hints based on the guess.

        Args:
            target (int): The number to guess
            guess (int): User's current guess

        Returns:
            str: Hint message
        """
        hints = []

        # Hint about divisibility
        if target % 2 == 0 and guess % 2 != 0:
            hints.append("The target number is even.")
        elif target % 2 != 0 and guess % 2 == 0:
            hints.append("The target number is odd.")

        # Hint about ranges
        if abs(target - guess) > 20:
            hints.append("You're quite far from the target number.")

        return " ".join(hints) if hints else "No additional hints available."

    def play_round(self):
        """
        Play a single round of the Number Guessing Game.
        """
        # Select difficulty
        difficulty = self._get_difficulty()
        max_attempts = difficulty["chances"]

        # Generate target number
        target_number = random.randint(1, 100)

        # Game setup
        attempts = 0
        start_time = time.time()

        print(f"\nGreat! You have selected the {difficulty['name']} difficulty level.")
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} chances to guess the correct number.\n")

        # Game loop
        while attempts < max_attempts:
            try:
                # Get user guess
                guess = int(input("Enter your guess: "))
                attempts += 1

                # Check guess
                if guess == target_number:
                    end_time = time.time()
                    elapsed_time = round(end_time - start_time, 2)

                    print(
                        f"\nCongratulations! You guessed the correct number {target_number} in {attempts} attempts."
                    )
                    print(f"Time taken: {elapsed_time} seconds")

                    # Update high scores
                    self.high_scores.update_score(
                        difficulty["name"], attempts, elapsed_time
                    )
                    return

                # Provide feedback
                if guess < target_number:
                    print("Incorrect! The number is greater than your guess.")
                else:
                    print("Incorrect! The number is less than your guess.")

                # Provide hints if stuck
                if attempts > max_attempts // 2:
                    print("Hint:", self._generate_hints(target_number, guess))

                # Remaining attempts
                remaining = max_attempts - attempts
                print(f"Attempts remaining: {remaining}\n")

            except ValueError:
                print("Please enter a valid number between 1 and 100.")

        # Game over if no attempts left
        print(f"\nGame Over! The number was {target_number}.")
