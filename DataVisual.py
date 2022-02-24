import matplotlib.pyplot as plt

print(plt.style.available)

# input_value = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

fig, ax = plt.subplots()

# ax.scatter(input_value, squares, s=100)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.axis([0, 1100, 0, 1100000])

# Here is to draw the plot line

# ax.plot(input_value, squares)

# Set Chart title and label axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
