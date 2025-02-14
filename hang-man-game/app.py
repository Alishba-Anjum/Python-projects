from time import sleep
import random


user_name = input('Enter your name: ')
print(f"Hello, {user_name}! Let's play the game!")
sleep(1)
print("Start guessing...")
sleep(0.5)

words = ['apple', 'strawberry', 'orange', 'smartphone', 'umbrella', 'laptop']

word = random.choice(words)
word_length = len(word)

guesses = ''
attempts = 6

# Game loop
while attempts > 0:
    failed = 0


    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += '_'
            failed += 1

    print(display_word)

    if failed == 0:
        print("Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    guesses += guess

    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")
        if attempts == 0:
            print(f"Game over! The word was '{word}'.")
