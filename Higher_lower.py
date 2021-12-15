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

# print(a)
# print(b)
print("before the while loop")

while True:

    # a = data[selectA].get('follower_count')
    # b = data[selectB].get('follower_count')

    if counter != 0:
        a = changeA
        b = changeB

        # print(f"This is after counter is done: {a}")
        # print(f"This is after counter is done {b}")

    print(a)
    print(f"this is b:  {b}")

    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # Code below checking and evaluating the code process

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


    # selectC = random.randint(0, pick)
    #
    # infoNameC = data[selectC].get('name')  #
    # infoDescrC = data[selectC].get('description')
    # infoCountryC = data[selectC].get('country')
    # c = data[selectC].get('follower_count')
    #
    # getC = f"{infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}."

    def get_A():
        # print("I am read")
        needB = data[selectB].get('follower_count')
        if counter == 1:  # or counter > 1:
            needA = needB
            # print("b change to A")
            # print(needA)
            global a
            a = needA
            # print(f"this is a after change it from b {a}")

            # print("Me read")
            return a
        print("I finish reading")


    def getSecondA():

        global a
        a = changeB

        print("I get here, I am reading ")
        print(f"This is from line 149 {a}")
        return a


    if True:

        if counter > 1:
            switch1 = f"{option1} {getC} "
            # cut = switch1.removeprefix(option1)
            #
            #
            # print(cut)
            print(switch1)

            changeA = getSecondA()

        else:
            switch = f"{option1} {getB}"
            print(switch)
            print("Here is the problem")

            changeA = get_A()

    # print(f"a is still {d}")
    print(vs)
    print(f"a is still {a}")

    selectC = random.randint(0, pick)

    infoNameC = data[selectC].get('name')  #
    infoDescrC = data[selectC].get('description')
    infoCountryC = data[selectC].get('country')
    # move the c from here

    getC = f"{infoNameC}, {aLetter} {infoDescrC}, {frm} {infoCountryC}."


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
        print("This is from get_C function")
        print(c)

        global b
        b = c
        print(f"This is b after change if from c {b}")

        print(f"{option2} {getC}")
        return b


    changeB = get_C()
    print(a)
    print(b)
