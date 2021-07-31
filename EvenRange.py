# How to get or find Even Numbers from Number

# Method 1

number = 0
tr = 0
for check in range(1, 101):
    if check % 2 == 0:
        # print(check)
        number += check

print(number)

# Method 2

#
# for check in range(2, 101, 2):
#     print(check)
#     tr += check
#
# print(tr)

