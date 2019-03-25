import matplotlib.pyplot as plt
'''
squares = [0, 1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

#Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set the size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.show()
