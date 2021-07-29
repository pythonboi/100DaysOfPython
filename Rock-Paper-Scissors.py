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


if pick == 0:
    print(f"human pick{rock}")
elif pick == 1:
    print(f"human pick{paper}")
elif pick == 2:
    print(f"human pick {scissors}")


choose = random.choice(selection)
# print(choose)

m = len(selection)

take = random.randint(0, m)
print(take)

if take == 0:
    print(f"Computer picks{rock}")
elif take == 1:
    print(f"Computer pick{paper}")
elif take == 2:
    print(f"Computer pick{scissors}")

if pick == 0 and take == 0:
    print("It is a Draw")


# if len(selection[0]) == 0:
#     print(f"Computer pick{rock}")
#

