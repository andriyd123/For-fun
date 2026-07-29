from art import guessing_art
import random

numbers = list(range(1, 101))

chosen_number = random.choice(numbers)

def number_guess(number):
    if number == chosen_number:
        print("You guessed it!")
        return True
    elif number < chosen_number:
        print("Too low.")
        return False
    else:
        print("Too high.")
        return False

def game():
    print(guessing_art)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("choose a difficulty. Type 'easy' or 'hard': ").lower()

    attemps = 0

    if difficulty == "easy":
        print("You have 10 attempts to guess the number.")
        attemps = 10
    elif difficulty == "hard":
        print("You have 5 attempts to guess the number.")
        attemps = 5
    else:
        print("Invalid difficulty. Please choose 'easy' or 'hard'.")
        exit()

    while attemps > 0:
        guess = int(input("Enter your guess: "))
        if number_guess(guess):
            break
        attemps -= 1
        if attemps == 0:
            print(f"You've run out of guesses. The number was {chosen_number}. You lose.")
            break
        else:
            print("Guess again.")
            print(f"You have {attemps} attempts remaining to guess the number.")

game()

continue_game = input("Do you want to play again? Type 'y' or 'n': ").lower()
if continue_game == "y":
    print("\n" * 100)
    game()
else:
    print("Thanks for playing!")
    exit()