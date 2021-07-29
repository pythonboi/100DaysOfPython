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

pick = input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors")
selection = [rock, paper, scissors]

rock = 1
paper = 2
scissors = 3

choose = random.choice(selection)

print(choose)

