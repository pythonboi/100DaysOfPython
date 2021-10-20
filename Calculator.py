from art import logoCal


# Create a function for Adding
def add(n1, n2):
    return n1 + n2


# Create a function for Subtracting
def subtract(n1, n2):
    return n1 - n2


# Create a function for Multiplication
def multiply(n1, n2):
    return n1 * n2


# Create a function for Division
def divide(n1, n2):
    return n1 / n2


# Create a dictionary for the arithmetic symbols
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# Create a calculator function
def calculator():
    # Print the Calculator logo from the art.py
    print(logoCal)

    # Create the first variable number
    num1 = float(input("What is the first number?: "))

    for operation in operations:
        print(operation)

    signs = input("Pick an operation from the line above: ")

    num2 = float(input("What is the second number? "))

    # For loop to verify the sign matches with the symbol in the operations dictionary
    for symbol in operations:
        if signs == symbol:
            result = operations[symbol]
            finalResult = result(num1, num2)

    print(f"{num1} {signs} {num2} = {finalResult}")

    questions = input(f"Type 'y' to continue calculating with {finalResult}, or type 'n' to start a new calculation.: ")

    # Create a while loop for continuous calculation
    while True:

        # questions = input(
        #     f"Type 'y' to continue calculating with {finalResult}, or type 'n' to start a new calculation.: ")

        # Check and validate the user input if yes
        if questions == 'y':
            # print(f"Type 'y' to continue calculating with {finalResult}, or type 'n' to exit.: ")
            signs = input("Pick an operation: ")

            nxt = float(input("What is the next number?: "))

            theSign = operations[signs]
            theResult = theSign(finalResult, nxt)

            print(f"{finalResult} {signs} {nxt} = {theResult}")

            questions = input(
                f"Type 'y' to continue calculating with {theResult}, or type 'n' to start a new calculation.: ")
        # Check
        if questions == 'y' and finalResult != theResult:
            finalResult = theResult
            # print(finalResult)

        # Break out of the loop if n alphabet is selected
        if questions == 'n':
            calculator()
            # break
        elif questions != 'y' and questions != 'n':
            break
        # else:
        #     break


calculator()

# print(f"{final}")
# else:
#     print("Please enter 'y' for yes or 'n' for no and exit.")

# ThirdOperation = input("Pick another operation: ")
#
# num3 = int(input("What is the next number?: "))
#
# ThirdPick = operations[ThirdOperation]
#
# thirdResult = ThirdPick(finalResult, num3)
#
# print(f"{finalResult} {ThirdOperation} {num3} = {thirdResult}")
