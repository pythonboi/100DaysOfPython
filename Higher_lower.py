import random
from art import logoHighLowe, vs
from game_data import data

print(logoHighLowe)

# Create a variable for the number of list in the data dictionary
pick = (len(data) - 1)

# Randomly select/Pick a number from the Data dictionary of the List
selectA = random.randint(0, pick)
selectB = random.randint(0, pick)

# Check and make sure the same value or number is not picked/selected during the random number picking
if selectA == selectB:
    selectA = random.randint(0, pick)
    # selectB = random.randint(0, pick)

selected = [selectA]

# Create a variable to use for counting the numbers of correct scores or valid attempts
counter = 0

# Create a variable to help with the f-string format for linking the string and easy rotation for each of the question
# comparison
option1 = 'Compare A:'

#
infoName = data[selectA].get('name')  #
infoDescr = data[selectA].get('description')
infoCountry = data[selectA].get('country')

aLetter = 'a'
frm = 'from'

# print(option1, infoName, infoDescr, infoCountry)

option2 = 'Against B:'

infoNameB = data[selectB].get('name')  #
infoDescrB = data[selectB].get('description')
infoCountryB = data[selectB].get('country')


getA = f"{infoName}, {aLetter} {infoDescr}, {frm} {infoCountry}."
getB = f"{infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}."

print(f"{option1} {infoName}, {aLetter} {infoDescr}, {frm} {infoCountry}.")

print(vs)

print(f"{option2} {infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}.")

a = data[selectA].get('follower_count')
b = data[selectB].get('follower_count')


while True:

    # This is to fix the code from not giving the same value
    if a == b:
        get_C()

# If counter is more than change the previous/existing value of a and b
    if counter != 0:
        a = changeA
        b = changeB

# Get user input for the question variable
    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # The Code below checking and evaluating the value between a and b

    if choose == 'a':
        if a > b:
            counter = counter + 1
            # pointer = pointer + 1
            print(f"You're right! Current score: {counter}.")

    elif choose == 'b':
        if b > a:
            counter = counter + 1
            # pointer = pointer + 1
            print(f"You're right! Current score: {counter}.")

    if choose == 'a':
        if a < b:
            print(f"Sorry, that's wrong. Final score: {counter}")
            # exit()
            break

    elif choose == 'b':
        if b < a:
            print(f"Sorry, that's wrong. Final score: {counter}")
            # exit()
            break

    else:
        print(f"Sorry, that's wrong. Final score: {counter}")
        break

# Create a function to get and change the global variable of a
    def get_A():

        needB = data[selectB].get('follower_count')
        if counter == 1:  # or counter > 1:
            needA = needB

            global a
            a = needA

            return a

# Create a function to change the value get from the get_C function and change it to be for a
    def getSecond_A():

        global a
        a = changeB

        return a

# Create awhile loop to keep rotating the question and replacing the value for the question

    if True:

        if counter > 1:
            switch1 = f"{option1} {getC} "
            print(switch1)

            changeA = getSecond_A()

        else:
            switch = f"{option1} {getB}"
            print(switch)

            changeA = get_A()

    print(vs)

# Creating and getting the third value for a placeholder to be able to rotate and change the questions

    selectC = random.randint(0, pick)

    infoNameC = data[selectC].get('name')  #
    infoDescrC = data[selectC].get('description')
    infoCountryC = data[selectC].get('country')

    getC = f"{infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}."

# Create a function for the third placeholder and changing the global variable value of b from c to b
    def get_C():

        # selectC = random.randint(0, pick)
        #
        # infoNameC = data[selectC].get('name')  #
        # infoDescrC = data[selectC].get('description')
        # infoCountryC = data[selectC].get('country')
        # c = data[selectC].get('follower_count')
        #
        # getC = f"{infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}."

        c = data[selectC].get('follower_count')

        global b
        b = c

        print(f"{option2} {getC}")
        return b


    changeB = get_C()
    print(a)
    print(b)
