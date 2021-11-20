import random
from art import logoBlackjack1

# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The the Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

print(logoBlackjack1)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    newCard = random.choice(cards)
    return newCard


deal_card()

# counts = 0

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

user_cards.append(deal_card())
computer_cards.append(deal_card())

for count in range(len(user_cards)):
    if count < 2:
        user_cards.append(deal_card())

print(user_cards)

for num in range(len(computer_cards)):
    if num < 2:
        computer_cards.append(deal_card())


# print(computer_cards)


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.


def compare(user, computer):
    if sum(user_cards) == sum(computer_cards):
        print("draw")
        print(sum(user_cards), "and", sum(computer_cards))
        print(computer_cards)

        exit()


compare(user_cards, computer_cards)


def calculate_score(user, computer):
    # print(sum(user_cards))
    # return user_cards[0] + user_cards[1]
    # return computer_cards[0] + computer_cards[1]
    # print(sum(computer_cards))

    # Place code here
    # The code works fine when check if computer or user has the total cards of 21 when check above verifying
    # blackjack
    # working  code move from here

    # code below are first
    # Checking for blackjack

    if sum(user_cards) == 21:
        if user_cards[0] == 11 and user_cards[1] == 10:
            print("BlackJack You Win")
        elif user_cards[0] == 10 and user_cards[1] == 11:
            print("BlackJack You Win")

        # return 0
        # return True

    elif sum(computer_cards) == 21:
        if computer_cards[0] == 11 and computer_cards[1] == 10:
            print("BlackJack Computer Wins")
            print(computer_cards)
        elif computer_cards[0] == 10 and computer_cards[1] == 11:

            print("BlackJack Computer Wins")
            print(computer_cards)
        # return 0
        # return True

    elif sum(user_cards) == 21:
        print("You Win, your score is: ", sum(user_cards))
        print("Computer score is: ", sum(computer_cards))
        print(computer_cards)
        # return "You win, your score is ", sum(user_cards)
        # print(0)
        # return 0
        exit()

    elif sum(computer_cards) == 21:
        print("Computer wins, score is: ", sum(computer_cards))
        print("Your score is: ", sum(user_cards))
        print(computer_cards)
        # print(computer_cards)
        # print(0)
        exit()

    # Here is where i moved the code from

    # Code move above

    if sum(user_cards) > 21:
        if user_cards[0] == 11 or user_cards[1] == 11:
            user_cards.remove(11)
            user_cards.append(1)

            print(sum(user_cards))

    if sum(computer_cards) > 21:
        if computer_cards[0] == 11 or computer_cards[1] == 11:
            computer_cards.remove(11)
            computer_cards.append(1)
            print(sum(computer_cards))

    # putting code move from top here

    ##########################

    if sum(user_cards) > 21:
        print("You loose, your score is: ", sum(user_cards))
        print(computer_cards)

        print("Computer Win, Computer score: ", sum(computer_cards))

        # exit()

    if sum(computer_cards) > 21:
        # print(computer_cards)
        print("Computer loose, computer score is: ", sum(computer_cards))
        print("You win, your score is: ", sum(user_cards))
        exit()

    if sum(user_cards) == sum(computer_cards):
        compare(user, computer)
        # (user_cards, computer_cards)

    return user_cards, computer_cards


# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
# instead of the actual score. 0 will represent a blackjack in our game.


# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21,
# remove the 11 and replace it with a 1. You might need to look up append() and remove().

calculate_score(user_cards, computer_cards)

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0)
# or if the user's score is over 21, then the game ends.

if sum(user_cards) == 21 or sum(computer_cards) == 21:
    exit()

while sum(user_cards) <= 21:  # and

    deal = input("what to deal another card:? ").lower()

    if deal == 'y':
        user_cards.append(deal_card())
        print(user_cards)
        calculate_score(user_cards, computer_cards)

    elif deal == 'n':  # or sum(computer_cards) < 21:
        while sum(computer_cards) <= 21:

            if sum(user_cards) == sum(computer_cards):
                compare(user_cards, computer_cards)

            # calculate_score(user_cards, computer_cards)
            # print("draw")
            # print(computer_cards)
            # print(sum(user_cards))
            # print(sum(computer_cards))
            # exit()
            # calculate_score(user_cards, computer_cards)

            # Check this code later
            # make this elif

            elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) <= 21:
                print("Computer Win, Computer Score is: ", sum(computer_cards))
                print(computer_cards)
                print("your Score is: ", sum(user_cards))
                exit()
                # break

            # computer_cards.append(deal_card())
            # print(computer_cards)
            # calculate_score(user_cards, computer_cards)

            # need to re-visit this code and understand what is doing much better
            # make this elif from if

            elif sum(computer_cards) > 21 and sum(user_cards) <= 21:
                print("You win, your Score is: ", sum(user_cards))
                print("Computer score is:", sum(computer_cards))
                break
                # exit()
                # computer_cards.append(deal_card())
                # calculate_score(user_cards, computer_cards)

            # elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) <= 21:
            #     print("Computer wins", sum(computer_cards))
            #     exit()
            elif sum(computer_cards) < sum(user_cards) and sum(computer_cards) < 21:
                computer_cards.append(deal_card())
                print(computer_cards)
                calculate_score(user_cards, computer_cards)

            elif sum(user_cards) > sum(computer_cards):
                print("You win, your score is:", sum(user_cards))
                print("Computer score is:", sum(computer_cards))
                break
                # exit()

            elif sum(computer_cards) > sum(user_cards) and sum(computer_cards) == 21:
                print("Computer Win, Computer score is: ", sum(computer_cards))
                print("You score is: ", sum(user_cards))
                break



    elif deal != 'y' or deal != 'n':

        break




# Hint 10: If the game has not ended, ask the user if they want to draw another card.
# If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and
# the checks in Hint 9 need to be repeated until the game ends.


# Hint 12: Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.


# Hint 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0),
# then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21,
# then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.

# play = input("Do you want restart the game:? 'y' for 'yes and 'n' for no").lower()
#
# if play == 'y':
#     calculate_score(user_cards, computer_cards)
#
# else:
#     exit()

# Hint 14: Ask the user if they want to restart the game.
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
