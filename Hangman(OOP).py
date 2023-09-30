import random
from selection import categories
from pic import hangman_pic

class HangmanGame:
    def __init__(self):
        self.selected_difficulty = None
        self.category_name = None
        self.chosen_word = None
        self.num_spaces = 0
        self.lives = 0
        self.display = []
        self.guessed_letters = set()
        self.game_over = False

    def choose_difficulty(self):
        while True:
            # Display available difficulty levels
            print("Choose a difficulty level:")
            for difficulty in categories.keys():
                print(difficulty)

            selected_difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").capitalize()

            # Check if the selected difficulty level exists
            if selected_difficulty in categories:
                self.selected_difficulty = selected_difficulty
                return

            print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")

    def choose_word(self):
        word_list = categories[self.selected_difficulty][self.category_name]
        self.chosen_word = random.choice(word_list)
        self.num_spaces = len(self.chosen_word)

    def choose_category(self):
        while True:
            # Display available categories for the chosen difficulty level
            print(f"Choose a category for {self.selected_difficulty} difficulty:")
            for category in categories[self.selected_difficulty].keys():
                print(category)

            selected_category = input("Enter the category: ").capitalize()

            # Check if the selected category exists for the chosen difficulty level
            if selected_category in categories[self.selected_difficulty]:
                self.category_name = selected_category
                return

            print(f"Invalid category. Please enter a valid category for {self.selected_difficulty} difficulty.")

    def initialize_game(self):
        self.choose_difficulty()
        self.choose_category()
        self.choose_word()

        # Adjust the number of lives based on difficulty
        if self.selected_difficulty == "Easy":
            self.lives = 6
        elif self.selected_difficulty == "Medium":
            self.lives = 4
        elif self.selected_difficulty == "Hard":
            self.lives = 3

        # Initialize the display as a list of underscores
        self.display = ['_'] * self.num_spaces

    def play(self):
        self.initialize_game()
        print(f"Category: {self.category_name}")

        while not self.game_over:
            print(f"{' '.join(self.display)}")
            print(f"Lives: {self.lives}")

            guessed_letter = input('Guessed a letter: ').lower()

            # Check if the letter has already been guessed
            if guessed_letter in self.guessed_letters:
                print("You've already guessed that letter.")
                continue

            self.guessed_letters.add(guessed_letter)

            letter_guessed = False

            for position in range(len(self.chosen_word)):
                letter = self.chosen_word[position]
                if letter == guessed_letter:
                    self.display[position] = guessed_letter
                    letter_guessed = True

            if not letter_guessed:
                self.lives -= 1
                if self.lives <= 0:
                    self.game_over = True

            if '_' not in self.display:
                self.game_over = True

            print(hangman_pic[self.selected_difficulty][self.lives])

            print(f"Letters guessed by you: {', '.join(self.guessed_letters)}")

        # Reveal the chosen word
        print(f"The word was: {self.chosen_word}")

        if '_' not in self.display:
            print("Congratulations! You've won!")
        else:
            print("Game over. You lose!")

if __name__ == "__main__":
    print("Let's play Hangman!")
    while True:  # Add a loop to allow playing multiple games
        game = HangmanGame()
        game.play()
        play_again = input("Do you want to play Hangman again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break  # Exit the loop if the player doesn't want to play again

