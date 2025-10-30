import random
""" Creates an interactive guessing game
User guesses the word with limited guesses.
"""
# Create a list of randoms words. 
random_word = ["panda", "flowers", "roses", "road", "plane"]
# A random word is selected ans stored.
word_choice = random.choice(random_word)

# Set the limit number of guessses to 5.
limit = 7
# Define empty string that stores attempts.
guesses = ''
# Loop runs as long as user has guesses left.
while limit > 0:
    # Counts characters guessed incorrectly so far.
    failed = 0
    # If guess is correct display the word. If not display underscore. 
    for w in word_choice:
        if w in guesses:
            print(w, end=" ")
        else:
            print("_", end=" ")
            failed += 1 # Store the incorrect guess.
    print()
    # If all characters are guessed. Display the word.
    if failed == 0:
        print(f"Congratulations! You guessed the word {word_choice}.")
        break
    else:
        print()
    # Prompt user to guess a letter.
    word_guessed = input("Guess a letter: ")
    # Store attempt in string.
    guesses += word_guessed
    # If the word is guessed incorrectly, store attempt.
    if word_guessed not in word_choice:
        limit -= 1
        print(f"Incorrect word. You have {limit} guesses left")
        # Once user runs out of limits, game over.
        if limit == 0:
            print("Game over, no more guesses left.")


