import random

# Create a List

word_list = ["aardvark", "baboon", "camel"]

# Randomly select the word in the list to a variable

chosen_word = random.choice(word_list)

# Creating an empty list
display = []

# Printing out the guess word
print(f"Psst, the guess word is:", chosen_word)

# For loop for creating the dash sign
for char in chosen_word:
    # display += "_"
    display.append("_")
# print(display)

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

    print(display)
