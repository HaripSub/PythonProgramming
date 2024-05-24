import random


def generate_number():
    return random.randint(1, 100)


def check_guess(number_to_guess, guess):
    if guess < 1 or guess > 100:
        return "Please guess a number within the range 1 to 100."
    elif guess < number_to_guess:
        return "Too low! Try again."
    elif guess > number_to_guess:
        return "Too high! Try again."
    else:
        return "Correct!"


def guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = generate_number()
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            result = check_guess(number_to_guess, guess)
            print(result)
            if result == "Correct!":
                guessed_correctly = True
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    guessing_game()
