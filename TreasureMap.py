# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print(map)
position = (input("Where do you want to put the treasure? "))
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


m = list(str(position))
#print(m)

print(type(m[0]))

print(m[0], m[1])

print(m[1])


if m[0] == "1" and m[1] == "1":
    row1[0] = "x"
elif m[0] == "1" and m[1] == "2":
    map[1][0] = "x"
elif m[0] == "1" and m[1] == "3":
    map[2][0] = "x"
elif m[0] == "2" and m[1] == "1":
    map[0][1] = "x"
elif m[0] == "2" and m[1] == "2":
    map[1][1] = "x"
elif m[0] == "2" and m[1] == "3":
    map[2][1] = "x"
elif m[0] == "3" and m[1] == "1":
    map[2][0] = "x"
elif m[0] == "3" and m[1] == "2":
    map[2][1] = "x"
elif m[0] == "3" and m[1] == "3":
    map[2][2] = "x"
else:
    print("ok")


# if m[0] == "0" and m[0] == "0":
#     map[0][0] = "x"
# elif m[0] == "0" and m[1] == "1":
#     map[0][1] = "x"
# elif m[0] == "0" and m[2] == "2":
#     map[0][2] = "x"
# elif map[2] == row1[2] and map[2] == row3[2]:
#     map[2][2] = "x"

# row3[2] = "x"
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
