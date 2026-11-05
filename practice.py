import random

secret_number = random.randint(1, 100)
guess = input("Guess a number between 1 and 100: ")

while int(guess) != secret_number:
    new = guess
    guess = input("Try again: ")

    if int(guess) < secret_number:
        print("Too low! Answer is higher than " + guess + " and lower than " + new)
    elif int(guess) > secret_number:
        print("Too high! Answer is lower than " + guess + " and higher than " + new)
    else:
        print("Congratulations! You guessed the secret number!")