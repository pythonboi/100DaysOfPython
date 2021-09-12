# a = 5
# b = a += 2
# print(a)

# hard = True
#
# while hard:
#     print("we move")
#     break

#
# live = 6
# num = 0
#
# for count in range(live):
#     if num < live:
#         live -= 1
#         print(live)
#
# # print(live)
#
# def greet(city, name, location):
#     print("Hello ", end='')
#     print("World")
#     print(f"I live in {city} and my name is {name}, you can find me in {location} ")
#
#
# greet(location="canada", name="hafeez", city="Toronto")
#
# import math
#
#
# # Write your code below this line 👇
# def paint_calc(height, width, cover):
#     numbOfCans = (height * width) / cover
#     print(numbOfCans)
#     rand = round(numbOfCans)
#     ran = math.ceil(numbOfCans)
#     print(f"You will need {rand} cans of paint")
#     print(f"You will need {ran} cans of paint")
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(len(alphabet))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    newEn = ''
    for count in text:
        en = alphabet.index(count) + shift
        if en >= len(alphabet):
            fw = alphabet.index("a") + shift
            fw -= 1
            lw = alphabet.index(count) - shift
            newEn += alphabet[fw]
            # newEn += alphabet[nw]
        else:
            newEn += alphabet[en]
        # print(en)
    print(newEn)
    print(alphabet.index("a"))


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

encrypt(text=text, shift=shift)
