# Import the art ASCII logo
import art

# create a list of alphabet characters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Print the art logo from the import art
print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# create a function for 3 parameters text, shift, direction

def caesar(text, shift, direction):
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))

    codeChar = ''
    # check and validate direction
    if direction == 'encode':
        # loop through the text
        for me in text:
            if shift > len(alphabet):
                shift = shift % len(alphabet)
            # check variable or value not in the alphabet list
            if me not in alphabet:
                codeChar += me
            else:
                ch = alphabet.index(me) + shift
            # Check if the ch variable is greater than the total alphabet character in the list
            if ch > len(alphabet):
                alpLeft = ch - len(alphabet)
                codeChar += alphabet[alpLeft]
            else:
                codeChar += alphabet[ch]

        print(f'The encoded text is: {codeChar}')

    # check if the direction string match decode
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

        print(f'The decoded text is: {decChar}')


caesar(text=text, shift=shift, direction=direction)

# continue looping through the code until the variable match
while True:

    # Get an input response
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ""\n").lower()

    # check if user want to go again encode or decode
    if again == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text=text, shift=shift, direction=direction)
    # exit if user not interested to encode or decode
    elif again == "no":
        print("Goodbye")
        exit()
    # make sure users response to yes or no
    else:
        print("Please answer 'yes' or 'no'")
