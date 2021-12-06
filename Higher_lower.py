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
option2 = 'Against B:'


def switch():
    if choose != '':
        pass


while True:

    print(
        f"Compare A: {data[selectA].get('name')}, a {data[selectA].get('description')}, from {data[selectA].get('country')}.")

    print(vs)

    # against = f"Against B:", data[selectB].get('name'), "a", data[selectB].get('description'), "from", data[selectB].get('country'),"."
    #

    print(
        f"Against B: {data[selectB].get('name')}, a {data[selectB].get('description')}, from {data[selectB].get('country')}.")

    # print(f"{data[selectA].get('follower_count')}")
    # print(f"{data[selectB].get('follower_count')}")

    choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    a = data[selectA].get('follower_count')
    b = data[selectB].get('follower_count')

    print(a)
    print(b)

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
