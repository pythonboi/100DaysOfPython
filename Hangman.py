import random

# Create a List

word_list = ["aardvark", "baboon", "camel"]

# Randomly select the word in the list to a variable

chosen_word = random.choice(word_list)

# Print out the Guess Letter
print("Guess a Letter: ",  end="")

# Take input from the user from the Keyboard
guess = input()

# change the input character from Capital letter to Lowercase letter of the use input
guess = guess.lower()


print(chosen_word)
print(guess)