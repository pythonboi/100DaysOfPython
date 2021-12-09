import random
from art import logoHighLowe, vs
from game_data import data

print(logoHighLowe)

pick = (len(data) - 1)
# print(pick)

selectA = random.randint(0, pick)
selectB = random.randint(0, pick)

if selectA == selectB:
    selectA = random.randint(0, pick)
    # selectB = random.randint(0, pick)

selected = [selectA]

# print(selected)
#
# print(selectA)
# print(selectB)

counter = 0

option1 = 'Compare A:'

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

# {option2}

getA = f"{infoName}, {aLetter} {infoDescr}, {frm} {infoCountry}."
getB = f"{infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}."

print(f"{option1} {infoName}, {aLetter} {infoDescr}, {frm} {infoCountry}.")

print(vs)

print(f"{option2} {infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}.")

a = data[selectA].get('follower_count')
b = data[selectB].get('follower_count')

print(a)
print(b)

while True:

    b = data[selectB].get('follower_count')

    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()



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
            break

    elif choose == 'b':
        if b < a:
            print(f"Sorry, that's wrong. Final score: {counter}")
            break

    # if optionA > optionB:
    #     counter = counter + 1
    #     print(f"You're right! Current score: {counter}.")

    # elif optionB > optionA:
    #     counter = counter + 1
    #     print(f"You're right! Current score: {counter}")

    else:
        print(f"Sorry, that's wrong. Final score: {counter}")
        break

    if True:
        # counter != 0:
        print(f"{option1} {getB}")

    print(vs)

    selectC = random.randint(0, pick)

    infoNameC = data[selectC].get('name')  #
    infoDescrC = data[selectC].get('description')
    infoCountryC = data[selectC].get('country')
    c = data[selectC].get('follower_count')
    # print(c)
    b = c
    print(b)

    print(f"{option2} {infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}.")


# print(
#     f"Compare A: {data[selectA].get('name')}, a {data[selectA].get('description')}, from {data[selectA].get('country')}.")

# against = f"Against B:", data[selectB].get('name'), "a", data[selectB].get('description'), "from", data[selectB].get('country'),"."
#

# print(
#     f"Against B: {data[selectB].get('name')}, a {data[selectB].get('description')}, from {data[selectB].get('country')}.")

# print(getB)
