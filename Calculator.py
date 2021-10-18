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


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


num1 = int(input("What is the first number?: "))

for operation in operations:
    print(operation)

signs = input("Pick an operation from the line above: ")

num2 = int(input("What is the second number? "))

for symbol in operations:
    if signs == symbol:
        result = operations[symbol]
        finalResult = result(num1, num2)


print(f"{num1} {signs} {num2} = {finalResult}")

questions = input(f"Type 'y' to continue calculating with {finalResult}, or type 'n' to exit.: ")

while True:

    if questions == 'y':
        # print(f"Type 'y' to continue calculating with {finalResult}, or type 'n' to exit.: ")
        signs = input("Pick an operation: ")

        nxt = int(input("What is the next number?: "))

        theSign = operations[signs]
        theResult = theSign(finalResult, nxt)

        print(f"{finalResult} {signs} {nxt} = {theResult}")

    questions = input(f"Type 'y' to continue calculating with {theResult}, or type 'n' to exit.: ")

    if questions == 'n':
        break
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