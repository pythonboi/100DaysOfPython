# Love Calculator

print("Welcome to the love Calculator!")

guy_name = input("What is your name?\n ")

female_name = input("What is her name?\n ")

guyLower = guy_name.lower()

femaleLower = female_name.lower()

both = guyLower + femaleLower

print(f"Male name is: {guyLower} and female name is: {femaleLower}\n")


print("T occurs", both.count("t"), " ", "L occurs", both.count("l"))
print("R occurs", both.count('r'), " ", "O occurs", both.count("o"))
print("U occurs", both.count('u'), " ", "V occurs", both.count("v"))
print("E occurs", both.count('e'), " ", "E occurs", both.count("e"))
print("\n")

trueCount = both.count("t") + both.count("r") + both.count("u") + both.count("e")
loveCount = both.count("l") + both.count("o") + both.count("v") + both.count("e")

totalCount = str(trueCount) + str(loveCount)
# print(totalCount)

print(f"Total count for True = {trueCount}")
print(f"Total count for Love = {loveCount}")

print(f"Your True Love Score = {trueCount}{loveCount}")
print("\n")

if int(totalCount) < 10 or int(totalCount) > 90:
    print(f"Your score is {totalCount}, you go together like coke and mentos")
elif 40 <= int(totalCount) <= 50:
    print(f"Your score is {totalCount}, you are alright together")
else:
    print(f"Your score is {totalCount}")



