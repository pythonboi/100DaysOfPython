from art import logoGuess
import random

logo = logoGuess

print(logo)

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = []

for count in range(1, 101):
    number.append(count)

    numberChoice = random.choice(number)

mode = {'easy': 10, 'hard': 5}


def check():
    # level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    for m in mode.keys():
        if m == level:
            numberOfGuesses = mode.get(m)
            print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
            while numberOfGuesses != 0:
                userGuess = int(input("Make a guess: "))
                if userGuess == numberChoice:
                    print(f"You won. you guessed the number right 😃 : {numberChoice}")
                    break
                elif userGuess > numberChoice:
                    print("Too high.\n"
                          "Guess again.")
                    numberOfGuesses = numberOfGuesses - 1
                    print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
                elif userGuess < numberChoice:
                    print("Too low.\n"
                          "Guess again.")
                    numberOfGuesses = numberOfGuesses - 1
                    print(f"You have {numberOfGuesses} attempts remaining to guess the number.")

            if numberOfGuesses == 0:
                print("You have exceeded the number of guesses, there are no more guesses left\n"
                      f"The guess number is {numberChoice}\n"
                      "Game Over!!! ")


check()
