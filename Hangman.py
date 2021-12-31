import random
import hangman_art
import hangman_words

# Print the logo from the hangman_art
print(random.choice(hangman_art.logos))

# Randomly select word from the word_list, imported from the hangman_words
chosen_word = random.choice(hangman_words.word_list)

# Creating an empty list
display = []

# Create a variable to use for number of lives
lives = 6

# Printing out the guess word
# print(f"Psst, the guess word is: {chosen_word}")

print("This is a hangman Game. You have 7 lives to guess the chosen word \n"
      "you have to guess each character in a chosen word"), "\n"

# For loop for creating the dash sign
for char in chosen_word:
    # display += "_"
    display.append("_")


while True:

    # Print out the Guess Letter
    print("Guess a Letter: ", end="")

    # Take input from the user from the Keyboard
    guess = input()

    # change the input character from Capital letter to Lowercase letter of the use input
    guess = guess.lower()

    # Check if guess character already exist in the chosen word
    if guess in display:
        print(f"{guess} is already in the chosen word")

    # Making a For loop to count the number of guess and make an index of that number with the missing blanks

    for check in range(len(chosen_word)):
        if guess in chosen_word[check]:
            display[check] = guess

    # Check if guess is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not on the chosen word ")
        # Print out the ASCII stages index base on the number of lives left as a value for the list (stages)
        print(hangman_art.stages[lives])

    # Check for no lives and exit the loop
    if lives == 0:
        print(f"You Loose!, you now have {lives} lives left")
        print(f"The chosen word is {chosen_word}")
        break

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
