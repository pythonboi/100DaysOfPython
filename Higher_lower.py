import random
from art import logoHighLowe, vs
from game_data import data

print(logoHighLowe)

pick = (len(data))

selectA = random.randint(0, pick)
selectB = random.randint(0, pick)

selected = [selectA]

print(selected)

# print(selectA)
# print(selectB)

counter = 0

print(
    f"Compare A: {data[selectA].get('name')}, a {data[selectA].get('description')}, from {data[selectA].get('country')}.")

print(vs)

print(
    f"Against B: {data[selectB].get('name')}, a {data[selectB].get('description')}, from {data[selectB].get('country')}.")
choose = input(f"Who has more followers? Type 'A' or 'B': ").lower()

while selectA not in selected:

    if data[selectA].get('follower_count') > data[selectB].get('follower_count'):
        counter = counter + 1
        print(f"You're right! Current score: {counter}.")

    elif data[selectB].get('follower_count') > data[selectA].get('follower_count'):
        counter = counter + 1
        print(f"You're right! Current score: {counter}")

    else:
        print(f"Sorry, that's wrong. Final score: {counter}")
        break
