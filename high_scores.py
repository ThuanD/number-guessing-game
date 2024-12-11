import json
import os


class HighScores:
    """
    A class to manage and track high scores across different difficulty levels.
    """

    def __init__(self, filename="high_scores.json"):
        """
        Initialize high scores.

        Args:
            filename (str): File to store high scores
        """
        self.filename = filename
        self.scores = self._load_scores()

    def _load_scores(self):
        """
        Load existing high scores from file.

        Returns:
            dict: High scores for each difficulty level
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)

        # Default structure if no file exists
        return {
            "Easy": {"best_attempts": float("inf"), "best_time": float("inf")},
            "Medium": {"best_attempts": float("inf"), "best_time": float("inf")},
            "Hard": {"best_attempts": float("inf"), "best_time": float("inf")},
        }

    def update_score(self, difficulty, attempts, time_taken):
        """
        Update high scores if current performance is better.

        Args:
            difficulty (str): Game difficulty level
            attempts (int): Number of attempts used
            time_taken (float): Time to solve the puzzle
        """
        # Check if current performance beats existing high score
        if attempts < self.scores[difficulty]["best_attempts"] or (
            attempts == self.scores[difficulty]["best_attempts"]
            and time_taken < self.scores[difficulty]["best_time"]
        ):
            self.scores[difficulty]["best_attempts"] = attempts
            self.scores[difficulty]["best_time"] = time_taken

            # Save updated scores
            with open(self.filename, "w") as f:
                json.dump(self.scores, f, indent=4)

            print(f"\n🏆 New High Score for {difficulty} Difficulty!")
            print(f"Attempts: {attempts}, Time: {time_taken} seconds")

        # Always display current high scores
        self.display_high_scores()

    def display_high_scores(self):
        """
        Display high scores for all difficulty levels.
        """
        print("\n--- High Scores ---")
        for difficulty, score in self.scores.items():
            if score["best_attempts"] != float("inf"):
                print(
                    f"{difficulty}: {score['best_attempts']} attempts in {score['best_time']:.2f} seconds"
                )
            else:
                print(f"{difficulty}: No high score yet")
