import random
from art import logoHighLowe, vs
from game_data import data

print(logoHighLowe)

pick = (len(data))

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


getB = f"{option2} {infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}."

while True:

    print(f"{option1} {infoName}, {aLetter} {infoDescr}, {frm} {infoCountry}.")

    print(
        f"Compare A: {data[selectA].get('name')}, a {data[selectA].get('description')}, from {data[selectA].get('country')}.")

    print(vs)

    # against = f"Against B:", data[selectB].get('name'), "a", data[selectB].get('description'), "from", data[selectB].get('country'),"."
    #

    print(
        f"Against B: {data[selectB].get('name')}, a {data[selectB].get('description')}, from {data[selectB].get('country')}.")

    print(f"{option2} {infoNameB}, {aLetter} {infoDescrB}, {frm} {infoCountryB}.")

    print(getB)

    # print(f"{data[selectA].get('follower_count')}")
    # print(f"{data[selectB].get('follower_count')}")

    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    a = data[selectA].get('follower_count')
    b = data[selectB].get('follower_count')

    print(a)
    print(b)


    def switch():
        if choose != '':

            print(option2)
            # pass


    switch()

    # print(choose)

    # while True:
    if choose == 'a':
        if a > b:
            counter = counter + 1
            print(f"You're right! Current score: {counter}.")

    elif choose == 'b':
        if b > a:
            counter = counter + 1
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
