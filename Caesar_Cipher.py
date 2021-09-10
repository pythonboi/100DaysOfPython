alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    count_text = len(text)
    move = ''

    for m in range(0, count_text):
        move += alphabet[shift]
        alphabet[shift] = alphabet[shift + 1]
        shift += 1

    print(move)

    # for run in range(0, count_text):
    #     move += alphabet[shift]
    #
    #
    #
    #
    #
    #
    #
    #
    #     for check in move:
    #         if check in move:
    #             newShift = alphabet[move] + 1
    #             newShift += 1
    #             move += alphabet[newShift]
    #
    # print(move)


encrypt(text=text, shift=shift)
