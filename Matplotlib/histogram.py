import matplotlib.pyplot as plt

scores = [
    45, 67, 78, 89, 56, 72, 91, 63, 84, 76,
    55, 69, 88, 94, 73, 81, 62, 47, 95, 58,
    71, 86, 79, 65, 53, 90, 68, 74, 82, 59,
    77, 92, 61, 85, 70, 49, 96, 64, 87, 75,
    57, 83, 66, 93, 52, 80, 60, 89, 54, 97
]

plt.hist(scores, bins=10, color='lightblue', edgecolor='black')
plt.title("Distribution of Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()