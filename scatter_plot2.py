import matplotlib.pyplot as plt

plt.scatter([1,2,3,4,5], [45,50,70,75,85], color='blue', marker='o', label='Group 1')
plt.scatter([1,2,3,4,5], [40,55,65,80,85], color='red', marker='s', label='Group 2')

plt.title('Scatter Plot of Scores vs Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.grid(color='lightgray')
plt.legend()
plt.show()