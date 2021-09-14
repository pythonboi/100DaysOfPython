alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# newText = text.split()
#
#
# def encrypt(text, shift):
#     count_text = len(text)
#     move = ''
#
#     # Loop through len of text
#     # for m in range(0, count_text):
#     # Add the index value of the number 5 to move variable
#     #     move += alphabet[shift]
#     # Increment the shift and add it to the index value
#     #     alphabet[shift] = alphabet[shift + 1]
#     # Increment the shift value by one during the Loop
#     #     shift += 1
#     #
#     # print(move)
#     # for loop for check the first letter in text variable in the alphabet list
#     for check in alphabet:
#         # check for the index of the first character in the newText variable
#         if check == newText[0][0]:
#             # get the index that match the first character of the newText
#             getIndex = alphabet.index(check)
#
#     print(getIndex)
#     # Loop through the length of the text variable
#     for count in range(0, count_text):
#         # Increment the index value in the alphabet
#         alphabet[getIndex] = alphabet[getIndex + 1]
#         # Increment the index on each loop to move forward
#         getIndex += 1
#         # Add each character of the index to the move string variable
#         move += alphabet[getIndex]
#
#     print(move)
#
#
# encrypt(text=text, shift=shift)

# for l in range()
#         alphabet[text] = alphabet[text + 1]
#         shift += 1
#

# BETTER COPY


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
    print(f"The encode text is {newEn}")  # newEn)


def decrypt(text, shift):
    deNew = ''
    for check in text:
        getDecry = alphabet.index(check) - shift
        deNew += alphabet[getDecry]

    print(f"The decoded text is {deNew}")


if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)
