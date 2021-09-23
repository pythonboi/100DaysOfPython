import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# create a function for 3 parameters text, shift, direction
def caesar(text, shift, direction):
    codeChar = ''
    # check and validate direction
    if direction == 'encode':
        # loop through the text
        for me in text:
            # check shift value greater than the len of alphabet

            if shift > len(alphabet):
                shift = shift % len(alphabet)
            # checking the value of the alphabet and increment with value of shift
            if me in alphabet:
                ch = alphabet.index(me) + shift

            else:
                codeChar += me
                # ch = alphabet.index(me) + shift

            if ch > len(alphabet):
                alpLeft = ch - len(alphabet)
                codeChar += alphabet[alpLeft]
            else:
                codeChar += alphabet[ch]

        print(f'The encoded text is {codeChar}')

        # for check in text:

    elif direction == 'decode':
        decChar = ''
        for new in text:
            if shift > len(alphabet):
                shift = shift % len(alphabet)
                # After code modification
            if new not in alphabet:
                decChar += new
            else:
                deco = alphabet.index(new) - shift
                decChar += alphabet[deco]
        print(f'The decoded text is {decChar}')


caesar(text=text, shift=shift, direction=direction)
