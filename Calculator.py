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

    num2 = float(input("What is the next number? "))

    # For loop to verify the sign matches with the symbol in the operations dictionary
    for symbol in operations:

        # Validate/Check if the signs and symbol are the same values
        if signs == symbol:

            # Assign the value of the dictionary operation to the result variable
            result = operations[symbol]

            # Do the calculation base on the dictionary value of the result for num1 and num2
            finalResult = result(num1, num2)

    # Print out the finalResult using the f string print format
    print(f"{num1} {signs} {num2} = {finalResult}")

    # Create a question variable for use input
    questions = input(
        f"Type 'y' to continue calculating with {finalResult}, or type 'n' to start a new calculation.: ")

    # Create a while loop for continuous calculation
    while True:

        # Check and validate the user input if 'y' is yes
        if questions == 'y':

            # Type or choose a new symbol
            signs = input("Pick an operation: ")

            nxt = float(input("What is the next number?: "))

            # Assign the value of the operations direction of the signs input to theSign variable
            theSign = operations[signs]
            theResult = theSign(finalResult, nxt)

            # Use the F string format to print out the theResult
            print(f"{finalResult} {signs} {nxt} = {theResult}")

            # Accept user input and assigned it to the questions string variable
            questions = input(
                f"Type 'y' to continue calculating with {theResult}, or type 'n' to start a new calculation.: ")

        # Validate the questions is 'y' and assigned the theResult value to the finalResult variable
        if questions == 'y' and finalResult != theResult:
            finalResult = theResult

        # Call the Calculator function when 'n' is selected
        if questions == 'n':
            calculator()

        # Break out of the loop if any alphabet is selected except 'y' and 'n'
        if questions != 'y' and questions != 'n':
            break


calculator()
