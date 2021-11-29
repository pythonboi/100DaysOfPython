from art import logoGuess
import random

level = input("Welcome to the Number Guessing Game!\n"
              "I'm thinking of a number between 1 and 100.\n"
              "Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = []

for count in range(1, 101):
    number.append(count)
    # print(count)
    #numberChoice = random.choice(count)
    #number.append(numberChoice)

print(number)

if level == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    print("Make a guess: ")
