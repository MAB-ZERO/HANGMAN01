import random

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """
    ]
    return stages[6 - attempts]  # Adjust index for attempts left

def get_word_list():
    # You can expand or replace this list as needed
    return [
        'python', 'hangman', 'programming', 'developer', 'good', 'bad', 'best', 'happy', 'king', 'boy',
        'girl', 'sleep', 'mankind', 'humanity', 'artist', 'texture', 'star', 'alone', 'master',
        'gamer', 'rose', 'trick', 'physics', 'code', 'mathematics', 'chemistry', 'biology',
        'queen', 'sleepover', 'party', 'old', 'songs', 'teacher', 'goodness', 'taxes', 'notebooks',
        'dictionary', 'grammar', 'pronunciation', 'people', 'person', 'accessibility', 'rock',
        'paper', 'scissor', 'license', 'year', 'university', 'english', 'learners',
        'understanding', 'password', 'global', 'animal', 'plants', 'control', 'external',
        'internal', 'scratch', 'profile', 'user', 'projects', 'last', 'problems', 'terminal',
        'package', 'banana', 'candle', 'giraffe', 'jacket', 'laptop', 'mountain', 'chains',
        'started', 'snowy', 'cloudy', 'tempest', 'packed', 'dishes', 'snacks', 'purple',
        'harmony', 'popcorn', 'france', 'garden', 'killer', 'strawberry', 'violet', 'trees',
        'picture', 'blossom', 'parade', 'hanger', 'spaces', 'lights', 'ocean', 'circle',
        'faces', 'delicate', 'negative', 'feature', 'heroic', 'silent', 'racecar', 'tango',
        'format', 'bounds', 'punched', 'starman', 'jelly', 'barbecue', 'serpent', 'fortune',
        'greater', 'equator', 'opened', 'laid', 'units', 'knitted', 'planet', 'theory',
        'chosen', 'volcano', 'history', 'trans', 'warehouse', 'enchant', 'madden', 'liberate',
        'painted', 'voices', 'silken', 'dissolve', 'torque', 'scabble', 'reasons', 'charted',
        'wraths', 'pickle', 'melon', 'throat', 'hammer', 'gleams', 'keeper', 'arden', 'scouts',
        'curves', 'delegate', 'hurts', 'educate', 'bashful', 'twins', 'puffed', 'muted', 'sirens',
        'apples', 'grapes', 'medium', 'excite', 'orchard', 'journey', 'paragon', 'destiny',
        'monkeys', 'sailing', 'classes', 'holiday', 'justice', 'puzzles', 'lizard', 'thistle',
        'peacock', 'terminal', 'swimmer', 'flavor', 'future', 'shatter', 'rougher', 'delight',
        'archive', 'sandals', 'cabaret', 'trouble', 'outcome', 'activity', 'tricked', 'cactus',
        'records', 'network', 'springy', 'signals', 'healers', 'machine', 'whistle', 'toggle',
        'curtain', 'patents', 'lowland', 'sculptor', 'horizon', 'mystery', 'fairway', 'monarch',
        'triumph', 'cluster', 'vibrant', 'plaster', 'unicorn', 'tangled', 'curious', 'mosaic',
        'whisper', 'convene', 'slipper', 'cheerful', 'sprouts', 'hormone', 'quattro', 'refined',
        'included', 'sapphire', 'inspire', 'raptor', 'patient', 'pineapple', 'success',
        'respect', 'freight', 'magical', 'customs', 'hunters', 'change', 'puzzle', 'planning',
        'variety', 'rescue', 'village', 'traverse', 'validate', 'securing', 'miracle',
        'special', 'grandeur'
    ]

def prompt_play_again():
    while True:
        response = input("Would you like to play again? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def get_valid_guess(already_guessed):
    while True:
        guess = input("Guess a letter (or type 'give up' to reveal the word): ").lower()
        if guess == 'give up':
            return 'give up'
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.")
        elif guess in already_guessed:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def main():
    words = get_word_list()
    wins = 0
    losses = 0
    hints_per_game = 2  # Limit hints per game

    print("Welcome to Hangman!")

    while True:
        word = random.choice(words).lower()
        guessed_letters = set()
        correct_letters = set(word)
        attempts_left = 6
        incorrect_letters = set()
        hints_left = hints_per_game

        print("\nStarting a new game!")
        while attempts_left > 0 and not all(letter in guessed_letters for letter in correct_letters):
            print(display_hangman(attempts_left))
            display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
            print(f"Word: {display_word}")
            print(f"Incorrect guesses: {', '.join(sorted(incorrect_letters))}")
            print(f"Remaining attempts: {attempts_left}")
            if hints_left > 0:
                print(f"Hints remaining: {hints_left} (type 'hint' to reveal a letter)")
            print("Type 'give up' to reveal the word and end this game.")

            guess = input("Your guess: ").lower()

            if guess == 'give up':
                print(f"The word was: {word}")
                losses += 1
                break
            elif guess == 'hint' and hints_left > 0:
                # Provide a hint
                remaining_letters = [letter for letter in correct_letters if letter not in guessed_letters]
                if remaining_letters:
                    hint_letter = random.choice(remaining_letters)
                    guessed_letters.add(hint_letter)
                    hints_left -= 1
                    attempts_left -= 1  # Using a hint costs an attempt
                    print(f"Hint revealed: '{hint_letter}'")
                else:
                    print("No remaining letters to reveal.")
                continue
            elif len(guess) != 1 or not guess.isalpha():
                print("Please enter a single alphabetic letter.")
                continue
            elif guess in guessed_letters or guess in incorrect_letters:
                print("You already guessed that letter.")
                continue

            # Process guess
            if guess in correct_letters:
                guessed_letters.add(guess)
                print("Good guess!")
            else:
                incorrect_letters.add(guess)
                attempts_left -= 1
                print("Wrong guess!")

        # Check win condition
        if all(letter in guessed_letters for letter in correct_letters):
            print(display_hangman(attempts_left))
            print(f"Congratulations! You guessed the word: {word}")
            wins += 1
        elif attempts_left == 0:
            print(display_hangman(attempts_left))
            print(f"Game over! The word was: {word}")
            losses += 1

        # Show stats
        print(f"Wins: {wins} | Losses: {losses}")

        # Custom message
        response = input("Would you like a motivational message? (yes/no): ").lower()
        if response in ['yes', 'y']:
            if all(letter in guessed_letters for letter in correct_letters):
                print("Excellent job! Keep up the great work!")
            else:
                print("Don't give up! Practice makes perfect.")

        # Play again?
        if not prompt_play_again():
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("\nPreparing a new game...\n")


if __name__ == "__main__":
    main()
