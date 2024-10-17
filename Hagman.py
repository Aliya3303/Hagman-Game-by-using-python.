import random

# Hangman stages, represented as ASCII art
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# List of possible words for the hangman game
word_list = ['python', 'java', 'kotlin', 'javascript', 'hangman']

def choose_word():
    return random.choice(word_list)

def display_progress(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

def play_hangman():
    word = choose_word()
    word_length = len(word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = len(stages) - 1
    game_over = False

    print("Welcome to Hangman!")
    
    while not game_over:
        print(stages[wrong_guesses])
        print(f"Word: {display_progress(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, {guess} is not in the word.")
            guessed_letters.append(guess)

        if set(guessed_letters) >= set(word):
            print(f"Congratulations! You guessed the word: {word}")
            game_over = True
        elif wrong_guesses == max_wrong_guesses:
            print(stages[wrong_guesses])
            print(f"Game over! The word was: {word}")
            game_over = True

if _name_ == "_main_":
    play_hangman()
