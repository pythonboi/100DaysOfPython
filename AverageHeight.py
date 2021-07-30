# 🚨 Don't change the code below 👇
#count = 0
student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
#
# # Write your code below this row 👇
#     count = count + student_heights[n]
#
# numb = count/len(student_heights)
#
# newNumber = round(numb)
#
# print(f"Average height is {newNumber}")

# Version 2.0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights[n])
addNumber = 0

for h in student_heights:
    addNumber += h
# print(addNumber)

totalCount = 0
for m in student_heights:
    totalCount = totalCount + 1
# print(totalCount)

avegCount = round(addNumber / totalCount)

print(f"Average number is: {avegCount}")
