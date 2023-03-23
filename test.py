# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False
#
# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break
#
# if found:
#     print("Element found at index", i)
# else:
#     print("absent")


# myList1 = [1]
# myList2 = myList1[:]
# myList1[0] = 2
# # print(myList2)
#
# newList = []
#
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# for check in my_list:
#     if check not in newList:
#         newList.append(check)
#     # else:
#     #     print(f"{check} already exits")
#
# # newList = my_list.sort()
# print("The list with unique elements only:")
# print(newList)

#
# myList1 = ["X", "Y", "Z"]
# myList2 = myList1
# myList3 = myList2
#
# del myList1[0]
# del myList2[:]
#
# print(myList3)
#
# newSquares = []
# squares = [x * 2 for x in range(1, 13)]
# newSquares.append(squares)
#
# number = 1
#
# odds = [x for x in newSquares if number % 2 != 0]
# print(odds)
#
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y << 1
#
# print(x)

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

# my_list = [i for i in range(-1, 2)]
# print(my_list)
#
#
# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])
#
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])
#
#
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
#
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
#
# print(c + d + e)


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
