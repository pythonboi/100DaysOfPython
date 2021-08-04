# Password Generator Project
import random
import os
import os.path


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
email = input("What email account is this password for? \n")
name = input("Account name? \n")

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# I decide to group all the list in one big nested list since all the variable are list
# mulRandom = [letters, numbers, symbols]

# sum all the integer together to have the total number and left of the character symbols to make
allSum = nr_letters + nr_symbols + nr_numbers

# Create a list variable
passwd = []


# Create a counter variable to be able to loop through the number of sequence needed

count = 0
synt = 0
nmb = 0

for char in letters:
    if count < nr_letters:
        count += 1
        passwd.append(random.choice(letters))

for sym in symbols:
    if synt < nr_symbols:
        synt += 1
        passwd.append(random.choice(symbols))

for num in numbers:
    if nmb < nr_numbers:
        nmb += 1
        passwd.append(random.choice(numbers))

# convert the list to a string using the join function

lstStn = "".join(passwd)


print(f"Here is your password: {lstStn}")

# Stronger password Technic

chG = ""

if len(passwd) == allSum:
    for pw in passwd:
        chG += "".join(random.choice(passwd))

# new advance password
print(f"Stronger password: {chG}")

path = "/Users/erudite/project/100DaysOfPython/passwd.txt"


with open("passwd.txt", "a") as file:
    if os.path.exists(path):
        if os.path.isfile(path):
            file.writelines("Email_Account:")
            file.write("\n")
            file.write(email)
            file.write("\n")
            file.write("UserAccount:")
            file.write("\n")
            file.write(name)
            file.write("\n")
            file.write(f"Password: {chG}")
            file.write("\n")


# Making the Password More Stronger and Harder to Guess

# password = ""
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for sym in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for numb in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)
# #
# print(f"Here is your password: {password}")
# print("Note this password can be easily cracked")

# print("\n")
#
# chPass = ""
#
# # if len(password) == allSum:
# #     # for i in password:
# #     newPass = "".join(random.choice(password) for i in range(0, len(password)))  # + random.choice(password)
# #     chPass += newPass
#
#
# print(chPass)
# print("Here is much stronger password, very hard to crack")
# print(f"Here is your new password: {chPass}")
