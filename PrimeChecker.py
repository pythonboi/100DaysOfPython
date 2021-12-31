numb = False


def primenumber(number):
    for numbers in range(2, number):
        if number % numbers != 0:
            numb = True
        # if numb = False:
        print("it is not a prime number")
    else:
        print("it is prime number")
        # if numbers % 2 != 0 and numbers > 1  :
        #
        #     #if numbers % 5 != 0 and numbers % 7 != 0:
        #     print(f"{numbers} is a prime number")
        # # else:
        # #     print(f"{numbers} is not a prime number")


primenumber(number=n)

# prime = []
# notPrime = []
#
# number = int(input("Enter a number: "))
# is_prime = True
# for numbers in range(2, number):
#     if number % numbers == 0:
#
#     #if number % numbers != 0:
#         is_prime = False
# if is_prime:
#     print("This is a prime number")
# else:
#     print("This is not a prime")
# prime.append(numbers)
# prime += numbers
# print(f"{number} it's a prime number")
# elif number % numbers == 0:
#     #notPrime.append(numbers)
#     #print(f"{number} it is not a prime")
# else:
#     print("it is not a prime")

# print(f"prime are {prime}")
# print(f"not prime are {notPrime}")

# q = []
# kl = []
#
# for m in range(2, number):
#     if m not in prime:
#         q.append(m)
#
# for m in range(2, number):
#     if m not in notPrime:
#         q.append(m)
#
# for bic in range(2, number):
#     if bic not in q:
#         kl.append(bic)
#
# print(q)
# print(kl)
