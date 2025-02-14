import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess > number_to_guess:
                print("Too high! Try again.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

# Run the game
guess_the_number()
