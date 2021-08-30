import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Create a List

word_list = ["aardvark", "baboon", "camel"]

# Randomly select the word in the list to a variable

chosen_word = random.choice(word_list)

# Creating an empty list
display = []

# Create a variable to use for number of lives
lives = 6

# Printing out the guess word
print(f"Psst, the guess word is:", chosen_word)

# For loop for creating the dash sign
for char in chosen_word:
    # display += "_"
    display.append("_")
# print(display)

# for name in chosen_word:
#     if guess not in name:
#         lives -= 1
#     print(lives)

while True:

    # Print out the Guess Letter
    print("Guess a Letter: ", end="")

    # Take input from the user from the Keyboard
    guess = input()

    # change the input character from Capital letter to Lowercase letter of the use input
    guess = guess.lower()

    # Making a For loop to count the number of guess and make an index of that number with the missing blanks

    for check in range(len(chosen_word)):
        if guess in chosen_word[check]:
            display[check] = guess
    # Check if guess is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
    # Check for no lives and exit the loop
    if lives == 0:
        print(f"You Loose!, you now have {lives} lives left")
        break

    # for name in range(lives):
    #     if guess not in chosen_word:
    #         lives -= 1
    print(lives)
    print(display)

    # create a counter list to use to verify the display list if no more item left
    counter = []

    # For loop use for looping through display list
    for count in display:
        if count in chosen_word:
            counter += count
    # comparing and validating the counter list against the display to make sure no more blank space is left
    if counter == display:
        print("You Won!")
        break

    # print(counter)
# print("You Won")
