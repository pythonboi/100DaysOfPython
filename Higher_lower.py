import random
from art import logoHighLowe, vs
from game_data import data

# vs = """
#  _    __
# | |  / /____
# | | / / ___/
# | |/ (__  )
# |___/____(_)
#
# """

print(logoHighLowe)

pick = (len(data))

selectA = random.randint(0, pick)
selectB = random.randint(0, pick)

print(selectA)
print(selectB)

print(
   f"Compare A: {data[selectA].get('name')}, a {data[selectA].get('description')}, from {data[selectA].get('country')}.")

print(vs)

print(f"Against B: ")
