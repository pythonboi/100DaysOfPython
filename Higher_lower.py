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
print("before the while loop")

while True:

    # a = data[selectA].get('follower_count')
    # b = data[selectB].get('follower_count')

    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # def getSocialName():
    #     a = data[selectA].get('follower_count')
    #     b = data[selectB].get('follower_count')
    #     if counter > 1:
    #         newA = b

    # Code below checking and evaluating the code process

    print("inside the evaluate function")

    # counter = 0

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

        # if optionA > optionB:
        #     counter = counter + 1
        #     print(f"You're right! Current score: {counter}.")

        # elif optionB > optionA:
        #     counter = counter + 1
        #     print(f"You're right! Current score: {counter}")

    else:
        print(f"Sorry, that's wrong. Final score: {counter}")
        break

    # evaluate()

    def getA():
        needB = data[selectB].get('follower_count')
        if counter > 1:
            needA = needB
            print(needA)
            a = needA


    if True:
        switch = f"{option1} {getB}"
        print(switch)

        # thisB = b

        print(type(switch))
        # if counter > 2:
        #     switch = f"{option1} {getC()}"
        getA()

    print(vs)


    def getC():

        selectC = random.randint(0, pick)

        infoNameC = data[selectC].get('name')  #
        infoDescrC = data[selectC].get('description')
        infoCountryC = data[selectC].get('country')
        c = data[selectC].get('follower_count')
        # print(c)
        b = c
        print(b)

        print(f"{option2} {infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}.")


    getC()
    print(a)
    print(b)
