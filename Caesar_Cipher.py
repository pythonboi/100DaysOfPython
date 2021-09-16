alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    codeChar = ''
    if direction == 'encode':
        for me in text:
            ch = alphabet.index(me) + shift
            if ch > len(alphabet):
                alpLeft = ch - len(alphabet)
                codeChar += alphabet[alpLeft]
            else:
                codeChar += alphabet[ch]
        print(f'The encoded text is {codeChar}')

    elif direction == 'decode':
        decChar = ''
        for new in text:
            deco = alphabet.index(new) - shift
            decChar += alphabet[deco]
        print(f'The decoded text is {decChar}')


caesar(text=text, shift=shift, direction=direction)
