# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
#
#
# # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#
# # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# # e.g.
# # cipher_text = "mjqqt"
# # shift = 5
# # plain_text = "hello"
# # print output: "The decoded text is hello"
#
#
# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# encrypt(plain_text=text, shift_amount=shift)
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # Scores 91 - 100:
# Grade1 = "Outstanding"
# #
# # Scores 81 - 90:
# Grade2 = "Exceeds Expectations"
# #
# # Scores 71 - 80:
# #
# Grade3 = "Acceptable"
# #
# # Scores 70 or lower:
# Grade4 = "Fail"
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for k, v in student_scores.items():
#     if v >= 91 and v <= 100:
#         student_grades[k] = Grade1
#     elif v >= 81 and v <= 90:
#         student_grades[k] = Grade2
#     elif v >= 71 and v <= 80:
#         student_grades[k] = Grade3
#     else:
#         student_grades[k] = Grade4
# # 🚨 Don't change the code below 👇
# print(student_grades)
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_Visited": 5},
#     "Canada": {"cities_visited": ["Toronto", "Calgary", "Edmonton"], "Total_Visited": 12},
#
# }

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

# def add_new_country(country, visits, cities):
#     newDict = {}
#
#     newDict['country'] = country
#     newDict['visits'] = visits
#     newDict['cities'] = cities
#
#     # print(newDict)
#     travel_log.append(newDict)

# newDict['country'] = country
# check['country'] = country
# check['visits'] = visits
# check['cities'] = cities


# 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# print(travel_log[0])

# theCountry = input("what country you visited: ").lower()
# theVisits = int(input("how many visits: "))
# theCities = input("Enter the cities you've visited: ").title()
# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }
#
# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }
#
# print(starting_dictionary)
# print(final_dictionary)
#
# final_dictionary = starting_dictionary["c"] = 7
#
# #final_dictionary = starting_dictionary
#
# print(final_dictionary)
#
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
#
# dict[1] = 4

def format_name(f_name, l_name):

    f_name = input("what is your first name:? ").title()
    l_name = input("what is your last name:? ").title()

    print(f_name.title())
    print(l_name.title())


format_name(f_name="tommy", l_name="vicky")

# what is your first name:? Jane
# what is your last name:? Tom

# A) Jane
# B) Tom
# C) Tommy
# D) Vicky

# What is your answer to the running code below?:

# def outside_function(x, y):
#     def inside_function(m, n):
#         return m + n
#
#     return inside_function(x, y)
#
#
# answer = outside_function(10, 20)
# print(answer)

# A) SyntaxError
# B) 10
# C) 20
# D) 30
# E) (10, 20)
# F) NameError
