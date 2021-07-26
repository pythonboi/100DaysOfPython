import random

randomGuess = random.randint(0, 1)

print("1 means Heads")
print("0 means Tails")

print(randomGuess)

if randomGuess == 1:
    print("It is Heads")
else:
    print("It is Tails")
