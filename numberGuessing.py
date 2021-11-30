from art import logoGuess
import random

logo = logoGuess

print(logo)

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.\n")

# level = input("Welcome to the Number Guessing Game!\n"
#               "I'm thinking of a number between 1 and 100.\n"
#               "Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = []

for count in range(1, 101):
    number.append(count)

    numberChoice = random.choice(number)

# print(number)
# print(numberChoice)

# numberOfGuesses = 0

# if level == 'easy':
#
#     print(f"You have {easy} attempts remaining to guess the number.")
#     numberOfGuesses = 10
#     while numberOfGuesses != 0:
#         userGuess = int(input("Make a guess: "))
#         if userGuess == numberChoice:
#             print(f"You won. you guessed the number right 😃 : {numberChoice}")
#             break
#         elif userGuess > numberChoice:
#             print("Too high.\n"
#                   "Guess again.")
#             numberOfGuesses = numberOfGuesses - 1
#             print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
#         elif userGuess < numberChoice:
#             print("Too low.\n"
#                   "Guess again.")
#             numberOfGuesses = numberOfGuesses - 1
#             print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
#
# elif level == 'hard':
#     print(f"You have {hard} attempts remaining to guess the number.")
#     numberOfGuesses = hard
#     while numberOfGuesses != 0:
#         guess = int(input("Make a guess: "))
#         if guess == numberChoice:
#             print(f"You Won, you guessed the right number 😃 : {numberChoice}")
#             break
#         elif guess > numberChoice:
#             print("Too high.\n"
#                   "Guess again.")
#             numberOfGuesses = numberOfGuesses - 1
#             print(f"You have {numberOfGuesses} attempts remaining to guess the number.")
#         elif guess < numberChoice:
#             print("Too low.\n"
#                   "Guess again.")
#             numberOfGuesses = numberOfGuesses - 1
#             print(f"You have {numberOfGuesses} attempts remaining to guess the number.")


# print("You are out of attempts!\n"
#       f"The Guess number is {numberChoice}\n"
#       "Game Over")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

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


check()
