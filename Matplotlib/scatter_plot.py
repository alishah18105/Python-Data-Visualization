import matplotlib.pyplot as plt

hours_studied = [1,2,3,4,5]
scores = [45,50,70,75, 85]

plt.scatter(hours_studied, scores, color='blue', marker='o', label='Scores vs Hours Studied')
plt.title('Scatter Plot of Scores vs Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.grid(color='lightgray')
plt.legend()
plt.show()