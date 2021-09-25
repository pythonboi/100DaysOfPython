import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

while True:

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ""\n").lower()

    if again == 'yes':

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
                    if me not in alphabet:
                        codeChar += me
                    else:
                        ch = alphabet.index(me) + shift
                    # check shift value greater than the len of alphabet

                    if shift > len(alphabet):
                        shift = shift % len(alphabet)

                    if ch > len(alphabet):
                        alpLeft = ch - len(alphabet)
                        codeChar += alphabet[alpLeft]
                    else:
                        codeChar += alphabet[ch]

                print(f'The encoded text is {codeChar}')

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
    elif again == "no":
        exit()
    else:
        print("Please answer 'yes' or 'no'")


caesar(text=text, shift=shift, direction=direction)
