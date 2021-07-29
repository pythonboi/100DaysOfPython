import random

print("Rock, Paper, Scissor")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pick = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors "))
selection = [rock, paper, scissors]

# Human selection
# pick variable is use for Human

if pick == 0:
    print(f"human pick{rock}")
elif pick == 1:
    print(f"human pick{paper}")
elif pick == 2:
    print(f"human pick {scissors}")
else:
    print("Please pick number from 0-2")


# Using Random to select number randomly

choose = random.choice(selection)

m = len(selection)

take = random.randint(0, m-1)


# Computer Selection
# take variable is use for computer

if pick > 3:
    print("Computer won by default")

if take == 0:
    print(f"Computer picks{rock}")
elif take == 1:
    print(f"Computer pick{paper}")
elif take == 2:
    print(f"Computer pick{scissors}")


# This is computation between users and computer

if pick == 0 and take == 0:
    print("It is a Draw")
elif pick == 0 and take == 1:
    print("Computer Won")
elif pick == 0 and take == 2:
    print("I won")
elif pick == 1 and take == 0:
    print("I Won")
elif pick == 1 and take == 1:
    print("It is a draw")
elif pick == 2 and take == 1:
    print("I won")
elif take == 1 and pick == 0:
    print("Computer Won")
if take == 0 and pick == 2:
    print("Computer Won")
elif take == 2 and pick == 1:
    print("Computer Won")
elif take == 2 and pick == 2:
    print("It is a draw")




